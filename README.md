## Wetterdaten - Heizlast Tool

Dieses tool ermöglicht den Download von historischen Wetterdaten vom deutschen Wetterdienst (DWD) und die Auswertung für Heizlast-relevante Daten wie
* Gradtagzahlen
* Vollbenutzungsstunden

Es ist work-in-progress. Keine Garantie auf Berechnungsergebnisse!

### Benutzung
Im Ordner `daily` findet sich ein `update.sh`: Hiermit kannst du die Wetterdaten (historisch & aktueller) vom DWD herunterladen. Führe das Skript im Ordner daily aus. Achtung: Es ist recht billig und prüft keine Pfade etc.

Die Wetterdaten belegen etwa 3GB Speicherplatz.

Sind diese heruntergeladen, so kannst du mit `python gtz.py` die Auswertung für einen beliebigen Zeitraum und eine beliebige Wetterstation durchführen.

```
usage: gtz.py [-h] [-s STATION_ID] [-f FIRST] [-l LAST] [-hl HEATING_LIMIT] [-ti TEMPERATURE_INSIDE] [-td DESIGN_TEMPERATURE]

options:
  -h, --help            show this help message and exit
  -s STATION_ID, --station_id STATION_ID
  -f FIRST, --first FIRST
  -l LAST, --last LAST
  -hl HEATING_LIMIT, --heating_limit HEATING_LIMIT
  -ti TEMPERATURE_INSIDE, --temperature_inside TEMPERATURE_INSIDE
  -td DESIGN_TEMPERATURE, --design_temperature DESIGN_TEMPERATURE


python gtz.py
Namespace(station_id='02444', first=20020000, last=20221231, heating_limit=15, temperature_inside=20, design_temperature=-13)
Station:  02444
average temperature:  10.573246414602345
heating limit:  15
average temperature on heating days:  6.487577160493828
coldest average temperature:  -16.1
1% percentile temperature:  -8.0
5% percentile temperature:  -3.1
30% percentile temperature:  3.7
Days:  7670
Heating days : 5184
VDI2067 Gradtagzahl:  70048.40000000001
VDI3807 Heizgradtage:  44128.39999999999
Vollbenutzungsstunden, DIN/TS 12831-1:2020-04:  37824.342857142845
Vollbenutzungsstunden pro Jahr, DIN/TS 12831-1:2020-04:  1799.9850251443465
```
