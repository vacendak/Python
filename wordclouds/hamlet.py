"""
Created on Sun Dec 20 20:40:24 2020

@author: Sergio Sanz
"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


# abrir el archivo y guardarlo en la variable alice_novel 
hamlet = open('hamlet.txt', 'r', encoding="utf-8").read()

# generar lista de palabras cortas para quitar
hamlet_list = hamlet.split()
print(len(hamlet_list))
print ('File downloaded and saved!')

# palabras a excluir
prohib_hamlet = open('prohib_hamlet.txt', 'r', encoding="utf-8").read()
forbid_words = set(prohib_hamlet.split())
stopwords = STOPWORDS | forbid_words
stopwords = stopwords | {'speech','though','awhile','another','almost',\
                         'things','thousand','effect','whithin','little',\
                        'whether','library','permission','something',\
                        'attendant','attendants','exeunt','commercially',\
                        'membership','without','bussiness','wherein',\
                        'colour','business','neither','double','receive',\
                        'indeed'}
print(len(stopwords))
# print(stopwords)

# instanciar un objeto de tipo nube
hamlet_wc = WordCloud(
    background_color='#E1E1E1',
    max_words=2000,
    stopwords=stopwords,
    min_word_length=6,
    width=400, height=300,
    min_font_size=6,
    colormap='inferno',
    font_path='arial'
)

# generar la nube de palabras 
hamlet_wc.generate(hamlet)

# mostrar la nube 
fig = plt.figure()
fig.set_figwidth(18) # establecer ancho 
fig.set_figheight(14) # establecer altura 
plt.imshow(hamlet_wc, interpolation='bilinear')
plt.axis('off')
plt.show()
fig.savefig('hamlet.png')
