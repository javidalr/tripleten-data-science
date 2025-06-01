# Análisis de Precios de Vehículos

## Resumen del Proyecto

El propósito es analizar los factores que influyen en el precio de venta de autos en el mercado de vehículos usados. Se proporcionó un conjunto de datos que contiene decenas de miles de anuncios de vehículos del sitio web **Crankshaft List**.

## Descripción de los Datos

Utilizaremos el conjunto de datos `vehicles_us.csv`, que contiene las siguientes columnas:

- `price`: precio de venta del vehículo  
- `model_year`: año de fabricación del vehículo  
- `model`: tipo de vehículo  
- `condition`: condición del vehículo  
- `cylinders`: tipo o número de cilindros del vehículo  
- `fuel`: tipo de combustible utilizado (ej. gasolina, diésel)  
- `odometer`: kilometraje del vehículo al momento del anuncio  
- `transmission`: tipo de transmisión del vehículo  
- `paint_color`: color del vehículo  
- `is_4wd`: valor booleano que indica si el vehículo tiene tracción en las cuatro ruedas  
- `date_posted`: fecha en que se publicó el anuncio  
- `days_listed`: duración en días que el anuncio estuvo activo antes de ser eliminado  

## Etapas

El proyecto se divide en tres etapas principales:

### Etapa 1: Preprocesamiento de Datos

En esta fase, el enfoque es mejorar la calidad de los datos, abordando valores faltantes, ajustando tipos de datos y creando columnas relevantes.

### Etapa 2: Análisis Exploratorio de Datos

Parte central del proyecto, en la cual, se analiza el conjunto de datos para obtener conclusiones y resolver las tareas planteadas. Se examinan parámetros claves, se tratan valores atípicos, se realizan visualizaciones y se interpretan los resultados.

### Etapa 3: Conclusiones

Presentación de conclusiones generales del análisis, junto con recomendaciones sobre los factores que deben considerarse con mayor atención al determinar el precio de venta de un vehículo usado.

## Librerías

- Pandas  
- Os
- Plotly
- Streamlit

Por ultimo, se adjunta link de la aplicación en Render.

Link de proyecto en Render: https://tripleten-data-science.onrender.com/