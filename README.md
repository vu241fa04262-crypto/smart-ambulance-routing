# 🚑 Smart Ambulance Routing System

A real-time intelligent web application that optimizes ambulance routes using GPS simulation, dynamic routing, and traffic analytics.

---

## 🌐 Live Demo
👉 https://smart-ambulance-routing.onrender.com

---


---

## 🚀 Features

- 🗺️ Real-time route calculation using road networks
- 🚑 Smooth ambulance movement simulation
- 📍 Live GPS tracking (latitude & longitude)
- ⚡ Dynamic speed updates
- 📊 Live traffic analytics (charts)
- 🖱️ Interactive map (click to select locations)

---

## 🧠 How It Works

1. User clicks on the map to select **start** and **destination**
2. System fetches the best route using routing API
3. Ambulance moves along the path using GPS simulation
4. Traffic data updates dynamically on dashboard

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML, CSS, JavaScript
- Leaflet.js (maps)
- Chart.js (analytics)

### APIs
- OpenStreetMap
- OSRM (routing engine)

---

## 📦 Installation (Run Locally)

```bash
git clone https://github.com/vu241fa04262-crypto/smart-ambulance-routing.git
cd smart-ambulance-routing
pip install -r requirements.txt
python app.py
