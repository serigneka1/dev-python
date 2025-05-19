from flask import Flask, render_template, request
import requests
from data import villes_france, api_key

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    resultats = []

    # Récupérer la ville passée en paramètre POST
    if request.method == "POST":
        ma_ville = request.form.get("ma-ville")

        if ma_ville:
            ma_ville = ma_ville.lower()
            if ma_ville in villes_france:
                lat, lon = villes_france[ma_ville]
                url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    temp_k = data["main"]["temp"]
                    temp_c = round(temp_k - 273.15, 2)
                    resultats.append({"ville": ma_ville.capitalize(), "temp": temp_c})
                else:
                    resultats.append({"ville": ma_ville.capitalize(), "temp": "Erreur API"})
            else:
                resultats.append({"ville": ma_ville.capitalize(), "temp": "Ville inconnue"})

    return render_template("home.html", villes=resultats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)