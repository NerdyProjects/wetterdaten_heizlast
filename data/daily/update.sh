rm -rf recent
mkdir recent
cd recent
wget -r -l1 -nd https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/recent/
for I in *; do unzip "$I"; done
cd ..
rm -rf historical
mkdir historical
cd historical
wget -r -l1 -nd https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/
for I in *; do unzip "$I"; done
cd ..
