import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import io
warnings.filterwarnings("ignore")


st.title("Análisis de Precios de Vehículos")

st.markdown('''
En esta presentación se analizara el conjunto de datos de Crankshaft List, el cual contiene características de vehiculos que pueden influir en su precio de venta, para ello se revisara el dataset para entender la información recolectada, para posteriormente realizar un análisis exploratorio de datos (EDA), y asi explicar que variables contribuyen al precio final de venta.    
''')

# Información Preliminar ============================================================================================

st.header("1 Información Preliminar")

st.subheader("1.1 Carga y Exploración de Datos")
if 'data' not in st.session_state:
    st.session_state.data = pd.read_csv('vehicles_us.csv')
data = st.session_state.data

st.subheader('1.2 Muestra del conjunto de datos')
st.dataframe(data.head(5), use_container_width=True)


st.subheader("1.3 Descripcion general")
buffer = io.StringIO()
data.info(buf=buffer)
info_str = buffer.getvalue()
st.code(info_str)

st.subheader("1.4 Tamaño del Dataset")
st.write(f'El dataset contiene {data.shape[0]} registros y {data.shape[1]} variables')

st.subheader("1.5 Descripción Estadística")
st.write(data.describe())

st.markdown('''
**Hallazgos:**

- El conjunto de datos se compone de 51.525 registros y 13 variables, de las cuales, 5 columnas contienen valores nulos.

- Las columnas model_year, cylinders y odometer son actualmente de tipo de dato flotante, pero deberían ser enteros.

- La columna date_posted contiene datos de fecha, pero actualmente está almacenada como una cadena de texto.

- La columna is_4wd debería ser de tipo booleano, donde el valor 1 representa un vehículo con tracción en las cuatro ruedas, mientras que el 0 representa un vehículo sin tracción 4x4. Parece que el número 0 está representado por valores NaN, lo que resulta en el menor número de entradas no nulas en esta columna.

- Existe una diferencia notable entre los valores promedio y mediana en las columnas price y days_listed, lo cual indica la posible presencia de valores atípicos.

- Los valores más bajos en las columnas odometer y days_listed son 0. Un valor de 0 en odometer podría indicar un vehículo nuevo, mientras que un 0 en days_listed parece inusual.

- Algunas columnas tienen una cantidad significativa de valores únicos, lo cual puede ser útil para categorizar los datos.

En general, los datos parecen ser suficientes, pero requieren limpieza. En el siguiente paso, se realizará la limpieza de los datos, lo que implica abordar los valores faltantes y cambiar los tipos de datos según la información anteriormente detallada.
''')

# Preprocesamiento de datos ==========================================================================================

st.header('2 Preprocesamiento de datos')

st.subheader("2.1. Tramiento de Valores Ausentes")
st.write('Valores ausentes por columna',data.isna().sum())

st.markdown('''
Cada columna con valores faltantes tiene características únicas y, por lo tanto, requiere enfoques diferentes para tratarlas. Se iniciará con las más simples: `is_4wd` y `paint_color`.

Para la columna `is_4wd`, se reemplazaran los valores faltantes por 0, lo que indica que el vehículo no tiene tracción en las cuatro ruedas. También se modificara el tipo de dato de esta columna a booleano, ya que consiste principalmente en valores de sí o no.

En cuanto a la columna `paint_color`, dado que está relativamente poco relacionada con el enfoque principal del análisis, se rellenaran los valores faltantes con 'unknown' sin afectar significativamente la calidad general de los datos.
''')

data['is_4wd'] = data['is_4wd'].where(data['is_4wd'] == 1, 0).astype('bool')
data['paint_color'] = data['paint_color'].fillna('unknown')

st.markdown('''
Los valores en las columnas `paint_color` e `is_4wd`, ya fueron corregidos, y los tipos de datos se actualizaron correctamente. A continuación, se abordaran los valores faltantes en las tres columnas restantes.

Las columnas model_year, cylinders y odometer son fundamentales para el análisis, por lo que no se pueden eliminar. Sin embargo, imputar los valores faltantes usando métodos como la mediana, puede introducir sesgos en el análisis.

Además, estas columnas están interrelacionadas con otras. Por ejemplo, el valor de odometer está relacionado con el año de fabricación del vehículo (model_year, que también tiene valores faltantes) y con su estado (condition). La columna cylinders depende en gran medida de la columna model, la cual tiene numerosos valores únicos. Rellenar los valores faltantes con la mediana distorsionaría los datos a ese nivel.

Para evitar errores potenciales y distorsiones en los datos, se ha determinado eliminar todas las filas que contienen valores faltantes en estas tres columnas.
''')

data.dropna(inplace=True)
data.reset_index(drop=True, inplace=True)
st.write('Despues del proceso')
buffer = io.StringIO()
data.info(buf=buffer)
info_str = buffer.getvalue()
st.code(info_str)

st.markdown('''
La eliminación de registros con valores ausentes en las columnas model_year, cylinders y odometer, representa una pérdida del 30% aproximadamente de los datos. Sin embargo, incluso con 36.419 filas restantes, el conjunto de datos sigue siendo considerablemente grande, robusto y lo suficientemente representativo para los objetivos actuales del análisis.

Aunque la pérdida de datos no es ideal, es fundamental priorizar la calidad y la confiabilidad de la información para obtener resultados precisos. Con el conjunto de datos disponible, se puede continuar con el análisis con confianza, teniendo en cuenta la representatividad de los datos restantes.
''')

data['model_year'] = data['model_year'].astype('int')
data['cylinders'] = data['cylinders'].astype('int')
data['odometer'] = data['odometer'].astype('int')
data['date_posted'] = pd.to_datetime(data['date_posted'], format='%Y-%m-%d')



st.subheader('1.5 Ingenieria de Características (Features Engineering)')

st.markdown('''
Ahora se procede a mejorar la calidad del conjunto de datos, modificando algunos tipos de datos y añadiendo algunos campos nuevos y útiles que facilitaran el proceso de análisis.

1. day_posted: Extrae día de la semana desde la columna date_posted, esto permite examinar, si el día de publicación del anuncio influye en la duración del mismo y potencialmente en el precio de venta.

2. month_posted: Extrae mes desde la columna date_posted, esto brindará información sobre tendencias estacionales y permitirá analizar posibles variaciones en el precio de venta según el mes de publicación.

3. year_posted: Extrae el año desde la columna date_posted permite seguir la evolución de los precios de venta a lo largo del tiempo y analizar tendencias a largo plazo.

4. mileage_per_year: Columna calculada dividiendo el valor del odómetro (odometer) por la edad del vehículo (año actual menos model_year). Representa el kilometraje promedio anual de cada vehículo, lo que puede ofrecer información valiosa sobre la intensidad de uso y su posible influencia en el precio de venta.

5. condition_rank: Valor numérico que indica el estado general de cada vehículo. Esta clasificación ayuda a evaluar cómo el estado del vehículo afecta el precio de venta y a comparar vehículos según su condición.

Con la incorporación de estas columnas, se busca enriquecer el conjunto de datos y obtener conclusiones más profundas para el análisis.
''')

data['model_year'] = pd.to_numeric(data['model_year'], errors='coerce').astype('Int64')
data['cylinders'] = pd.to_numeric(data['cylinders'], errors='coerce').astype('Int64')
data['odometer'] = pd.to_numeric(data['odometer'], errors='coerce').astype('Int64')
data['date_posted'] = pd.to_datetime(data['date_posted'], format='%Y-%m-%d', errors='coerce')
data['day_posted'] = data['date_posted'].dt.day_name()
data['month_posted'] = data['date_posted'].dt.month_name()
data['year_posted'] = data['date_posted'].dt.year
data['age_year'] = data['year_posted'] - data['model_year']
data['age_year'] = data['age_year'].replace(0, pd.NA) 
data['age_year'] = data['age_year'].where(data['age_year'] != 0, 1)
data['mileage_per_year'] = data['odometer'] / data['age_year']
data['condition_rank'] = data['condition'].replace(['new', 'like new', 'excellent', 'good', 'fair', 'salvage'], [5, 4, 3, 2, 1, 0])
data.insert(4, 'condition_rank', data.pop('condition_rank'))
condition_dict = data[['condition_rank','condition']].drop_duplicates().sort_values('condition_rank').reset_index(drop=True)

st.write('Informacion general del dataset luego de las correciones')
buffer = io.StringIO()
data.info(buf=buffer)
info_str = buffer.getvalue()
st.code(info_str)

option = st.checkbox('Muestra de dataset final')
if option:
    st.dataframe(data.head(5), use_container_width=True)
    st.write('Nuevo tamaño del dataset', data.shape)


# # Análisis Exploratorio de Datos ============================================================================================
st.header("3 Análisis Exploratorio de Datos")

st.markdown('''
            Se analizaran los siguientes parametros:
                
                - Precio ('price')
                - Antiguedad ('age_year')
                - Kilometraje ('odometer')
                - Numero de Cilindros ('cylinders')
                - Condicion ('condition_rank')
            ''')

fig = make_subplots(rows=5, cols=1, subplot_titles=(
    'Precio',         
    'Antigüedad del Vehículo',
    'Kilometraje',
    'Cantidad de Cilindros',
    'Condición'))
fig.add_trace(
    go.Box(x=data['price'], name='Precio', orientation='h'),
    row=1, col=1)
fig.add_trace(
    go.Box(x=data['age_year'], name='Antigüedad', orientation='h'),
    row=2, col=1)
fig.add_trace(
    go.Box(x=data['odometer'], name='Kilometraje', orientation='h'),
    row=3, col=1)
cyl_counts = data['cylinders'].value_counts().sort_index()
fig.add_trace(
    go.Bar(x=cyl_counts.index, y=cyl_counts.values, name='Cilindros'),
    row=4, col=1)
cond_counts = data['condition_rank'].value_counts().sort_index()
fig.add_trace(
    go.Bar(x=cond_counts.index, y=cond_counts.values, name='Condición'),
    row=5, col=1)
fig.update_layout(height=1500, width=1200, showlegend=False)
st.plotly_chart(fig)


st.markdown('''
Hallazgos:

- Las columnas `price`, `age_year` y `odometer` contienen una cantidad significativa de valores atípicos.

- La distribución de los tipos de cilindros de los vehículos se concentra principalmente en 4, 6 y 8 cilindros, lo que coincide con las configuraciones más comunes en la mayoría de los vehículos. Sin embargo, todavía hay algunos vehículos con una cantidad distinta de cilindros en el conjunto de datos.

- La mayoría de los vehículos del conjunto de datos están clasificados como de calidad moderada, dentro de las categorías "good" y "excellent".

- Para asegurar un análisis más limpio y preciso, se eliminaran todos los valores atípicos. Cabe destacar que esto puede reducir la cantidad de datos disponibles para el análisis. Sin embargo, el conjunto resultante ofrecerá una base más clara y confiable para el análisis.
''')

# Tratamiento Valores Atipicos =======================================================================================
st.subheader('3.1 Tratamiento de Valores Atipicos')

lower_whisker = 0

def upper_whisker(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    value = Q3 + (1.5 * IQR)
    return value

df = data[(data['price'] < upper_whisker(data, 'price')) & (data['age_year'] < upper_whisker(data, 'age_year')) & (data['odometer'] < upper_whisker(data, 'odometer'))].reset_index(drop=True)

st.write(f'Luego de remover los valores atipicos de las columnas anteriormente mencionadas el dataset nuevamente disminuyo sus registros {df.shape}, pero aun asi sigue siendo robusto para el análisis del proyecto. A continuación se comparar ambas graficas para ver el antes y el despues de la limpieza.')

fig = make_subplots(rows=3, cols=2, subplot_titles=(
    'Precio',
    'Precio limpio',
    'Antigüedad del Vehículo',
    'Antigüedad del Vehículo limpia',
    'Kilometraje',
    'Kilometraje limpio'))
fig.add_trace(
    go.Box(x=data['price'], name='Precio',orientation='h'),
    row=1, col=1)
fig.add_trace(
    go.Box(x=data['age_year'], name='Antigüedad',orientation='h'),
    row=2, col=1)
fig.add_trace(
    go.Box(x=data['odometer'], name='Kilometraje', orientation='h'),
    row=3, col=1)
fig.add_trace(
    go.Box(x=df['price'], name='Precio',orientation='h'),
    row=1, col=2)
fig.add_trace(
    go.Box(x=df['age_year'], name='Antigüedad',orientation='h'),
    row=2, col=2)
fig.add_trace(
    go.Box(x=df['odometer'], name='Kilometraje', orientation='h'),
    row=3, col=2)
fig.update_layout(height=1200, width=1000, showlegend=False)
st.plotly_chart(fig)

st.write('Descripcion de los datos originales')
st.write(data.describe())

st.write('Descripcion de los datos limpios')
st.write(df.describe())

# Duracion del Anuncio ============================================================================================

st.subheader('Duracion del anuncio')

st.markdown('Ahora se indagará la columna days_listed, en los nuevos datos, para medir la duración de tiempo en que un anuncio estuvo publicado.')

st.write(df['days_listed'].describe())

st.write(df['days_listed'].mode())

st.write(df[df['days_listed'] == 24]['days_listed'].count())


st.markdown('''
En promedio (media), los anuncios se muestran durante aproximadamente 40 días antes de que el vehículo sea vendido o el anuncio eliminado. La mayoría de los anuncios se muestran durante 24 días, que es la moda y representa la duración más común.

El tiempo mínimo (min) que un anuncio estuvo publicado es de 0 días, lo que indica que algunos anuncios podrían haber sido eliminados o cancelados de inmediato. Por otro lado, el tiempo máximo (max) que un anuncio estuvo activo es de 271 días, lo que equivale a aproximadamente 9 meses.

Para comprender mejor la distribución de estos datos, los visualizará mediante un histograma u otros métodos apropiados.
''')

fig = px.histogram(df, x='days_listed')
st.plotly_chart(fig)

fig = px.box(x=df['days_listed'])
st.plotly_chart(fig)

st.markdown('''
El histograma muestra que la mayoría de los anuncios se publican por menos de 50 días, lo que indica que la mayoría de los vehículos se venden en ese período. Sin embargo, también hay una cantidad significativa de anuncios que permanecen activos por períodos más largos, llegando hasta 271 días.

La duración de la publicación de un anuncio puede verse influida por diversos factores como el precio del vehículo, su tipo, condición o antigüedad. Es posible que los vehículos con precios más altos o con ciertas características necesiten más tiempo para encontrar comprador. Se puede realizar un análisis adicional para explorar la relación entre estos factores y la duración del anuncio.

En general, esta información ofrece una visión general sobre cómo se comportan los anuncios de vehículos en términos de duración en la plataforma.
''')

# Precio promedio por vehiculo ============================================================================================

st.markdown('''
A continuación, se calculará la cantidad de anuncios y el precio promedio para cada tipo de vehículo. Además, se indagará la relación entre la cantidad de anuncios y el tipo de vehículo. Posteriormente, se seleccionaran los dos tipos de vehículos con mayor número de anuncios.
''')

st.write('Precio promedio y numero de anuncios por tipo de vehiculo')

mean_price = df. pivot_table(index='type', values='price', aggfunc=['mean', 'count'])
mean_price.columns = ['average_price', 'number_of_list']
st.write(mean_price.sort_values(by='number_of_list', ascending=False))

st.write('Correlacion entre precio promedio y cantidad de anuncios')

st.write(mean_price['average_price'].corr(mean_price['number_of_list']))

st.markdown('''
El tipo de vehículo con mayor número de anuncios no está directamente correlacionado con el precio. Los vehículos más anunciados no son necesariamente los más caros ni los más baratos. De hecho, la correlación entre la cantidad de anuncios y el precio es muy baja (-0.04).
''')

sorted_df = mean_price.sort_values('number_of_list').reset_index()
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=sorted_df[sorted_df.columns[0]],
    y=sorted_df['number_of_list'],
    mode='markers',  # <<< SOLO puntos
    marker=dict(size=8, color='blue')))
st.plotly_chart(fig)

st.markdown('''
Según el gráfico, se puede observar un aumento significativo en la cantidad de anuncios para los tres tipos de vehículos más populares en comparación con los demás. Por lo tanto, para el análisis posterior, se centrará en los dos tipos con mayor número de anuncios, es decir, sedanes y SUVs.
''')


# Factor Precio ============================================================================================
st.header('Factor Precio')

st.markdown('''
Ahora se realizará un análisis para investigar los factores que más influyen en el precio de los vehículos. Específicamente, el enfoque de este análisis en los dos tipos de vehículos más populares: sedanes y SUVs.

Para evaluar la correlación entre el precio de estos tipos de vehículos y varios parámetros, se consideraran los siguientes factores:

- Antiguedad del vehículo (age_year)

- Kilometraje (odometer)

- Condición (condition_rank)

- Tipo de transmisión (transmission)

- Color de pintura (paint_color)

Ahora puede seleccionar que tipo de vehiculo quiere analizar primero, o incluso revisar ambos en conjunto.            
''')

st.write('Selecciona el tipo de informe')
option_1 = st.checkbox('Sedan')
option_2 = st.checkbox('SUV')

button = st.button('Entregar informe(s) seleccionado(s)')  # crear un botón

if option_1 & option_2:
    if button:
        st.subheader('Informe general por tipo de vehiculos')
        st.subheader('Sedan')
        df_sedan = df[df['type'] == 'sedan'].reset_index(drop=True)
        df_sedan = df_sedan[['price','age_year', 'odometer', 'condition_rank', 'transmission', 'paint_color']]
        st.write('Correlacion de las variables con el Precio')
        st.write(df_sedan.select_dtypes(include='number').corr()['price'])
        st.write('Graficos de Correlacion entre las Variables')
        fig = make_subplots(rows=3, cols=1, subplot_titles=[
                'Precio vs Condición',
                'Precio vs Antigüedad',
                'Precio vs Kilometraje'])
        fig.add_trace(
            go.Scatter(
                x=df_sedan['condition_rank'],
                y=df_sedan['price'],
                mode='markers',
                marker=dict(color='blue')),
                row=1, col=1)
        fig.add_trace(
            go.Scatter(
                x=df_sedan['age_year'],
                y=df_sedan['price'],
                mode='markers',
                marker=dict(color='green')),
                row=2, col=1)
        fig.add_trace(
            go.Scatter(
                x=df_sedan['odometer'],
                y=df_sedan['price'],
                mode='markers',
                marker=dict(color='orange')),
                row=3, col=1)
        fig.update_layout(
            height=1000, width=1300,
            showlegend=False,)
        st.plotly_chart(fig)
        
        st.markdown('''
        Basado en el análisis de correlación, se observa una correlación negativa significativa entre el precio de los vehículos sedán, su antiguedad y kilometraje. A medida que aumenta la edad o el kilometraje, el precio tiende a disminuir.

        Por otro lado, existe una correlación positiva débil entre el precio y la condición de los sedanes. Sin embargo, es importante destacar que mejorar la condición del vehículo no garantiza necesariamente un precio más alto. Los precios parecen ser relativamente más altos para vehículos de calidad moderada (niveles 2, 3, 4) en comparación con aquellos de alta calidad (nivel 5).

        A continuación, se analizaran las correlaciones en las variables categóricas, específicamente el tipo de transmisión (`transmission`) y el color del vehículo (`paint_color`).

        Para asegurar la validez del análisis, primero se estudiará la cantidad de anuncios en cada categoría dentro de estas variables. Idealmente, se necesitan al menos 50 anuncios por categoría para garantizar una representación suficiente en el análisis.            
        ''')
        st.write('Cantidad de vehiculos sedan con un tipo de transmision')
        st.write(df_sedan['transmission'].value_counts())
        
        st.write('Cantidad de vehiculos sedan por color')
        st.write(df_sedan['paint_color'].value_counts())
        
        st.markdown('''
        La variable `transmission` parece tener un número suficiente de anuncios en cada categoría, lo que permite realizar un análisis válido. Sin embargo, la característica `paint_color` contiene tres categorías —morado (purple), amarillo (yellow) y naranja (orange)— que no cumplen con el mínimo de 50 anuncios por categoría. Por lo tanto, estas tres categorías de color seran excluidas del análisis.
        ''')
        
        fig = px.box(
                    df_sedan,
                    x='price', 
                    y='transmission',
                    color='transmission',
                    width=800, 
                    height=500)
        st.plotly_chart(fig)
        
        st.markdown('''
        Es evidente que los vehículos con transmisión automática tienden a tener precios más altos en comparación con los vehículos con transmisión manual u otros tipos. El análisis de correlación sugiere una relación positiva entre el tipo de transmisión y el precio del vehículo, lo que indica que los vehículos automáticos suelen tener un precio más elevado que los de transmisión manual u otros.        
        ''')
        
        df_sedan_color = df_sedan[~df_sedan['paint_color'].isin(['purple', 'yellow', 'orange'])]
        fig = px.box(df_sedan_color, 
                    x='price', 
                    y='paint_color',
                    color='paint_color',
                    width=800, 
                    height=500)
        st.plotly_chart(fig)
        
        st.markdown('''
        La correlación entre el precio y el color del vehículo es relativamente baja, lo que indica que no existe una diferencia significativa de precio entre los distintos colores. El color del vehículo parece tener un impacto mínimo en el precio de los sedan.
        ''')
        
        st.subheader('SUV')
        df_suv = df[df['type'] == 'SUV'].reset_index(drop=True)
        df_suv = df[['price','age_year', 'odometer', 'condition_rank', 'transmission', 'paint_color']]
        st.write('Correlacion de las variables con el Precio')
        st.write(df_suv.select_dtypes(include='number').corr()['price'])
        st.write('Graficos de Correlacion entre las Variables')
        fig = make_subplots(rows=3, cols=1, subplot_titles=[
                'Precio vs Condición',
                'Precio vs Antigüedad',
                'Precio vs Kilometraje'])
        fig.add_trace(
            go.Scatter(
                x=df_suv['condition_rank'],
                y=df_suv['price'],
                mode='markers',
                marker=dict(color='blue')),
                row=1, col=1)
        fig.add_trace(
            go.Scatter(
                x=df_suv['age_year'],
                y=df_suv['price'],
                mode='markers',
                marker=dict(color='green')),
                row=2, col=1)
        fig.add_trace(
            go.Scatter(
                x=df_suv['odometer'],
                y=df_suv['price'],
                mode='markers',
                marker=dict(color='orange')),
                row=3, col=1)
        fig.update_layout(
            height=1000, width=1300,
            showlegend=False,)
        st.plotly_chart(fig)
        
        st.markdown('''
        El patrón de correlación en los SUVs es relativamente similar al de los sedanes, pero con coeficientes de correlación más bajos. La columna `age_year` presenta una correlación de -0.533737, la columna `odometer` tiene una correlación de -0.435377, y la columna `condition_rank` muestra una correlación de 0.186926.

        Al igual que en los sedanes, la correlación con la columna `condition_rank` indica que los SUVs de calidad media tienden a tener precios más altos.

        A continuación, se revisará la validez de las variables categóricas `transmission` y `paint_color`, examinando la cantidad de anuncios en cada categoría. Se necesitan al menos 50 anuncios por categoría para asegurar la validez del análisis.
        ''')
        
        st.write('Cantidad de vehiculos SUV con un tipo de transmision')
        st.write(df_suv['transmission'].value_counts())
        
        st.write('Cantidad de vehiculos SUV por color')
        st.write(df_suv['paint_color'].value_counts())
        
        st.markdown('''
        Dado que todas las categorías en las variables `transmission` y `paint_color` tienen más de 50 anuncios, podemos continuar con el análisis.

        Se examinaran las correlaciones entre el precio y las variables categóricas para los SUVs. Primero, se estudiará la correlación con la variable transmission.            
        ''')
        
        fig = px.box(
                    df_suv,
                    x='price', 
                    y='transmission',
                    color='transmission',
                    width=800, 
                    height=500)
        st.plotly_chart(fig)
        
        fig = px.box(df_suv, 
                    x='price', 
                    y='paint_color',
                    color='paint_color',
                    width=800, 
                    height=500)
        st.plotly_chart(fig)
        
        st.markdown('''
        Se puede apreciar que en los SUVs, el tipo de transmisión "otro" está asociado a precios medianos más altos en comparación con las transmisiones automática y manual. Además, los SUVs de color naranja y amarillo tienden a presentar niveles de precio más altos en comparación con otros colores.

        Estos hallazgos ofrecen información valiosa para comprender los factores que influyen en los precios de los SUVs. Al considerar tanto el tipo de vehículo como sus variables categóricas asociadas, se obtiene una comprensión más completa de los patrones de precios.
        ''')

elif option_1:
    if button:
        st.subheader('Informe de vehiculos "Sedan"')
        df_sedan = df[df['type'] == 'sedan'].reset_index(drop=True)
        df_sedan = df_sedan[['price','age_year', 'odometer', 'condition_rank', 'transmission', 'paint_color']]
        st.write('Correlacion de las variables con el Precio')
        st.write(df_sedan.select_dtypes(include='number').corr()['price'])
        st.write('Graficos de Correlacion entre las Variables')
        fig = make_subplots(rows=3, cols=1, subplot_titles=[
                'Precio vs Condición',
                'Precio vs Antigüedad',
                'Precio vs Kilometraje'])
        fig.add_trace(
            go.Scatter(
                x=df_sedan['condition_rank'],
                y=df_sedan['price'],
                mode='markers',
                marker=dict(color='blue')),
                row=1, col=1)
        fig.add_trace(
            go.Scatter(
                x=df_sedan['age_year'],
                y=df_sedan['price'],
                mode='markers',
                marker=dict(color='green')),
                row=2, col=1)
        fig.add_trace(
            go.Scatter(
                x=df_sedan['odometer'],
                y=df_sedan['price'],
                mode='markers',
                marker=dict(color='orange')),
                row=3, col=1)
        fig.update_layout(
            height=1000, width=1300,
            showlegend=False,)
        st.plotly_chart(fig)
        
        st.markdown('''
        Basado en el análisis de correlación, se observa una correlación negativa significativa entre el precio de los vehículos sedán, su antiguedad y kilometraje. A medida que aumenta la edad o el kilometraje, el precio tiende a disminuir.

        Por otro lado, existe una correlación positiva débil entre el precio y la condición de los sedanes. Sin embargo, es importante destacar que mejorar la condición del vehículo no garantiza necesariamente un precio más alto. Los precios parecen ser relativamente más altos para vehículos de calidad moderada (niveles 2, 3, 4) en comparación con aquellos de alta calidad (nivel 5).

        A continuación, se analizaran las correlaciones en las variables categóricas, específicamente el tipo de transmisión (`transmission`) y el color del vehículo (`paint_color`).

        Para asegurar la validez del análisis, primero se estudiará la cantidad de anuncios en cada categoría dentro de estas variables. Idealmente, se necesitan al menos 50 anuncios por categoría para garantizar una representación suficiente en el análisis.            
        ''')
        st.write('Cantidad de vehiculos sedan con un tipo de transmision')
        st.write(df_sedan['transmission'].value_counts())
        
        st.write('Cantidad de vehiculos sedan por color')
        st.write(df_sedan['paint_color'].value_counts())
        
        st.markdown('''
        La variable `transmission` parece tener un número suficiente de anuncios en cada categoría, lo que permite realizar un análisis válido. Sin embargo, la característica `paint_color` contiene tres categorías —morado (purple), amarillo (yellow) y naranja (orange)— que no cumplen con el mínimo de 50 anuncios por categoría. Por lo tanto, estas tres categorías de color seran excluidas del análisis.
        ''')
        
        fig = px.box(
                    df_sedan,
                    x='price', 
                    y='transmission',
                    color='transmission',
                    width=800, 
                    height=500)
        st.plotly_chart(fig)
        
        st.markdown('''
        Es evidente que los vehículos con transmisión automática tienden a tener precios más altos en comparación con los vehículos con transmisión manual u otros tipos. El análisis de correlación sugiere una relación positiva entre el tipo de transmisión y el precio del vehículo, lo que indica que los vehículos automáticos suelen tener un precio más elevado que los de transmisión manual u otros.        
        ''')
        
        df_sedan_color = df_sedan[~df_sedan['paint_color'].isin(['purple', 'yellow', 'orange'])]
        fig = px.box(df_sedan_color, 
                    x='price', 
                    y='paint_color',
                    color='paint_color',
                    width=800, 
                    height=500)
        st.plotly_chart(fig)
        
        st.markdown('''
        La correlación entre el precio y el color del vehículo es relativamente baja, lo que indica que no existe una diferencia significativa de precio entre los distintos colores. El color del vehículo parece tener un impacto mínimo en el precio de los sedan.
        ''')
        
elif option_2:
    if button:
        st.subheader('Informe de vehiculos "SUV"')
        df_suv = df[df['type'] == 'SUV'].reset_index(drop=True)
        df_suv = df[['price','age_year', 'odometer', 'condition_rank', 'transmission', 'paint_color']]
        st.write('Correlacion de las variables con el Precio')
        st.write(df_suv.select_dtypes(include='number').corr()['price'])
        st.write('Graficos de Correlacion entre las Variables')
        fig = make_subplots(rows=3, cols=1, subplot_titles=[
                'Precio vs Condición',
                'Precio vs Antigüedad',
                'Precio vs Kilometraje'])
        fig.add_trace(
            go.Scatter(
                x=df_suv['condition_rank'],
                y=df_suv['price'],
                mode='markers',
                marker=dict(color='blue')),
                row=1, col=1)
        fig.add_trace(
            go.Scatter(
                x=df_suv['age_year'],
                y=df_suv['price'],
                mode='markers',
                marker=dict(color='green')),
                row=2, col=1)
        fig.add_trace(
            go.Scatter(
                x=df_suv['odometer'],
                y=df_suv['price'],
                mode='markers',
                marker=dict(color='orange')),
                row=3, col=1)
        fig.update_layout(
            height=1000, width=1300,
            showlegend=False,)
        st.plotly_chart(fig)
        
        st.markdown('''
        El patrón de correlación en los SUVs es relativamente similar al de los sedanes, pero con coeficientes de correlación más bajos. La columna `age_year` presenta una correlación de -0.533737, la columna `odometer` tiene una correlación de -0.435377, y la columna `condition_rank` muestra una correlación de 0.186926.

        Al igual que en los sedanes, la correlación con la columna `condition_rank` indica que los SUVs de calidad media tienden a tener precios más altos.

        A continuación, se revisará la validez de las variables categóricas `transmission` y `paint_color`, examinando la cantidad de anuncios en cada categoría. Se necesitan al menos 50 anuncios por categoría para asegurar la validez del análisis.
        ''')
        
        st.write('Cantidad de vehiculos SUV con un tipo de transmision')
        st.write(df_suv['transmission'].value_counts())
        
        st.write('Cantidad de vehiculos SUV por color')
        st.write(df_suv['paint_color'].value_counts())
        
        st.markdown('''
        Dado que todas las categorías en las variables `transmission` y `paint_color` tienen más de 50 anuncios, podemos continuar con el análisis.

        Se examinaran las correlaciones entre el precio y las variables categóricas para los SUVs. Primero, se estudiará la correlación con la variable transmission.            
        ''')
        
        fig = px.box(
                    df_suv,
                    x='price', 
                    y='transmission',
                    color='transmission',
                    width=800, 
                    height=500)
        st.plotly_chart(fig)
        
        fig = px.box(df_suv, 
                    x='price', 
                    y='paint_color',
                    color='paint_color',
                    width=800, 
                    height=500)
        st.plotly_chart(fig)
        
        st.markdown('''
        Se puede apreciar que en los SUVs, el tipo de transmisión "otro" está asociado a precios medianos más altos en comparación con las transmisiones automática y manual. Además, los SUVs de color naranja y amarillo tienden a presentar niveles de precio más altos en comparación con otros colores.

        Estos hallazgos ofrecen información valiosa para comprender los factores que influyen en los precios de los SUVs. Al considerar tanto el tipo de vehículo como sus variables categóricas asociadas, se obtiene una comprensión más completa de los patrones de precios.
        ''')
else:
    if button:
        st.write('!!! Debe seleccionar uno o ambos tipos de vehiculos !!!')

st.header('4 Conclusion general')
st.markdown('''
Con base en el análisis exploratorio de datos (EDA), realizado sobre el conjunto de datos de Crankshaft List, se identifican varios hallazgos claves. La antiguedad y el kilometraje del vehículo tienen un impacto significativo en el precio, siendo que a mayor edad y mayor kilometraje, el precio tiende a disminuir. Sin embargo, la correlación entre precio y condición del vehículo es relativamente débil.

Además, el análisis revela que la relación entre el precio y las variables categóricas varía según el tipo de vehículo. En los sedanes, el tipo de transmisión desempeña un papel más relevante en la determinación del precio, con transmisiones automáticas asociadas generalmente a precios más altos. En cambio, en los SUVs, el tipo de transmisión "otro" parece estar asociado a los precios más altos.

Respecto al color, en los sedanes, no se observan variaciones significativas de precio según el color, en los SUVs, ciertos colores como el naranja y el amarillo presentan precios más elevados.

En conclusión, al analizar los precios de los vehículos en el conjunto de datos Crankshaft List, es fundamental tener en cuenta la antiguedad, el kilometraje y el tipo de transmisión, mientras que el impacto de la condición del vehículo y el color es relativamente menor.

Estos hallazgos pueden ser de gran utilidad para compradores, vendedores y analistas que deseen entender los principales factores que influyen en el precio de los vehículos en este conjunto de datos.
''')