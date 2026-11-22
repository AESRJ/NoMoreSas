## User
- `User.id`, `User.email`, `User.createdAt`: contratos003 y unicidadcorreo preservados. Email externo cambiante no cambiaUUID existente.
## PasswordCredential
- `PasswordCredential.userId`: UUIDPK/FKusers ONDELETECASCADE, una porcuentalocal, opcional paracuentasGoogle.
- `PasswordCredential.passwordHash`: stringArgon2id real copiado exactamente desdeusers enmigración, nunca texto ni hashficticio paraGoogle.
## ExternalIdentity
- `ExternalIdentity.provider`: enumgoogle.
- `ExternalIdentity.subject`: string1–255, sub verificado, UNIQUE(provider,subject).
- `ExternalIdentity.userId`: UUIDFKusers, vínculo únicoGoogleporusuario enMVP.
- `ExternalIdentity.createdAt`: ISOservidor; no tokensGoogle.
## OAuthAttempt
- `OAuthAttempt.sessionHash`: SHA256 del ID de sesión del servidor, ligado a la presesión; nunca aceptar intento de otra sesión.
- `OAuthAttempt.stateHash`: SHA256 de32bytesaleatorios, PK; nunca aceptar estado de otra sesión.
- `OAuthAttempt.nonceHash`: hash de32bytesaleatorios enviadoscomo nonce, comparación después deIDtoken.
- `OAuthAttempt.verifier`: PKCEaleatorio43–128caracteres, solo transitorio en tabla oauth_attempts privada con TTL5min; expira y se elimina, no escredencial permanente.
- `OAuthAttempt.purpose`: login|link.
- `OAuthAttempt.expectedUserId`: nullparalogin;UUID de sesiónparalink, cambia→rechazo.
- `OAuthAttempt.expiresAt`: timestampservidor ahora+5min.
- `OAuthAttempt.returnTo`: enum interno projects|account, no URLexterna.
- `OAuthAttempt.consumed`: estado lógico consumido mediante DELETE RETURNING atómico una vez, incluso anteerror de canje para impedirreplay.
Intentos ligados a la sesiónprivada003, no navegadorstorage. Estado/nonce/verifier/códigos no se guardan en memoriaexterna ni Git/logs.
