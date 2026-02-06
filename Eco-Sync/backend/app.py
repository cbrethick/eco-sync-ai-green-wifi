from flask import Flask, jsonify
from src.realtime_collector import collect
from src.ai_predictor import Predictor
from src.adaptive_power import decide
from src.energy_model import energy, co2
import os
app = Flask(__name__)

predictor = Predictor()
total_energy_saved = 0.0
total_co2_saved = 0.0

@app.route("/")
def health():
    return jsonify({
        "status": "Eco-Sync backend is running",
        "endpoint": "/data"
    })

@app.route("/data")
def data():
    global total_energy_saved, total_co2_saved

    stats = collect()
    predictor.update(stats["traffic_mb_s"])
    prediction = predictor.predict()

    power = decide(prediction)

    baseline_energy = 10
    eco_energy = energy(power)

    energy_saved = max(baseline_energy - eco_energy, 0)
    co2_saved = co2(energy_saved)

    total_energy_saved += energy_saved
    total_co2_saved += co2_saved

    return jsonify({
        "traffic": round(stats["traffic_mb_s"], 4),
        "predicted": round(prediction, 4) if prediction else None,
        "power": power,
        "baseline_energy": baseline_energy,
        "eco_energy": round(eco_energy, 2),
        "total_energy_saved": round(total_energy_saved, 2),
        "total_co2_saved": round(total_co2_saved, 6)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
