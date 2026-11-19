# Journal des incidents

## Incident n°1

**Partie / étape :** Partie 2 - Étape 2.4 (Exécution du conteneur Docker)
**Symptôme observé :** `curl localhost:8080` échoue avec `curl: (56) Recv failure: Connection reset by peer` alors que le conteneur est `Up` dans `docker ps`.
**Diagnostic :** `docker ps` et `docker logs mon-app` montrent `Listening at: http://127.0.0.1:8080`.
**Cause racine :** Gunicorn n'écoute que sur l'interface loopback (`127.0.0.1`) à l'intérieur du conteneur, ce qui bloque le trafic entrant mappé par `-p 8080:8080`.
**Correction appliquée :** Remplacement de `127.0.0.1:8080` par `0.0.0.0:8080` dans la directive `CMD` du `Dockerfile`, puis reconstruction de l'image.
**Comment l'éviter à l'avenir :** Toujours binder les services conteneurisés sur `0.0.0.0` et tester la réponse HTTP depuis l'extérieur du conteneur après build.

## Incident n°2

**Partie / étape :** Partie 3 - Étape 3.1 / 3.4 (Workflow GitHub Actions `ci-cd.yml`)
**Symptôme observé :** Aucun pipeline ne se déclenche sur `push` lors de la fusion d'une Pull Request vers la branche `main`.
**Diagnostic :** Lecture du déclencheur `on.push.branches` dans le modèle `.github/workflows/ci-cd.yml` fourni par l'équipe (`branches: [master]`) alors que `git branch` montre que la branche par défaut du dépôt est `main`.
**Cause racine :** Incohérence entre le nom de la branche configurée dans le workflow (`master`) et la branche principale réelle du dépôt GitHub (`main`).
**Correction appliquée :** Remplacement de `branches: [master]` par `branches: [main]` dans `.github/workflows/ci-cd.yml`.
**Comment l'éviter à l'avenir :** Vérifier le nom de la branche par défaut du dépôt (`main`) lors de la mise en place des déclencheurs CI/CD.
