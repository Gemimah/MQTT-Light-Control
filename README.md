# MQTT-Light-Control
🚀 MQTT Light Control# MQTT Light Control

## 📌 Project Overview
MQTT Light Control is a web-based project that allows users to control a light using MQTT (Message Queuing Telemetry Transport). It provides an intuitive UI where users can toggle the light ON or OFF, with a glowing lamp animation to indicate the light's status.

## 💡 Features
- Real-time light control using MQTT.
- Interactive UI with a glowing lightbulb effect when ON.
- Responsive design built with Bootstrap.
- Supports WebSockets for seamless communication.
- Works with public MQTT brokers like HiveMQ.

## 🚀 Technologies Used
- HTML, CSS, Bootstrap
- JavaScript (MQTT.js)
- MQTT Protocol (HiveMQ Broker)

## 📦 Setup Instructions
1. Clone the repository:
2. Open the `index.html` file in a web browser.
3. Click the buttons to turn the light ON and OFF.

## 🔧 How It Works
- The frontend connects to an MQTT broker (`wss://broker.hivemq.com:8000/mqtt`).
- When the "Turn ON" button is clicked, an "ON" message is published to the MQTT topic.
- When the "Turn OFF" button is clicked, an "OFF" message is published.
- The lamp icon visually reflects the current state.

## 🌍 Live Demo
[Optional: Add a link to a live demo if hosted online]

## 🛠 Future Enhancements
- Add support for multiple devices.
- Implement a real-time status update from the MQTT broker.
- Improve UI with animations.

## 📜 License
This project is open-source and free to use.

---
Enjoy using MQTT Light Control! 🚀💡

