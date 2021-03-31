# Etape 1 : charger le dictionnaire (fichier texte) dans une structure dict
# ouvrir le fichier, le lire ligne par ligne
# decouper chaque ligne sur la base du sep (\t)
# enregistrer les données (forme, lemme, info_gramm) dans le dico
# dico['marcher'] = {'present_indicatif_personne1' : 'marche', 'pers2' : 'marches', 'pers6' : 'marchent'}

# Etape 2 du programme

#output = {'present_indicatif_personne1' : 'marche', 'pers2' : 'marches', 'pers6' : 'marchent'}

# 182371  14      étaient être    v0ei_____a iimp 3pl     été     ATNT            @       lat     *   
import streamlit as st
st.title('''Conjugueur des verbes de la langue française''')

import streamlit as st


dico = {}
with open(r'''\Users\Sam\Desktop\L3\S6\PYTHON\Projet_HN\lexique-grammalecte-fr-v7.0\lexique-grammalecte.txt''', encoding='utf8') as f:
  for line in f:
    res = line.split("\t")
    if len(res)>5:
      if res[4].startswith("v"):
        if res[3] in dico:
          data = dico[res[3]]
          data.append({res[4]: res[2]})
          dico[res[3]] = data
        else :
          dico[res[3]] = [{res[4]: res[2]}]

#print(dico)
a = st.sidebar.text_input('''Entrez un verbe à l'infinitif''')
for a in dico[a]:
  st.text(a)

