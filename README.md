# Análisis de Videojuegos

## Resumen del Proyecto

Este es un proyecto integrado del curso de Tripleten, y abarca diversas habilidades enseñadas durante la primera parte del programa, incluyendo Python básico, preprocesamiento de datos, análisis exploratorio y análisis estadístico.

La tienda en línea **"Ice"**, especializada en la venta de videojuegos a nivel mundial, proporcionó datos de fuentes abiertas que incluyen reseñas de expertos y usuarios, géneros, plataformas de los juegos e información histórica de ventas. El principal objetivo es identificar patrones que contribuyen al éxito de un videojuego para así detectar títulos con alto potencial y planificar campañas publicitarias efectivas.

El conjunto de datos se enfoca en el año **2016**, y asumimos que estamos en diciembre de ese año, por lo que el análisis busca preparar una estrategia de campaña para **2017**.

Es importante señalar que este conjunto de datos contiene abreviaturas como **ESRB**, que corresponde a la *Entertainment Software Rating Board*, una organización reguladora que clasifica los videojuegos por edad (como Teen o Mature).

### Objetivos del proyecto:

1. Analizar patrones que contribuyen al éxito o fracaso de un videojuego.  
2. Proporcionar recomendaciones sobre juegos con potencial para campañas de publicidad en 2017.  
3. Probar dos hipótesis:
   - Si las calificaciones promedio de los usuarios para Xbox One y PC son iguales.
   - Si las calificaciones promedio de los usuarios para los géneros Acción y Deportes son diferentes.

## Descripción de los Datos

Se analizaran los datos almacenados en el archivo `games.csv`. Aunque se tiene información preliminar, es necesario evaluar la calidad de los datos.

**Descripción de las columnas:**

- `Name`: Nombre del videojuego  
- `Platform`: Plataforma(s) en las que está disponible  
- `Year_of_Release`: Año de lanzamiento  
- `Genre`: Género o categoría  
- `NA_sales`: Ventas en Norteamérica (millones USD)  
- `EU_sales`: Ventas en Europa (millones USD)  
- `JP_sales`: Ventas en Japón (millones USD)  
- `Other_sales`: Ventas en otros países (millones USD)  
- `Critic_Score`: Puntuación de los críticos (máx. 100)  
- `User_Score`: Puntuación de los usuarios (máx. 10)  
- `Rating`: Clasificación ESRB asignada  

**Significado de las clasificaciones ESRB:**

- **E** (*Everyone*): Contenido apto para todas las edades  
- **T** (*Teen*): Apto para mayores de 13 años  
- **M** (*Mature*): Apto para mayores de 17 años  
- **E10+** (*Everyone 10 and older*): Apto para mayores de 10 años  
- **K-A** (*Kids to Adults*): Apto para todas las edades (usado antes de 1999)  
- **AO** (*Adults Only*): Solo para mayores de 18 años  
- **EC** (*Early Childhood*): Apto para niños de 3 años en adelante  
- **RP** (*Rating Pending*): Clasificación pendiente por ESRB

## Hipótesis

Se asignaron dos hipótesis para analizar:

- La calificación promedio de los usuarios para las plataformas Xbox One y PC es la misma.  
- Las calificaciones promedio de los usuarios para los géneros Acción y Deportes son diferentes.

## Etapas

El análisis se desarrollará en las siguientes fases:

1. **Descripción Inicial de los Datos**: Vista general del conjunto de datos y estadísticas básicas.  
2. **Preprocesamiento de Datos**: Mejora de la calidad de los datos, incluyendo lectura, validación, renombrado de columnas, manejo de valores nulos, ajuste de tipos de datos y creación de columnas relevantes.  
3. **Análisis Exploratorio de Datos**: Búsqueda de patrones y análisis de desempeño en ventas. Se presentarán recomendaciones basadas en estos hallazgos.  
4. **Análisis Estadístico de Datos**: Ejecución de pruebas estadísticas para validar las hipótesis planteadas.  
5. **Conclusiones**: Resumen de los resultados obtenidos y conclusiones generales del proyecto.

Estas etapas permitirán llevar a cabo un análisis completo del conjunto de datos y extraer conclusiones útiles sobre el desempeño de ventas de videojuegos.

## Librerías

- Pandas  
- NumPy
- Matplotlib  
- Seaborn  
- SciPy