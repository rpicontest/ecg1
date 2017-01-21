# ecg1

## ECG System #1

Hauptsensoren: 
=======================
- Trittmatte
- Taster
- Bluetooth

Dokumentation:
=======================
- https://www.sunfounder.com/learn/category/Sensor-Kit-v1-0-for-Raspberry-Pi.html


Anleitung:
=======================
1. Skript 0_init.sh ausführen

2. Konfiguration des Systems
   - "sudo raspi-config" starten
   - deutsche Lokalisierung (4.I1=>de_DE.UTF-8 UTF-8 (per Space auswählen, Return zum bestätigen); Default=>de_DE.UTF-8)
   - deutsches Tastaturlayout (4.I3=>Other=>German=>German)
   - SSH aktivieren (5.P2=>yes)
   - VNC aktivieren (5.P3=>yes)
   - SPI Interface aktivieren (5.P4=>yes)
   - 1-wire aktivieren (5.P7=>yes)
   - Hostname konfigurieren (7.A2=>je nach Aufschrift "ecg1", "ecg2", "ecg3")
   - Reboot durchführen

# MERKER
ab sofort ist der Raspberry unter "ssh -p 22 pi@ecg1" im lokalen Netzwerk erreichbar (hierfür idealerweise DHCP im Router aktivieren und den Raspebrry per Netzwerkkabel anschließen)
