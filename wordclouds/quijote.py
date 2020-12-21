"""
Created on Sun Dec 20 13:11:31 2020

@author: Sergio Sanz
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt


# abrir el archivo y guardarlo en la variable alice_novel 
el_quijote = open('el_quijote.txt', 'r', encoding="utf-8").read()

# generar lista de palabras cortas para quitar
el_quijote_lista = el_quijote.split()
shortwords = set()
for w in el_quijote_lista:
    if len(w) < 5:
        if w not in shortwords:
            shortwords.add(w)       
# print(shortwords)
print(len(shortwords))
print(len(el_quijote_lista))
print ('File downloaded and saved!')

#añadir palabras para quitar a la lista del apartado anterior
stopwords = shortwords | {'contra','desde','entre','aunque','hasta',\
                        'mucho','algun','tiene','alguna','sobre','alguno'\
                        'tambie','cuanto','muchas','muchos','entonces',\
                        'estaban','palabra','nombre','porque','cuando',\
                        'estaba','aquella','manera','respondio','quiere',\
                        'despue','alguno','nuestro','vuestro','diciendo',\
                        'delante','adelante','primero','puesto','grande',\
                        'quiero','ninguna','vuestra','nuestra','parece',\
                        'cuatro','viendo','puerta','fueron','cuales','tantos',\
                        'tantas','pareci','llevar','volver','algunos','tienen',\
                        'aquello','estado','aquellos','siempre','llamaba',\
                        'caballeri'}
stopwords.remove('don')
# print(stopwords)
print(len(stopwords))

# instanciar un objeto de tipo nube
quijote_wc = WordCloud(
    background_color='#F3F1CE',
    max_words=20000,
    stopwords=stopwords,
    min_word_length=6,
    width=400, height=300,
    min_font_size=6
)

# generar la nube de palabras 
quijote_wc.generate(el_quijote)

# mostrar la nube 
fig = plt.figure()
fig.set_figwidth(18) # establecer ancho 
fig.set_figheight(14) # establecer altura 
plt.imshow(quijote_wc, interpolation='bilinear')
plt.axis('off')
plt.show()
fig.savefig('quijote.png')
