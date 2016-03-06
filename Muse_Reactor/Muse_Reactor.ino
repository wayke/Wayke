#include <Wire.h>
#include <rgb_lcd.h>

int soundPin = 6;
int ledPin = 5;
int touchPin = 2;

rgb_lcd lcd;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(touchPin, INPUT);
  pinMode(soundPin, OUTPUT);
  
  lcd.begin(16, 2);
  modeNormal();
  
}

// the loop function runs over and over again forever
void loop() {
  if (digitalRead(touchPin) == 1){ 
    modeTired();
    digitalWrite(ledPin, HIGH);
    digitalWrite(soundPin, HIGH);  
    delay(200);       
    digitalWrite(soundPin, LOW);      
    delay(2500);
    digitalWrite(ledPin, LOW);
    modeNormal();
  }
}

void modeNormal(){
  lcd.clear(); 
  lcd.setRGB(252, 189, 13);
  lcd.print("Mode: Normal");
  lcd.setCursor(0, 0);
}

void modeTired(){
    lcd.clear();
    lcd.setRGB(255, 0, 0); 
    lcd.print("Take a break,");
    lcd.setCursor(0, 1);  
    lcd.print("you seem tired"); 
}
