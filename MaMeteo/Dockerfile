# Utilise une image Python légère
FROM python:3.11-slim

# Variables d'environnement pour de meilleures pratiques
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier les dépendances d'abord pour tirer parti du cache Docker
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste du projet (app.py, templates/, etc.)
COPY . .

# Exposer le port (facultatif mais conseillé)
EXPOSE 5000

# Lancer le serveur Flask
CMD ["python", "app.py"]

