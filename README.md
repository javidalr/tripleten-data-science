# Análisis de planes telefónicos - Proyecto 04

## Descripción del proyecto

En este proyecto, se solciita un análisis de los planes de prepago para determinar su potencial de ingresos en distintos mercados objetivo. Además, llevar a cabo pruebas de hipótesis utilizando métodos de análisis estadístico.

Megaline, un operador de telecomunicaciones, ofrece dos paquetes de prepago: Surf y Ultimate. El departamento de publicidad busca optimizar el presupuesto publicitario identificando qué plan de prepago genera más ingresos.

El análisis, consta de una muestra de 500 clientes de Megaline y exploraremos su comportamiento, incluyendo su identidad, lugar de origen, tipo de plan y estadísticas de uso como la cantidad de llamadas y mensajes enviados durante 2018. Al analizar el comportamiento del cliente, nuestro objetivo es determinar qué paquete de prepago genera mayores ingresos para Megaline.

## Descripción de los datos

Se proporcionan cinco conjuntos de datos para este análisis, cada uno con distinta información. A continuación se describen:

### megaline_users (datos de usuarios):

user_id: ID del usuario

first_name: Nombre del usuario

last_name: Apellido del usuario

age: Edad del usuario en años

reg_date: Fecha de suscripción (dd, mm, aa)

churn_date: Fecha en que el usuario dejó de usar el servicio (si está vacío, significa que el plan seguía activo cuando se generaron los datos)

city: Ciudad donde vive el usuario

plan: Nombre del plan telefónico

### megaline_calls (datos de llamadas):

id: ID único de cada sesión de llamada

call_date: Fecha de la llamada

duration: Duración de la llamada en minutos

user_id: ID del usuario que realizó la llamada

### megaline_messages (datos de SMS):

id: ID único del SMS

message_date: Fecha en que se envió el SMS

user_id: ID del usuario que envió el SMS

### megaline_internet (datos de sesiones web):

id: ID único de cada sesión web

mb_used: Volumen de datos consumido durante la sesión en megabytes

session_date: Fecha de la sesión web

user_id: ID del usuario

### megaline_plans (datos de planes telefónicos):

plan_name: Nombre del plan telefónico

usd_monthly_fee: Tarifa mensual en dólares

minutes_included: Minutos de llamada incluidos al mes

messages_included: SMS incluidos al mes

mb_per_month_included: Volumen de datos incluido al mes en megabytes

usd_per_minute: Precio por minuto si se excede el límite del plan

usd_per_message: Precio por SMS si se excede el límite del plan

usd_per_gb: Precio por gigabyte adicional si se excede el límite del plan (1 GB = 1024 megabytes)

## Hipótesis

- El ingreso promedio de los usuarios de los planes telefónicos Ultimate y Surf es diferente.

- El ingreso promedio de los usuarios en el área NY-NJ es diferente al ingreso de los usuarios de otras regiones.

## Librerías

- Pandas
- NumPy 
- Matplotlib
- Seaborn
- SciPy
