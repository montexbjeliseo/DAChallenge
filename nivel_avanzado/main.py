from flask import Flask, render_template, request, jsonify
from api import get_current_weather_data, get_forecast_data
from utils import day
from template_tags import unique
from itertools import groupby


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    forecast_data = None
    errors = []
    
    if request.method == "POST":
        city = request.form["city"]
        weather_data = get_current_weather_data(city)
        

        if not weather_data:
            errors.append("Asegúrese de haber escrito bien el nombre de la ciudad")
            return render_template(
                "index.html", 
                weather_data=None, 
                errors=errors, 
                forecast_data=None
            ), 400
            
        forecast_data = get_forecast_data(city)

    return render_template(
        "index.html", weather_data=weather_data, errors=errors, forecast_data=forecast_data
    )


@app.route("/api/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "Debe proporcionar el nombre de una ciudad."}), 400

    weather_data = get_current_weather_data(city)

    if not weather_data:
        return (
            jsonify(
                {
                    "error": "No se pudo obtener los datos climáticos para la ciudad proporcionada."
                }
            ),
            404,
        )

    return jsonify(weather_data), 200


if __name__ == "__main__":
    app.run(debug=True)
