#include <Wire.h>
#include <U8g2lib.h>

#define TRIG_PIN 14  // D5 = GPIO14
#define ECHO_PIN 12  // D6 = GPIO12
#define BUZZER_PIN 13  // D7 (GPIO13)

// U8g2 for SH1106 using hardware I2C
U8G2_SH1106_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, U8X8_PIN_NONE);

void setup() {
  Serial.begin(9600);
  Wire.begin(4, 5);  // SDA = GPIO4 (D2), SCL = GPIO5 (D1)

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  u8g2.begin();
}

void loop() {
  // Send ultrasonic pulse
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH);
  float distance_cm = duration * 0.0343 / 2;

  Serial.print("Distance: ");
  Serial.print(distance_cm);
  Serial.println(" cm");

if (distance_cm > 500 || duration == 0) {
  noTone(BUZZER_PIN);  // silence = nothing nearby
} else if (distance_cm < 10) {
  tone(BUZZER_PIN, 1000);  // very close = very high
} else if (distance_cm < 30) {
  tone(BUZZER_PIN, 800);
} else if (distance_cm < 60) {
  tone(BUZZER_PIN, 400);
} else if (distance_cm < 100) {
  tone(BUZZER_PIN, 300);
} else if (distance_cm < 200) {
  tone(BUZZER_PIN, 200);
} else {
  tone(BUZZER_PIN, 100);  // far = low tone
}
  u8g2.clearBuffer();
  
  if (distance_cm > 500 || duration == 0) {
    u8g2.setDrawColor(1);
    u8g2.setFont(u8g2_font_ncenB08_tr);
    u8g2.drawStr(30, 30, "Out of");
    u8g2.drawStr(30, 50, "Range");
  } else if (distance_cm < 100) {
    // Invert background
    u8g2.setDrawColor(1);
    u8g2.drawBox(0, 0, 128, 64);
    u8g2.setDrawColor(0);  // black text on white
    u8g2.setFont(u8g2_font_ncenB08_tr);
    char dist[10];
    sprintf(dist, "%.1f cm", distance_cm);
    u8g2.drawStr(20, 40, dist);
  } else {
    u8g2.setDrawColor(1);
    u8g2.setFont(u8g2_font_ncenB08_tr);
    char dist[10];
    sprintf(dist, "%.1f cm", distance_cm);
    u8g2.drawStr(20, 40, dist);
  }

  u8g2.sendBuffer();
  delay(100);
}