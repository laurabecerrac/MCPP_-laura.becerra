
# coding: utf-8

# # Taller 9
# Métodos Computacionales para Políticas Públicas - URosario
# 
# **Entrega: viernes 28-oct-2016 11:59 PM**

# <div class="alert alert-success">
# **[Laura Becerra Cardona]** <br><br>
# [l.becerra52@uniandes.edu.co]
# </div>

# ## Instrucciones:
# - Guarde una copia de este *Jupyter Notebook* en su computador, idealmente en una carpeta destinada al material del curso.
# - Modifique el nombre del archivo del *notebook*, agregando al final un guión inferior y su nombre y apellido, separados estos últimos por otro guión inferior. Por ejemplo, mi *notebook* se llamaría: mcpp_taller9_santiago_matallana
# - Marque el *notebook* con su nombre y e-mail en el bloque verde arriba. Reemplace el texto "[Su nombre acá]" con su nombre y apellido. Similar para su e-mail.
# - Desarrolle la totalidad del taller sobre este *notebook*, insertando las celdas que sea necesario debajo de cada pregunta. Haga buen uso de las celdas para código y de las celdas tipo *markdown* según el caso.
# - Recuerde salvar periódicamente sus avances.
# - Cuando termine el taller:
#     1. Descárguelo en PDF. Si tiene algún problema con la conversión, descárguelo en HTML.
#     2. Suba todos los archivos a su repositorio en GitHub, en una carpeta destinada exclusivamente para este taller, antes de la fecha y hora límites.

# ---

# NLTK Book (http://www.nltk.org/book/), Exercises:
# - Chapter 1: 22, 26, 28
# - Chapter 2: 2, 4, 11

# In[5]:

import nltk
from nltk.book import *
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# ## Language Processing and Python 

# #### 2. Find all the four-letter words in the Chat Corpus (text5). With the help of a frequency distribution (FreqDist), show these words in decreasing order of frequency.

# In[6]:

punto2 = sorted([w.lower() for w in text5 if len(w) is 4 if w.isalpha()])


# In[7]:

fdist2 = FreqDist(punto2)
fdist2.most_common()


# #### 26. What does the following Python code do? sum(len(w) for w in text1) Can you use it to work out the average word length of a text

# In[8]:

(sum([len(w) for w in text1])) / len(text1)


# #### 28. Define a function percent(word, text) that calculates how often a given word occurs in a text, and expresses the result as a percentage.

# In[9]:

def percent(word, text):
    return "{:.2%}".format(text.count(word) / len(text4))


# In[10]:

percent('part', text4) 


# ## Accessing Text Corpora and Lexical Resources 

# #### 2. Use the corpus module to explore austen-persuasion.txt. How many word tokens does this book have? How many word types?

# In[11]:

p2 = nltk.corpus.gutenberg.words('austen-persuasion.txt')


# In[12]:

len(p2)


# In[13]:

len(set(p2))


# #### 4. Read in the texts of the State of the Union addresses, using the state_union corpus reader. Count occurrences of men, women, and people in each document. What has happened to the usage of these words over time?

# In[14]:

from nltk.corpus import state_union


# In[15]:

cfd = nltk.ConditionalFreqDist((target, fileid[:4])
                               for fileid in state_union.fileids()
                               for w in state_union.words(fileid)
                               for target in ['men', 'women', 'people']
                               if w.lower() == target)
cfd.tabulate()


# In[16]:

cfd.plot()


# #### 6.  In the discussion of comparative wordlists, we created an object called translate which you could look up using words in both German and Italian in order to get corresponding words in English. What problem might arise with this approach? Can you suggest a way to avoid this problem?

# In[17]:

from nltk.corpus import swadesh
de2en = swadesh.entries(['de', 'en'])
it2en = swadesh.entries(['it', 'en'])
translate2 = dict(de2en)
translate2.update(dict(it2en))
len(translate2)


# In[18]:

translate2['bianco']


# In[19]:

translate2['Hund']


# ---
