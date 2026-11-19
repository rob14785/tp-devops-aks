"""Application de démonstration pour le TP DevOps."""
import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def accueil():
    return jsonify(
        message=os.getenv("MESSAGE", "Bonjour depuis AKS !"),
        version=os.getenv("APP_VERSION", "dev"),
        pod=socket.gethostname(),
    )


@app.get("/health")
def health():
    """Sonde de vivacité (liveness)."""
    return jsonify(status="ok")


@app.get("/ready")
def ready():
    """Sonde de disponibilité (readiness)."""
    return jsonify(status="ready")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
