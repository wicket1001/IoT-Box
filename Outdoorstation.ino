#include <Adafruit_Si7021.h>
#include <Adafruit_MPL115A2.h>
#include "SimpleBLE.h"

#define powerConversionFactor 0.0009
#define powerPin 4
#define powerOutSleepTime 99999999999999

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

SimpleBLE ble;

Adafruit_MPL115A2 pressureSensor;
Adafruit_Si7021 humiditySensor = Adafruit_Si7021();
boolean pressureOkay = false;
boolean humidityOkay = false;
RTC_DATA_ATTR unsigned long intervall = 9000000; //Messintervall in Millisekunden, standardmäßig 15 min = 900000ms
unsigned long upTime = 120000;
boolean powered = false; //wenn das System nicht im Akkubetrieb läuft, geht es nicht in sleep, somit kann es auch requests erfüllen, bei Akkubetrieb = false
int startTime;


void setup() {
  if(getBatteryLevel() < 3.65){
    esp_sleep_enable_timer_wakeup(powerOutSleepTime);
    esp_deep_sleep_start();
  }
  startTime = millis();
  Serial.begin(9600);
  delay(1000);
  Serial.println("Initiating Sensors");
  // put your setup code here, to run once:
  pressureSensor.begin();
  pressureOkay = true;
  if(!humiditySensor.begin()){
    Serial.println("Humidity-sensor failure");
  }
  else{
    humidityOkay = true;
    Serial.println("Successfully initiated humidity-sensor");
  }
  Serial.println("Initiated sensors, start with communications");
  
  

}

void loop() {
  transmit();
  long nextSleep = intervall - (millis() - startTime);
  if(nextSleep > 1000){
    esp_sleep_enable_timer_wakeup(nextSleep);
    esp_deep_sleep_start();
  }
  delay(nextSleep);

}

void transmit(){
  String message = "T"+String(getTemperature())+"P"+String(getPressure())+"H"+String(getHumidity())+"B"+String(getBatteryLevel());
  ble.begin(message);
  delay(upTime);

}

float getPressure(){
  if(pressureOkay){
    return pressureSensor.getPressure();
  }
  else{
    return 0;
  }
  
}

float getHumidity(){
  if(humidityOkay){
    return humiditySensor.readHumidity();
  }
  else{
    return 0;
  }
  
  
}

float getTemperature(){
  return humiditySensor.readTemperature();

}

double getBatteryLevel(){
  return analogRead(powerPin)*powerConversionFactor*2;
  
}

void handleRequest(String input){
  input.toUpperCase();
  if(input.indexOf("S") != -1){
    
  }
  else if (input.indexOf("R") != -1){
    if(input == "RB"){
      //send battery level
    }
    else if(input == "RT"){
      //send temperature
    }
    else if(input == "RH"){
      //send humidity
    }
    else if(input == "RP"){
      //send pressure
    }
    else if(input == "RI"){
      //send intervall
    }
    
  }
}



