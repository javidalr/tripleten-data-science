# Análisis de Planes Telefónicos

## Resumen del Proyecto

En este proyecto se realizará un análisis de planes de prepago para determinar su potencial de ingresos en distintos mercados objetivo. Además, de llevar a cabo pruebas de hipótesis utilizando métodos de análisis estadístico.

**Megaline**, una operadora de telecomunicaciones, ofrece dos planes de prepago: **Surf** y **Ultimate**. El departamento de marketing busca optimizar el presupuesto publicitario identificando cuál de estos planes genera mayores ingresos.

En este análisis se examinará una muestra de 500 clientes de Megaline y exploraremos su comportamiento: identidad, ciudad de origen, tipo de plan y estadísticas de uso (llamadas y mensajes enviados en 2018). El objetivo es determinar cuál plan prepago genera más ingresos para Megaline.

## Descripción de los Datos

Se han recibido cinco archivos de datos, cada uno con información diferente. A continuación, se describe el contenido de cada uno:

**megaline_users (datos de usuarios):**
- `user_id`: ID del usuario  
- `first_name`: Nombre del usuario  
- `last_name`: Apellido del usuario  
- `age`: Edad en años  
- `reg_date`: Fecha de suscripción (dd/mm/aa)  
- `churn_date`: Fecha en que el usuario dejó de usar el servicio (si está vacío, significa que el plan estaba activo al generar los datos)  
- `city`: Ciudad de residencia  
- `plan`: Nombre del plan telefónico  

**megaline_calls (datos de llamadas):**
- `id`: ID único de la sesión de llamada  
- `call_date`: Fecha de la llamada  
- `duration`: Duración de la llamada en minutos  
- `user_id`: ID del usuario que hizo la llamada  

**megaline_messages (datos de SMS):**
- `id`: ID único del mensaje  
- `message_date`: Fecha del mensaje  
- `user_id`: ID del remitente  

**megaline_internet (datos de navegación web):**
- `id`: ID único de la sesión de navegación  
- `mb_used`: Volumen de datos consumidos en megabytes  
- `session_date`: Fecha de la sesión  
- `user_id`: ID del usuario  

**megaline_plans (datos de planes):**
- `plan_name`: Nombre del plan  
- `usd_monthly_fee`: Tarifa mensual en USD  
- `minutes_included`: Minutos incluidos al mes  
- `messages_included`: Mensajes SMS incluidos al mes  
- `mb_per_month_included`: Datos incluidos al mes en MB  
- `usd_per_minute`: Costo por minuto extra  
- `usd_per_message`: Costo por mensaje extra  
- `usd_per_gb`: Costo por GB extra de navegación (1 GB = 1024 MB)  

## Hipótesis

Se asignaron evaluación las siguientes hipótesis:

- La media de ingresos de los usuarios de los planes **Ultimate** y **Surf** es diferente.  
- El ingreso promedio de los usuarios del área NY-NJ es diferente al de los usuarios de otras regiones.

## Etapas

Este proyecto se divide en tres fases:

1. **Preprocesamiento de Datos**: Limpieza y preparación de los datos para el análisis, manejo de valores faltantes, eliminación de valores atípicos y transformación de datos si es necesario.

2. **Análisis de Datos**: Exploración de los datos para comprender patrones y tendencias. Incluye estadísticas descriptivas, visualizaciones y análisis de correlaciones entre variables.

3. **Pruebas de Hipótesis**: Evaluación de las hipótesis planteadas mediante pruebas estadísticas. Se definirán hipótesis nula y alternativa, se elegirá la prueba adecuada, se calculará el estadístico y se interpretarán los resultados para tomar decisiones fundamentadas.

Al completar estas etapas, se obtendrá una visión clara del comportamiento de los clientes y el rendimiento de los planes prepago en diferentes mercados.

## Librerías

- Pandas
- NumPy  
- Matplotlib  
- Seaborn
- SciPy