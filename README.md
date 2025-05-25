# Instacar: Plataforma de entregas

## Descripción del proyecto

Instacart es una plataforma de entregas de comestibles donde la clientela puede registrar un pedido y hacer que se lo entreguen, similar a Uber Eats y Door Dash. El conjunto de datos que te hemos proporcionado tiene modificaciones del original. Se redujo el tamaño del conjunto para que los cálculos se realicen más rápido y se introducen valores ausentes y duplicados. Se considero, con cuidado de conservar las distribuciones de los datos originales al momento de las modificaciones.

## Descripción de los datos

Se proporcionan 5 conjuntos de datos, las cuales seran usadas para el preprocesamiento de datos y el análisis exploratorio de datos. A continuación se muestran las columnas de cada tabla y describe los datos que contienen.

### instacart_orders.csv

Cada fila corresponde a un pedido en la aplicación Instacart.

'order_id': número de ID que identifica de manera única cada pedido.
'user_id': número de ID que identifica de manera única la cuenta de cada cliente.
'order_number': el número de veces que este cliente ha hecho un pedido.
'order_dow': día de la semana en que se hizo el pedido (0 si es domingo).
'order_hour_of_day': hora del día en que se hizo el pedido.
'days_since_prior_order': número de días transcurridos desde que este cliente hizo su pedido anterior.

### products.csv

Cada fila corresponde a un producto único que pueden comprar los clientes.

'product_id': número ID que identifica de manera única cada producto.
'product_name': nombre del producto.
'aisle_id': número ID que identifica de manera única cada categoría de pasillo de víveres.
'department_id': número ID que identifica de manera única cada departamento de víveres.

### order_products.csv

Cada fila corresponde a un artículo pedido en un pedido.

'order_id': número de ID que identifica de manera única cada pedido.
'product_id': número ID que identifica de manera única cada producto.
'add_to_cart_order': el orden secuencial en el que se añadió cada artículo en el carrito.
'reordered': 0 si el cliente nunca ha pedido este producto antes, 1 si lo ha pedido.

### aisles.csv

'aisle_id': número ID que identifica de manera única cada categoría de pasillo de víveres.
'aisle': nombre del pasillo.

### departments.csv

'department_id': número ID que identifica de manera única cada departamento de víveres.
'department': nombre del departamento.

## Hipótesis

Se asignaron a evaluacion las sihguientes hipótesis:

- Dias y horarios de más compras
- Frecuencia de pedidos
- Categorías y productos más populares
- Demanda de productos

## Librerías
- Pandas
- Matplotlib