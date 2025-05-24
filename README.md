## Introducción

La Film Junky Union, una nueva comunidad innovadora para entusiastas del cine clásico, está desarrollando un sistema para filtrar y categorizar reseñas de películas con el fin de detectar opiniones negativas.

## Objetivo

- Construir un modelo para clasificar reseñas como positivas o negativas utilizando un conjunto de datos de reseñas de películas de IMDb etiquetadas por polaridad. El modelo debe alcanzar una puntuación F1 de al menos 0.85.

## Datos

Descripción de los datos

tconst: Identificador único para cada película en la base de datos de IMDb.

title_type: Tipo o categoría del título (por ejemplo, película).

primary_title: Título principal de la película.

original_title: Título original de la película (en su idioma original).

start_year: Año en que se estrenó o comenzó la película.

end_year: Año en que finalizó la película (si aplica).

runtime_minutes: Duración de la película en minutos.

is_adult: Indicador binario (1 o 0) que señala si la película está clasificada como “para adultos”.

genres: Géneros asociados a la película.

average_rating: Calificación promedio otorgada a la película.

votes: Número de votos que ha recibido la película.

rating: Calificación otorgada en la reseña.

sp: Polaridad del sentimiento (positivo, neutral).

ds_part: Parte del conjunto de datos (entrenamiento o prueba).

idx: Identificador del punto de datos en el conjunto.

## Características

review: Texto de la reseña de la película.

## Variable objetivo

pos: Indicador binario (1 o 0) que señala la polaridad del sentimiento de la reseña.

## Principales bibliotecas utilizadas

Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn, LightGBM, Tensorflow, PyTorch, Optuna, NLTK, SpaCy, Transformers