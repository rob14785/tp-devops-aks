# Journal des incidents

## Incident n°1

**Partie / étape :** Partie 2 - Étape 2.4 (Exécution du conteneur Docker)
**Symptôme observé :** `curl localhost:8080` échoue avec `curl: (56) Recv failure: Connection reset by peer` alors que le conteneur est `Up` dans `docker ps`.
**Diagnostic :** `docker ps` et `docker logs mon-app` montrent `Listening at: http://127.0.0.1:8080`.
**Cause racine :** Gunicorn n'écoute que sur l'interface loopback (`127.0.0.1`) à l'intérieur du conteneur, ce qui bloque le trafic entrant mappé par `-p 8080:8080`.
**Correction appliquée :** Remplacement de `127.0.0.1:8080` par `0.0.0.0:8080` dans la directive `CMD` du `Dockerfile`, puis reconstruction de l'image.
**Comment l'éviter à l'avenir :** Toujours binder les services conteneurisés sur `0.0.0.0` et tester la réponse HTTP depuis l'extérieur du conteneur après build.
