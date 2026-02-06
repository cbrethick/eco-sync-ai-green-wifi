from flask import Flask, render_template, jsonify
from src.realtime_collector import collect
from src.ai_predictor import Predictor
from src.adaptive_power import decide
from src.energy_model import energy, co2

app = Flask(__name__)

predictor = Predictor()
total_energy_saved = 0.0
total_co2_saved = 0.0
baseline_energy = 10  # 10W always ON

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    global total_energy_saved, total_co2_saved

    stats = collect()
    predictor.update(stats["traffic_mb_s"])
    prediction = predictor.predict()

    power = decide(prediction)

    baseline_energy = 10          # Wh per interval (baseline)
    eco_energy = energy(power)    # Wh per interval (Eco-Sync)

    energy_saved = max(baseline_energy - eco_energy, 0)
    co2_saved = co2(energy_saved)

    total_energy_saved += energy_saved
    total_co2_saved += co2_saved

    return jsonify({
        "time": stats["time"],
        "traffic": stats["traffic_mb_s"],
        "predicted": round(prediction, 4) if prediction else None,
        "power": power,
        "baseline_energy": round(baseline_energy, 2),
        "eco_energy": round(eco_energy, 2),
        "energy_saved": round(energy_saved, 2),
        "total_energy_saved": round(total_energy_saved, 2),
        "total_co2_saved": round(total_co2_saved, 6)
    })




if __name__ == "__main__":
    app.run()


