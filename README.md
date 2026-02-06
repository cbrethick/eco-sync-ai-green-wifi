🌱 Eco-Sync – AI-Native Green Wi-Fi Manager

Eco-Sync is an AI-powered Green Wi-Fi Management system designed to reduce unnecessary energy consumption in wireless networks. Traditional Wi-Fi routers operate at full power even during idle or low-usage periods, leading to wasted electricity and increased carbon emissions. Eco-Sync addresses this problem by predicting Wi-Fi usage patterns using AI and dynamically adjusting router power levels, while maintaining user experience.
This project aligns with the AI for Good vision by promoting energy-efficient, sustainable, and intelligent networking.

🚀 Key Features
📊 Real-time Wi-Fi traffic monitoring
🤖 AI-based traffic prediction
⚡ Adaptive router power control
🔋 Baseline vs Eco-Sync energy comparison
🌍 Live CO₂ emission reduction tracking
📈 Interactive dashboard with charts
⏱️ Updates every 5 seconds
🧠 How Eco-Sync Works

Traffic Collection
Real-time (simulated) Wi-Fi traffic data is collected continuously.

AI Prediction
A lightweight machine-learning model predicts near-future network usage based on recent traffic patterns.

Adaptive Power Decision
Based on the predicted usage:

Low traffic → power reduced
Medium traffic → moderate power
High traffic → full power

Energy & CO₂ Calculation
Eco-Sync compares:

Baseline router (always ON at full power)
Eco-Sync router (AI-controlled)
and calculates energy saved and CO₂ emissions reduced.

Visualization
A user-friendly dashboard visualizes:
Real vs predicted traffic
Router power levels
Energy usage comparison
Total energy and CO₂ saved

🖥️ Tech Stack
Backend

Python
Flask
Custom AI logic (lightweight predictor)

Frontend

HTML
CSS
JavaScript
Chart.js
Deployment

Backend: Render
Frontend: Static hosting (local / Vercel)

▶️ How to Run Locally (VS Code)
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the backend
python app.py

3️⃣ Open in browser
http://127.0.0.1:5030

🌍 Real-World Impact

Reduces unnecessary energy usage in Wi-Fi infrastructure
Lowers carbon emissions at scale
Demonstrates how AI can optimize network resources responsibly
Can be extended to smart homes, campuses, enterprises, and ISPs

🧪 Current Status

✔ Fully working prototype
✔ Real-time dashboard
✔ AI-based decision logic
✔ Cloud-deployable backend

Future extensions may include:

Real router integration
Advanced ML models
Multi-router optimization
Carbon-aware scheduling
