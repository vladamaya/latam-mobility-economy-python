# Proyecto 5: Movilidad urbana y productividad económica en ciudades de LATAM
# TripleTen Data Analyst, Sprint 5: Prepara y estructura datos con Python
# Notebook original: S5 ladb_mobility_economy_project_student.ipynb (aprobado, Iteración 1, revisora Gina Buvoli)
# Código principal transcrito de los Pasos 1 a 7 el 2026-11-12.
# Nota: este .py incluye el código principal de limpieza, filtrado, agregación, unión y exportación.
# No incluye salidas de celdas, celdas Markdown de instrucciones, visualizaciones ni el texto del resumen ejecutivo del notebook.

# importar librerías
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# cargar archivos
traffic = pd.read_csv('/datasets/tomtom_traffic.csv')
eco = pd.read_csv('/datasets/oecd_city_economy.csv')

# mostrar las primeras 5 filas (Nota: agregar .head() a la variable definida y visualizar con print())
print(traffic.head())
print(eco.head())

# Estandarizar los nombres de las columnas de traffic
traffic=traffic.rename(columns={
    'Country':'country',
    'City':'city',
    'UpdateTimeUTC':'update_time_utc',
    'JamsDelay':'jams_delay',
    'TrafficIndexLive':'traffic_index_live',
    'JamsLengthInKms':'jams_length_in_kms',
    'JamsCount':'jams_count',
    'TrafficIndexWeekAgo':'traffic_index_week_ago',
    'UpdateTimeUTCWeekAgo':'update_time_utc_week_ago',
    'TravelTimeLivePer10KmsMins':'travel_time_live_per_10_kms_mins',
    'TravelTimeHistoricPer10KmsMins':'travel_time_historic_per_10_kms_mins',
    'MinsDelay':'mins_delay'})
# verificar cambios
traffic.columns

# Estandarizar los nombres de las columnas de eco
eco=eco.rename(columns={
    'Year':'year',
    'City':'city',
    'Country':'country',
    'City GDP/capita':'city_gdp_per_capita',
    'Unemployment %':'unemployment_pct',
    'PM2.5 (μg/m³)':'pm25',
    'Population (M)':'population_m'})
# verificar cambios
eco.columns

# Convertir las columnas de traffic a tipo fecha con pd.to_datetime()
traffic['update_time_utc'] = pd.to_datetime(traffic['update_time_utc'], errors='coerce')
traffic['update_time_utc_week_ago'] = pd.to_datetime(traffic['update_time_utc_week_ago'], errors='coerce')
# verificar el cambio
traffic.info()

# Limpia separadores y convierte columnas numéricas en eco
# eco['city_gdp_capita'] = ....astype(str).str.replace('.', '').str.replace(',', '.').astype(float)
# eco['unemployment_pct'] = ...
# eco['population_m'] = ...
eco['city_gdp_per_capita']=(
    eco['city_gdp_per_capita']
    .astype(str)
    .str.replace('.','',regex=False)
    .str.replace(',','.',regex=False)
    .astype(float)
)
eco['unemployment_pct']=(
    eco['unemployment_pct']
    .astype(str)
    .str.replace('%','',regex=False)
    .str.replace(',','.',regex=False)
    .astype(float)
)
eco['population_m']=(
    eco['population_m']
    .astype(str)
    .str.replace(',','.',regex=False)
    .astype(float)
)
# Calcula la población total en unidades absolutas (Multiplica * 1000000)
# eco['population'] = ...
eco['population']=eco['population_m']*1000000
# verificar el cambio
eco.info()
eco.head(3)

# Extraer el año de las fechas en update_time_utc
# traffic['year'] = ...
traffic['year']=traffic['update_time_utc'].dt.year
# Verificar cambio
traffic.head(3)

# Filtra los registros del año 2024
# traffic_2024 = traffic[...].copy()
# eco_2024 = ...
traffic_2024=traffic[traffic['year']==2024].copy()
eco_2024=eco[eco['year']==2024].copy()
# Revisar dataframes nuevos
display(traffic_2024.head())
display(eco_2024.head())

# Calcular los  promedios de trafico por ciudad, país y año
traffic_city_year_2024=(traffic_2024.groupby(['city','country','year'])[[
'jams_delay',
'traffic_index_live',
'jams_length_in_kms',
'jams_count',
'mins_delay',
'travel_time_live_per_10_kms_mins',
'travel_time_historic_per_10_kms_mins'
]]
.mean().reset_index())
# Mostrar resultado
traffic_city_year_2024.head()

# Seleccionar columnas clave de tráfico y economía
left_cols = [
    'city',
    'country',
    'year',
    'jams_delay',
    'traffic_index_live',
    'jams_length_in_kms',
    'jams_count',
    'mins_delay',
    'travel_time_live_per_10_kms_mins',
    'travel_time_historic_per_10_kms_mins'
]
right_cols=[
    'year',
    'city',
    'city_gdp_per_capita',
    'unemployment_pct',
    'pm25',
    'population'
]
# Usar .copy() para crear los dos nuevos datasets reducidos
# traffic_2024_small = traffic_city_year_2024[ ... ].copy()
# eco_2024_small = ...
traffic_2024_small=traffic_city_year_2024[left_cols].copy()
eco_2024_small=eco_2024[right_cols].copy()
# Unir datasets
merged=pd.merge(
traffic_2024_small,eco_2024_small,on=['city','year'],how='inner'
)
# Mostrar las primeras 5 filas
merged.head()

# Exporta el dataset final como CSV
merged.to_csv("ladb_mobility_economy_2024_clean.csv",index=False)
