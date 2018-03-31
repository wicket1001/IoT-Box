# IoT-Box

Das ist die Steuerung des Indoor- und Outdoormoduls der IoT-Box für den Wettbewerb 3-IoT-Stars 2018. 

## Getting Started

Die Outstation kommuniziert mit der Indoorstation, die dann die Daten auf den 3-Server pusht.

### Voraussetzungen

Die Indoorstation bedarf einem Raspberry Pi und die Outdoorstation eines ESPs.

### Installation

Auf dem Raspberry muss man den Code mittels dem Befehl der unten angeführt ist starten:
```
sudo python ReadSensors.py
```

Den Code der Outdoorstation "Outdoorstation.ino" muss man mittels der Arduino IDE ausführen.

## Autoren

* **Harald Moritz** - *Hauptentwickler* - [Github](https://github.com/wicket1001)
* **Valentin Benke** - *Outdoorstationsentwicklung* - [Github](https://github.com/Vabe7)
* **Sophie Tomitsch** - *Freundliche Unterstützung* - [Github](https://github.com/SopTom)
