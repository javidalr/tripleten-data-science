# Análisis de Videojuegos - Proyecto 06

## Descripción del proyecto

Primer proyecto integrado de Tripleten, abarca varias habilidades enseñadas durante la primera parte del plan de estudios, incluyendo Python básico, preprocesamiento de datos, análisis exploratorio de datos y análisis estadístico de datos.

La tienda en línea "Ice", especializada en la venta de videojuegos a nivel mundial, proporcionaron los datos provenientes de fuentes abiertas. Estos datos incluyen reseñas de expertos y usuarios, géneros, plataformas de juegos e información histórica de ventas. Nuestro objetivo principal es identificar patrones que contribuyen al éxito de un videojuego, permitiéndonos detectar juegos con alto potencial y planificar campañas publicitarias efectivas.

El conjunto de datos corresponde al año 2016, y asumimos un escenario donde actualmente es diciembre de 2016, y se nos ha encargado planificar una campaña para el año siguiente, 2017.

Es importante destacar que este conjunto de datos contiene abreviaciones, entre ellas ESRB, que corresponde a Entertainment Software Rating Board. La ESRB es una organización reguladora independiente encargada de evaluar el contenido de los juegos y asignar calificaciones por edad como Teen o Mature.

## Descripción de los datos

Analizaremos los datos almacenados en el archivo games.csv. Aunque tenemos información preliminar sobre los datos, es necesario evaluar su calidad.

A continuación se describen las variables del conjunto de datos:

Name: Nombre del videojuego

Platform: Plataforma(s) en las que está disponible el juego

Year_of_Release: Año de lanzamiento del juego

Genre: Género o categoría del juego

NA_sales: Ventas en América del Norte, en millones de USD

EU_sales: Ventas en Europa, en millones de USD

JP_sales: Ventas en Japón, en millones de USD

Other_sales: Ventas en otros países, en millones de USD

Critic_Score: Calificación dada por los críticos, con un máximo de 100

User_Score: Calificación dada por los usuarios, con un máximo de 10

Rating: Clasificación asignada por la ESRB

Estas variables proporcionan información importante sobre los juegos, incluyendo su desempeño en ventas, evaluaciones por parte de críticos y usuarios, y clasificaciones por edad.

Significado de las clasificaciones ESRB (según su sitio web):

- E (Everyone): Contenido apto para todas las edades

- T (Teen): Contenido apto para mayores de 13 años

- M (Mature): Contenido apto para mayores de 17 años

- E10+ (Everyone 10 and older): Contenido apto para mayores de 10 años

- K-A (Kids to Adults): Contenido apto para todas las edades (clasificación usada antes de 1999, reemplazada por "E")

- AO (Adults Only): Contenido solo apto para mayores de 18 años

- EC (Early Childhood): Contenido apto para niños mayores de 3 años

- RP (Rating Pending): Clasificación aún no asignada por la ESRB

## Hipótesis

La calificación promedio de los usuarios para las plataformas Xbox One y PC es la misma.

Las calificaciones promedio de los usuarios para los géneros Acción y Deportes son diferentes.

## Librerías

- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
