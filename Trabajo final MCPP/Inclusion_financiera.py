
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 10),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
plt.rcParams.update(params)
plt.style.use('ggplot')
p1 = plt.bar(ind, ciudad, width)


# In[6]:

plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor']='black'
N=5
producto= (65,67.2,71.6,72.7,75.4)
ind = np.arange(N)    
width = 0.35 
p1 = plt.bar(ind, producto, width)
plt.ylabel('Porcentaje')
plt.title('Número de adultos con algún porducto financiera')
plt.xticks(ind + width/2., ('2011', '2012', '2013', '2014', '2015'))
plt.yticks(np.arange(0, 81, 10))
plt.show()


# In[12]:

# Data to plot
labels = '18 a 25 años ', '26 a 40 años', '41 a 65 años','Más de 65 años '
sizes = [11.2, 38.3, 42.1,8.3]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'] 
# Plot
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()


# Para abrir la base de datos con la evolución de los desembolsos utilizamos el siguiente comando: 

# In[83]:

desembolsos = pd.read_excel('Evolucion_desembolsos.xls')
desembolsos = desembolsos.set_index('tiempo')


# In[84]:

desembolsos


# In[87]:

Grafico=desembolsos[['< a 1 SMMLV','> a 25 SMMLV hasta <=120 SMMLV']].plot(linewidth=3,title="Evolucion desembolsos");
Grafico.set_axis_bgcolor('white')
Grafico.spines['bottom'].set_color('black')
Grafico.spines['left'].set_color('black')
Grafico.set_ylabel("Porcentaje %")
legend = Grafico.legend(bbox_to_anchor=(1.1, 1.15))
frame = legend.get_frame()
frame.set_facecolor('White')


# In[102]:

plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor']='black'
N = 5
ciudad = (68,65,63,62,60)
intermedio = (19,21,22,22,24)
rural=(7.9,9.0,9.9,10.8,10.3)
ruraldisperso=(4.6,5.0,5.3,5.2,5.3)
ind = np.arange(N)    
width = 0.35       

p1 = plt.bar(ind, ciudad, width, color='b')
p2 = plt.bar(ind, intermedio, width, color='c')
p3 = plt.bar(ind, rural, width, color='m')
p4 = plt.bar(ind, ruraldisperso, width, color='r')

plt.ylabel('Porcentaje')
plt.title('porcentaje de desembolsos de microcrédito por nivel de ruralidad')
plt.xticks(ind + width/2., ('2011', '2012', '2013', '2014', '2015'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('ciudad', 'intermedio','rural','rural disperso'))
plt.show()



# In[ ]:



