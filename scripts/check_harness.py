"""Validate repository state without network, third-party packages or mutations."""
import argparse
import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATES = {"pending", "in_progress", "blocked", "done"}
HANDOFF_STATES = {"draft", "ready", "in_review", "closed", "blocked"}
REQUIRED = [
    "AGENTS.md", "CLAUDE.md", "CHECKPOINTS.md", "README.md", "init.ps1",
    "docs/setup-step-by-step.md", "docs/context/project-context.md",
    "docs/notebooklm.md", "progress/current.md", "progress/history.md",
    ".specify/memory/constitution.md", ".specify/integration.json",
    ".mcp.json", ".codex/config.toml", "feature_list.json",
]
PROFILES = ["implementer", "frontend", "backend", "catalog-infrastructure",
            "qa", "security-reviewer", "documenter"]


class InvalidHarness(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise InvalidHarness(message)


def local_path(root, value):
    require(isinstance(value, str) and value.strip(), "Ruta vacia o invalida")
    path = (root / value).resolve()
    require(path.is_relative_to(root.resolve()), f"Ruta fuera del repositorio: {value}")
    return path


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def validate_features(root, data):
    require(data.get("schema_version") == 1, "Version de indice desconocida")
    features = data.get("features")
    require(isinstance(features, list) and features, "Indice de funcionalidades vacio")
    ids = set()
    for feature in features:
        fid = feature.get("id")
        require(isinstance(fid, str) and fid and fid not in ids, f"ID invalido o duplicado: {fid}")
        ids.add(fid)
        require(feature.get("status") in STATES, f"Estado invalido: {fid}")
        require(feature.get("owner") in {"codex", "claude-code"}, f"Responsable invalido: {fid}")
        if feature.get("spec_dir"):
            require((local_path(root, feature["spec_dir"]) / "spec.md").is_file(), f"Spec ausente: {fid}")
        if feature["status"] == "done":
            require(feature.get("evidence"), f"Falta evidencia de cierre: {fid}")
            require(local_path(root, feature["evidence"]).is_file(), f"Evidencia ausente: {fid}")
    require(sum(f["status"] == "in_progress" for f in features) <= 1,
            "Solo puede haber una funcionalidad in_progress")
    return features


def validate_handoff(root, handoff, features, implementation=False):
    fid = handoff.get("feature_id")
    feature = next((f for f in features if f["id"] == fid), None)
    require(feature is not None, f"Entrega sin funcionalidad: {fid}")
    require(handoff.get("status") in HANDOFF_STATES, f"Estado de entrega invalido: {fid}")
    require(handoff.get("planner") == "codex", "Solo Codex prepara la entrega")
    require(handoff.get("executor") == "claude-code", "Solo Claude Code implementa")
    require(handoff.get("spec_dir") == feature.get("spec_dir"), f"Spec no coincide: {fid}")
    spec_dir = local_path(root, handoff.get("spec_dir"))
    for key in ["task_ids", "allowed_paths", "verification_commands", "blockers"]:
        require(isinstance(handoff.get(key), list), f"Campo debe ser lista: {key}")
    for key in ["implementation_report", "review_report"]:
        local_path(root, handoff.get(key))
    if implementation:
        require(handoff["status"] == "ready", "Entrega no esta ready; no iniciar implementacion")
    if handoff["status"] == "ready":
        require(feature["status"] == "in_progress", "La entrega ready requiere feature in_progress")
        require(not handoff["blockers"], "Entrega ready con bloqueos")
        for filename in ["spec.md", "plan.md", "tasks.md"]:
            path = spec_dir / filename
            require(path.is_file() and path.read_text(encoding="utf-8").strip(), f"Falta {filename}: {fid}")
        tasks = (spec_dir / "tasks.md").read_text(encoding="utf-8")
        pending = set(re.findall(r"^\s*- \[ \]\s+(T\d+)\b", tasks, re.M))
        task_ids = handoff["task_ids"]
        require(task_ids and all(isinstance(t, str) for t in task_ids), "Faltan IDs de tareas")
        require(len(task_ids) == len(set(task_ids)), "IDs de tarea duplicados")
        require(set(task_ids) <= pending, "La entrega referencia tareas ausentes o completadas")
        require(handoff["allowed_paths"], "Falta alcance de archivos")
        for path in handoff["allowed_paths"]:
            local_path(root, path)
        commands = handoff["verification_commands"]
        require(commands and all(isinstance(c, str) and c.strip() for c in commands), "Faltan comandos de verificacion")
        require(all(not re.search(r"<[^>]+>|TODO|PENDIENTE", c, re.I) for c in commands),
                "Los comandos de verificacion contienen marcadores sin resolver")


def validate(root, implementation_handoff=None):
    for filename in REQUIRED:
        require((root / filename).is_file(), f"Falta archivo: {filename}")
    for profile in PROFILES:
        path = root / ".claude/agents" / f"{profile}.md"
        require(path.is_file(), f"Falta perfil: {profile}")
        content = path.read_text(encoding="utf-8")
        require(content.startswith("---\n") and f"name: {profile}" in content, f"Perfil invalido: {profile}")
    integrations = load_json(root / ".specify/integration.json")
    require({"codex", "claude"} <= set(integrations.get("installed_integrations", [])), "Falta integracion Spec Kit")
    for directory in [".agents", ".claude"]:
        for skill in ["constitution", "specify", "clarify", "plan", "tasks", "analyze", "implement", "converge"]:
            require((root / directory / "skills" / f"speckit-{skill}" / "SKILL.md").is_file(), f"Falta skill: {directory}/{skill}")
    mcp = load_json(root / ".mcp.json")["mcpServers"]["notebooklm"]
    codex = tomllib.loads((root / ".codex/config.toml").read_text(encoding="utf-8"))
    require(mcp["command"] == codex["mcp_servers"]["notebooklm"]["command"], "Clientes usan distintos servidores MCP")
    features = validate_features(root, load_json(root / "feature_list.json"))
    for path in sorted((root / "handoffs").glob("*.json")):
        if path.name != "template.json":
            validate_handoff(root, load_json(path), features)
    if implementation_handoff:
        validate_handoff(root, load_json(local_path(root, implementation_handoff)), features, implementation=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--implementation-ready", metavar="HANDOFF_JSON")
    args = parser.parse_args()
    try:
        validate(ROOT, args.implementation_ready)
    except (InvalidHarness, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("OK: estructura, integraciones, referencias, estados y entregas del arnes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
