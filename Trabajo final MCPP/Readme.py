
# coding: utf-8

# **Análisis de la evolución de indicadores de inclusión financiera en Colombia 2011-2015**

# 26-Noviembre-2016

# <img src="Documents/Trabajo final MCPP/Word Cloud.png">

# **Motivación y descripción**

# Dentro del Plan Nacional de Desarrollo 2014 – 2018 se establecen metas específicas en materia de inclusión financiera 
# como lo son incentivar la reducción del uso de efectivo en la economía, aumentar el número de adultos con acceso al
# sistema financiero, reducir la inactividad en las cuentas de ahorro y dinamizar el acceso al crédito sobretodo en zonas de díficil acceso como el sector rural.

# Algunas de las preguntas que motivan este trabajo son:
# 1. ¿Hay más o menos adultos con acceso al sistema financiero? ¿Dentro que rangos hay una mayor participación de adultos en el sistema financiero?
# 2. ¿En qué lugares hay más cuentas de ahorro activas? ¿Cómo ha evolucionado el ahorro?
# 3. ¿Qué departamentos tienen mayor acceso a microcrédito? ¿Cómo ha sido la dinámica de desembolsos de microcrédito en los últimos años?
# 4. ¿Comó ha sido el acceso al crédito por parte de víctimas del conflicto armado en el último año?
# 

# El siguiente análisis puede ser una herramienta tanto para priorizar las diferentes tareas y generar un plan de acción, como para monitorear el cumplimiento de objetivos 

# **Métodos utilizados y resultados obtenidos** 

# La información proviene de la Superintendencia financiera de Colombia. Para responder las preguntas planteadas se realiza un anáslisis descriptivo de los datos por medio de las distintias herramientas que se aprendieron en la clase (Python, R, Qgis y Tableau).
# 

# cobebetura financiera: La herramienta utilizada fue Python. Se crearon tuplas con los datos que se iban a gráficar. 
# Se encontró que entre 2011 y 2015 aumentó el número de adultos con algún producto financiero y que el mayor  porcentaje de adultos con algún producto financiero se encuentra en el rango de edad de 41 a 65 años.

# <img src="Documents/Trabajo final MCPP/cobertura.png">

# <img src="Documents/Trabajo final MCPP/cobertura_edad.png">

# Análisis transaccional: la herramienta utilizada fue R. Se crean las variables que se van a gráficar y se encuentra que las personas estan utilizando otros mecanismos para hacer sus transacciones como lo son los corresponsales bancarios, los cuales permiten que personas en zonas rurales o alejadas puedan tener acceso al sistema financiero. Por otro lado, se encuentra que el ha aumentado el número de personas con telefónos móviles, los cuales también facilita las transacciones y permite que las personas puedan realizar operaciones que normalmente hacen a través de bancos de una forma más fácil y ágil.

# <img src="Documents/Trabajo final MCPP/3.png">

# <img src="Documents/Trabajo final MCPP/4.png">

# Ahorro: Se analiza el número de cuentas de ahorro tradicionales activas por departamento a través de un mapa georeferenciado el cual se realiza con tableau. Así mismo, se hace un análisis de la evolución de las cuentas de ahorro entre 2011-2015, así como el monto ahorrado en estas. Ambas gráficas se hacen con tableau. Los resultados muestran que el mayor número de cuentas tradicionales están en los departamentos donde se ubican las ciudades principales. Así mismo, se ha presentado una tendencia creciente en el número de cuentas de ahorro, sin embargo, la mayoría de estas tienen montos muy bajos por debajo de los 5 SMMLV.

# <img src="Documents/Trabajo final MCPP/5.png">

# <img src="Documents/Trabajo final MCPP/6.png">

# <img src="Documents/Trabajo final MCPP/7.png">

# Crédito: Primero se analiza el número de desembolsos de microcrédito de hasta 25 SMMLV por departamentos a través de un mapa georeferenciado por QGIS. Después se hacen dos gráficos en Python donde se utilizan tuplas con los datos para ver como ha sido la evolución de los desembolsos de microcréditos de hasta 1 SMMLV (menor monto) y de los desembolsos de 25 a 120 SMMLV (mayor monto), así como la evolución de los desembolsos por nivel de ruralidad. Se encuentra que al igual que con las cuentas de ahorro la mayor parte de los desembolsos de microcrédito se da en las grandes áreas metropolitanas, sin embargo, esto no se ha mantenido en los últimos años donde la participación en el sector rural ha aumentado. Por otro lado, en los últimos años se observa un aumento de los desembolsos de microcrédito de bajo monto.

# <img src="Documents/Trabajo final MCPP/8.png">

# <img src="Documents/Trabajo final MCPP/9.png">

# <img src="Documents/Trabajo final MCPP/10.png">

# Victimas con acceso a crédito: Se realiza un mapa con tableau donde se mira el número de desembolsos de crédito  a las víctimas por departamento y se encuentra que los departamentos con mayor número de desembolsos en 2015 son Antioquia y Nariño. 

# <img src="Documents/Trabajo final MCPP/11.png">

# **Ejercicio de statistical learning: Componentes principales**

# Cuando hay variables que pueden tener correlación, este metodo permite reducir la dimensionalidad de un conjunto de datos. Este convierte un conjunto de observaciones de variables posiblemente correlacionadas en un conjunto de valores de variables sin correlación lineal llamadas componentes principales.
# 
# 

# Se utilizan las siguientes variables: número cuentas de ahorro tradicionales, número de cuentas de ahorro electronicas, desembolsos microcrédito hasta 25 SMMLV, desembolsos microcrédito entre 25 y 120 SMMLV. Estas cifras se reportan en la BASE.csv

# <img src="Documents/Trabajo final MCPP/12.png">

# el componente principal 1 le da un peso similar a desembolsos de 25 SMMLV, de 25 a 120 SMMLV, y a cuentas tradcionales activas. Mientras que el segundo componente le da mayor peso a cuentas de ahorro electrónicas. Vemos que dentro del grupo de departamento se destacan Bogotá, Antioquia y Valle del Cauca. Esto refleja las brechas existentes entre las principales metropolís y el resto del país. 
