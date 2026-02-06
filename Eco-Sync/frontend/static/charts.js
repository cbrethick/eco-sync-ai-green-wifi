let labels = [];

let trafficData = [];
let predictedData = [];
let powerData = [];

let baselineEnergyData = [];
let ecoEnergyData = [];

const trafficChart = new Chart(
    document.getElementById("trafficChart"), {
        type: "line",
        data: {
            labels,
            datasets: [
                { label: "Real Traffic (MB/s)", data: trafficData },
                { label: "Predicted Traffic (MB/s)", data: predictedData }
            ]
        }
    }
);

const powerChart = new Chart(
    document.getElementById("powerChart"), {
        type: "line",
        data: {
            labels,
            datasets: [
                { label: "Power Level (%)", data: powerData }
            ]
        }
    }
);

const energyChart = new Chart(
    document.getElementById("energyChart"), {
        type: "line",
        data: {
            labels,
            datasets: [
                { label: "Baseline Energy (Wh)", data: baselineEnergyData },
                { label: "Eco-Sync Energy (Wh)", data: ecoEnergyData }
            ]
        }
    }
);

async function updateDashboard() {
    const res = await fetch("/data");
    const data = await res.json();
    document.getElementById("energySaved").innerText =
    data.total_energy_saved + " Wh";

    document.getElementById("co2Saved").innerText =
    data.total_co2_saved + " kg";

    labels.push(data.time);

    trafficData.push(data.traffic);
    predictedData.push(data.predicted);
    powerData.push(data.power);

    baselineEnergyData.push(data.baseline_energy);
    ecoEnergyData.push(data.eco_energy);

    if (labels.length > 20) {
        labels.shift();
        trafficData.shift();
        predictedData.shift();
        powerData.shift();
        baselineEnergyData.shift();
        ecoEnergyData.shift();
    }

    trafficChart.update();
    powerChart.update();
    energyChart.update();
}

setInterval(updateDashboard, 5000);
