#include <Arduino.h>

const int AvoidPin = 7; // Pin utilisé pour le détecteur de proximité
const int flameSensorPin = 12; // Pin utilisé pour le détecteur de flamme (analogique)
const int soundSensorPin = A1; // Pin utilisé pour le détecteur de son (analogique)
const int buzzerPin = 13;
const int ledGreen = 2;
const int ledRED = 8;
const int flameRedLED = 4; // LED associée à la détection de flamme (rouge)
const int flameGreenLED = 11; // LED associée à la détection de flamme (vert)
const int redLED = 10; // Pin de la LED rouge de la LED bicolore
const int greenLED = 9; // Pin de la LED verte de la LED bicolore

void setup() {
  pinMode(AvoidPin, INPUT); // Utilisation du pin pour le détecteur de proximité
  pinMode(flameSensorPin, INPUT); // Utilisation du pin pour le détecteur de flamme
  pinMode(soundSensorPin, INPUT); // Utilisation du pin pour le détecteur de son
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledRED, OUTPUT);
  pinMode(flameRedLED, OUTPUT); // Déclaration de la LED associée à la détection de flamme (rouge)
  pinMode(flameGreenLED, OUTPUT); // Déclaration de la LED associée à la détection de flamme (vert)
  pinMode(redLED, OUTPUT); // Déclaration de la LED rouge de la LED bicolore
  pinMode(greenLED, OUTPUT); // Déclaration de la LED verte de la LED bicolore
  Serial.begin(9600);
}

void loop() {
  int avoidState = digitalRead(AvoidPin);
  int flameValue = digitalRead(flameSensorPin);
  int soundValue = analogRead(soundSensorPin); // Lire la valeur du capteur de son

  if (avoidState == LOW) {
    digitalWrite(buzzerPin, HIGH);
    digitalWrite(ledGreen, HIGH);
    digitalWrite(ledRED, LOW);
    Serial.println("Obstacle détecté !");
  } else if (flameValue == LOW) {
    digitalWrite(buzzerPin, LOW); // Activer le buzzer si une flamme est détectée
    digitalWrite(ledGreen, LOW);
    digitalWrite(ledRED, HIGH);
    Serial.println("Flamme détectée !");
  } else {
    digitalWrite(ledGreen, LOW);
    digitalWrite(ledRED, HIGH);
    digitalWrite(buzzerPin, HIGH);
  }

  // Si une flamme est détectée
  if (flameValue == LOW) { // Adaptez la valeur seuil en fonction de votre capteur
    digitalWrite(flameRedLED, LOW); // La LED associée à la détection de flamme (rouge) s'éteint
    digitalWrite(flameGreenLED, HIGH); // La LED associée à la détection de flamme (vert) s'éteint
  } else {
    digitalWrite(flameRedLED, HIGH); // La LED associée à la détection de flamme (rouge) s'allume
    digitalWrite(flameGreenLED, LOW);
 // La LED associée à la détection de flamme (vert) s'allume
  }

  // Si un son est détecté
  if (soundValue > 500) {
    digitalWrite(redLED, LOW); // Éteint la LED rouge
    digitalWrite(greenLED, HIGH); // Adaptez la valeur seuil selon votre capteur de son

  } else {
    digitalWrite(redLED, HIGH); // Allume la LED rouge
    digitalWrite(greenLED, LOW); // Allume la LED verte
  }

  delay(500);
}