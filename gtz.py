import pandas as pd
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--station_id', default='02444')
parser.add_argument('-f', '--first', type=int, default=20020000)
parser.add_argument('-l', '--last', type=int, default=20221231)
parser.add_argument('-hl', '--heating_limit', type=int, default=15)
parser.add_argument('-ti', '--temperature_inside', type=int, default=20)
parser.add_argument('-td', '--design_temperature', type=float, default=-13)

args=parser.parse_args()

heating_limit_temperature = args.heating_limit
station_id = args.station_id
first=args.first
last=args.last
ti = args.temperature_inside
design_temperature = args.design_temperature

print(args)

historical = next(pd.read_csv(file, sep=';', skipinitialspace=True) for file in glob.glob(r'data/daily/historical/produkt_klima_*' + station_id + '.txt'))
recent = next(pd.read_csv(file, sep=';', skipinitialspace=True) for file in glob.glob(r'data/daily/recent/produkt_klima_*' + station_id + '.txt'))

df = pd.concat([historical, recent[recent['MESS_DATUM'].isin(historical['MESS_DATUM']) == False]])

working_set = df.query("MESS_DATUM <= @last and MESS_DATUM >= @first")
na_val = working_set.query('TMK == -999')
if not na_val.empty:
    print("Missing data for: ", na_val)

heating_days = working_set.query("TMK < @heating_limit_temperature")
print("Station: ", station_id)
print("average temperature: ", working_set['TMK'].mean())
print("heating limit: ", heating_limit_temperature)
print("average temperature on heating days: ", heating_days['TMK'].mean())
print("coldest average temperature: ", heating_days['TMK'].min())

print("1% percentile temperature: ", heating_days['TMK'].quantile(0.01))
print("5% percentile temperature: ", heating_days['TMK'].quantile(0.05))
print("30% percentile temperature: ", heating_days['TMK'].quantile(0.3))
print("Days: ", working_set['MESS_DATUM'].count())
print("Heating days :", heating_days['MESS_DATUM'].count())

print("VDI2067 Gradtagzahl: ", sum(ti - heating_days['TMK']))
print("VDI3807 Heizgradtage: ", sum(heating_limit_temperature - heating_days['TMK']))
print("Vollbenutzungsstunden, DIN/TS 12831-1:2020-04: ", (sum(heating_limit_temperature - heating_days['TMK']) * 24) / (heating_limit_temperature - design_temperature))
print("Vollbenutzungsstunden pro Jahr, DIN/TS 12831-1:2020-04: ", (sum(heating_limit_temperature - heating_days['TMK']) * 24) / (heating_limit_temperature - design_temperature) / working_set['MESS_DATUM'].count() * 365)
