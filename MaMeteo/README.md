# MaMeteo

Application Flask pour afficher la température actuelle d’une ville française via l’API OpenWeatherMap.

---

## Fonctionnalités

- Recherche de la température par ville (Paris, Bordeaux, etc.)
- Affichage en degrés Celsius
- Déploiement possible avec Docker

---

## Installation

1. Cloner le dépôt :
```bash
git clone <URL_DE_TON_REPO>
cd MaMeteo
```
2. Créer un environnement virtuel et installer les dépendances :
```bash
python -m venv venv
source venv/bin/activate  # sur Linux/macOS
venv\Scripts\activate     # sur Windows
pip install -r requirements.txt
```
3. Configurer l’API key dans data.py.

4. Utilisation
- Lancer l’application Flask :
```bash
python app.py
```
- Avec Docker
a- Construire l’image Docker :
```bash
docker build -t MaMeteo .
```
b- Lancer le conteneur :
```bash
docker run -p 5000:5000 MaMeteo
```
Ouvrir dans le navigateur : http://localhost:5000




