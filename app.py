from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/real-route", methods=["POST"])
def real_route():
    try:
        data = request.json
        start = data["start"]
        end = data["end"]

        # ✅ Use HTTPS (important for deployment)
        url = f"https://router.project-osrm.org/route/v1/driving/{start[1]},{start[0]};{end[1]},{end[0]}?overview=full&geometries=geojson"

        res = requests.get(url, timeout=10)
        res.raise_for_status()

        data = res.json()

        if "routes" not in data or len(data["routes"]) == 0:
            return jsonify({"error": "No route found"}), 400

        coords = data["routes"][0]["geometry"]["coordinates"]

        # Convert [lon, lat] → [lat, lon]
        route = [[c[1], c[0]] for c in coords]

        return jsonify({"route": route})

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"error": "Failed to fetch route"}), 500


if __name__ == "__main__":
    print("🚀 Smart Ambulance System Running...")
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )