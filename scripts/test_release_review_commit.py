"""Verifica snapshots del arnes en repositorios Git temporales, sin producto."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReviewedSnapshotTests(unittest.TestCase):
    def setUp(self):
        local = (ROOT / '.local').resolve()
        local.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix='review-snapshot-test-', dir=local)
        self.scratch = Path(self.temp.name).resolve()
        self.assertTrue(self.scratch.is_relative_to(local))
        self.repo = self.scratch / 'repo'
        self.repo.mkdir()
        self.env = os.environ.copy()
        self.env.update(GIT_AUTHOR_NAME='AESRJ', GIT_AUTHOR_EMAIL='vasquez.jorge@uabc.edu.mx',
                        GIT_COMMITTER_NAME='AESRJ', GIT_COMMITTER_EMAIL='vasquez.jorge@uabc.edu.mx',
                        PYTHONUTF8='1')
        for name in ['GIT_AUTHOR_DATE', 'GIT_COMMITTER_DATE']:
            self.env.pop(name, None)
        self.git('init', '-q')
        self.git('checkout', '-b', 'feat/revision-y-railway')
        (self.repo / 'file.txt').write_text('base\n', encoding='utf-8')
        self.git('add', 'file.txt')
        self.git('commit', '-qm', 'fixture: base de prueba del arnes')
        self.base = self.git('rev-parse', 'HEAD')
        accepted = self.git('hash-object', '-w', '--stdin', input='accepted\n')
        (self.repo / 'file.txt').write_text('later\n', encoding='utf-8')
        scripts = self.scratch / 'scripts'
        scripts.mkdir()
        source = (ROOT / 'scripts/release_review_commit.py').read_text(encoding='utf-8')
        original = "repo=Path('C:/Users/Roel/Documents/NoMoreSaaS_Frontend')"
        self.assertIn(original, source)
        self.helper = scripts / 'release_review_commit.py'
        self.helper.write_text(source.replace(original, 'repo=Path(' + repr(self.repo.as_posix()) + ')'), encoding='utf-8')
        reviews = self.scratch / '.local/release-reviews'
        reviews.mkdir(parents=True)
        self.review_path = reviews / '006-acceso-google-T005.json'
        self.review = dict(reviewer='codex', accepted=True, feature='006-acceso-google', task='T005',
                           base_commit=self.base, title='fixture', body='Prueba aislada del arnes.',
                           verification=['fixture'], paths=['file.txt'],
                           reviewed_blobs={'file.txt': {'oid': accepted, 'mode': '100644'}})

    def tearDown(self):
        self.assertTrue(self.scratch.is_relative_to((ROOT / '.local').resolve()))
        self.temp.cleanup()

    def git(self, *args, input=None):
        return subprocess.check_output(['git', *args], cwd=self.repo, env=self.env, input=input,
                                       text=True, encoding='utf-8', stderr=subprocess.PIPE).strip()

    def prepare(self):
        self.review_path.write_text(json.dumps(self.review), encoding='utf-8')
        return subprocess.run(['python', str(self.helper), '006-acceso-google', 'T005', '--prepare'],
                              cwd=self.scratch, env=self.env, capture_output=True, text=True, encoding='utf-8')

    def test_freezes_accepted_blob_without_changing_later_work(self):
        result = self.prepare()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.git('show', ':file.txt'), 'accepted')
        self.assertEqual((self.repo / 'file.txt').read_text(encoding='utf-8'), 'later\n')
        pending = json.loads((self.scratch / '.local/release-pending-commit.json').read_text())
        self.assertEqual(pending['tree'], self.git('write-tree'))

    def test_invalid_object_rejected_before_any_path_is_staged(self):
        self.review['paths'].append('second.txt')
        self.review['reviewed_blobs']['second.txt'] = {'oid': self.base, 'mode': '100644'}
        result = self.prepare()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Objeto revisado no es blob', result.stderr)
        self.assertEqual(self.git('diff', '--cached', '--name-only'), '')

    def test_existing_index_is_preserved(self):
        (self.repo / 'other.txt').write_text('unrelated\n', encoding='utf-8')
        self.git('add', 'other.txt')
        before = self.git('write-tree')
        result = self.prepare()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('ndice previo ocupado', result.stderr)
        self.assertEqual(self.git('write-tree'), before)

    def test_original_working_tree_staging_remains_available(self):
        self.review.pop('reviewed_blobs')
        result = self.prepare()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.git('show', ':file.txt'), 'later')


if __name__ == '__main__':
    unittest.main()
