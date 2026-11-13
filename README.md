# Movilidad urbana y productividad económica en ciudades de LATAM con Python

Proyecto de portafolio — TripleTen Data Analyst, Sprint 5: Prepara y estructura datos con Python (Proyecto 5).

## En simple

Tomé dos tablas sucias: una de tráfico en ciudades (TomTom) y otra de economía de ciudades (OECD). Las limpié con Python, me quedé solo con 2024, promedié el tráfico por ciudad y uní ambas tablas para poder comparar tráfico con economía (PIB por habitante, desempleo, contaminación y población).

## Qué hice

- Cargué `tomtom_traffic.csv` y `oecd_city_economy.csv` con pandas
- Estandaricé nombres de columnas (a snake_case)
- Convertí fechas y limpié números con formato europeo (puntos y comas)
- Extraje el año y filtré solo 2024
- Promedié las métricas de tráfico por ciudad, país y año
- Uní tráfico y economía con un INNER JOIN por ciudad y año
- Exporté el dataset final: `ladb_mobility_economy_2024_clean.csv`

## Herramientas

- Python, pandas, numpy
- seaborn y matplotlib (visualizaciones en el notebook original)

## Resultado

El dataset final aprobado contiene **15 ciudades, 14 columnas y 7 países** (según la revisión del proyecto).

## Código principal

Ver [`proyecto5_limpieza_y_union.py`](./proyecto5_limpieza_y_union.py) — código principal de los Pasos 1 a 7 del notebook aprobado `S5 ladb_mobility_economy_project_student.ipynb` (Iteración 1).

Nota: este repositorio incluye el código principal transcrito; no incluye las salidas de celdas, las visualizaciones ni el texto del resumen ejecutivo del notebook original, y los datos crudos del curso no se redistribuyen.

## Cómo correrlo

```bash
pip install -r requirements.txt
python proyecto5_limpieza_y_union.py
```

Coloca los archivos de entrada en una carpeta `datasets/` junto al script: `tomtom_traffic.csv` y `oecd_city_economy.csv` (son datos del entorno de práctica de TripleTen y no se redistribuyen). El script genera `ladb_mobility_economy_2024_clean.csv`.

## Autor

Vlad — Analista de datos en formación (TripleTen).
