 
# Prototype 1: Distance Detection with Buzzer Feedback

## 🎯 Goal
Create a basic glove prototype that detects distance and provides audio feedback using a buzzer with varying pitch.

## 🧰 Components Used
- ESP8266
- HC-SR04 Ultrasonic Sensor
- Buzzer 

## ⚙️ How It Works
- Measures distance from obstacles (range: **2 cm – 300 cm**)
- Buzzer pitch varies based on the measured distance:
  - Closer = higher pitch
  - Farther = lower pitch

## ✅ Status
- Distance detection working correctly  
- Buzzer pitch changes as expected  
- System responds smoothly within the defined range  

## ⚠️ Notes
- The sound feedback works but can be **overwhelming or tiring** over time  
- May need to consider vibration feedback or volume control in future versions