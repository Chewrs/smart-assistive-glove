# Prototype 2: Distance Detection with MicroPython + Raspberry Pi Logging (WIP)

## 🎯 Goal
Build on Prototype 1 by switching to MicroPython on ESP32, adding logging functionality via Flask on Raspberry Pi, and preparing to use a 3-pin buzzer for audio feedback.

## 🧰 Components Used
- ESP32 (MicroPython)
- HC-SR04 Ultrasonic Sensor
- 3-pin Buzzer (planned)
- Raspberry Pi 400(Flask server for logging)
- Wi-Fi network connection

## ⚙️ How It Works (Current & Planned)
- ✅ ESP32 connects to Wi-Fi on boot
- ✅ Reads distance from HC-SR04 (range: **2 cm – 300 cm**)
- ✅ Sends data via HTTP POST to Flask server on Raspberry Pi
- ✅ Raspberry Pi currently prints received data to console
- ⏳ Improve and clean up ESP32 code structure
- ⏳ Store logs or visualize data on the Raspberry Pi
- ⏳ Add buzzer feedback based on distance

## ✅ Status
- Wi-Fi setup on ESP32 successful  
- Sensor data reliably sent to Flask server  
- Flask server prints data as expected  
- System foundation ready for future improvements  

## ⚠️ Notes
- Flask server currently does not store or analyze data  
- ESP32 code needs refactoring for readability and modularity  
- Buzzer not connected yet; sound feedback logic still pending  