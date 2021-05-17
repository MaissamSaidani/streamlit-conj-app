# Etape 1 : charger le dictionnaire (fichier texte) dans une structure dict
# ouvrir le fichier, le lire ligne par ligne
# decouper chaque ligne sur la base du sep (\t)
# enregistrer les données (forme, lemme, info_gramm) dans le dico
# dico['marcher'] = {'present_indicatif_personne1' : 'marche', 'pers2' : 'marches', 'pers6' : 'marchent'}

# Etape 2 du programme

#output = {'present_indicatif_personne1' : 'marche', 'pers2' : 'marches', 'pers6' : 'marchent'}

# 182371  14      étaient être    v0ei_____a iimp 3pl     été     ATNT            @       lat     *   
import streamlit as st
import pandas as pd
st.title(''''My first app''')

dico = {}

with open(r'''\Users\Sam\Desktop\L3\S6\PYTHON\Projet_HN\lexique-grammalecte-fr-v7.0\nv-lexique.txt''', encoding='utf8') as f:
  for line in f:
    res = line.split("\t")
    if len(res)>5:
      if res[3].startswith("VER"):
        if res[2] in dico:
          data = dico[res[2]]
          infog = res[10].split(":")
          if len(infog) == 3 :
            data.append({"mode" : infog[0], "temps" : infog[1], "nombre" : infog[2][1], "personne" : infog[2][0],  "forme" : res[0]})
          #data.append({res[3]: res[10]})
            dico[res[2]] = data
  
        else:
          infos = res[10].split(";")
          if len(infos) == 1:
            infog = res[10].split(":")
            if len(infog) == 3 :
              dico[res[2]] = [{"mode" : infog[0], "temps" : infog[1], "nombre" : infog[2][1], "personne" : infog[2][0],  "forme" : res[0]}]
          else:
            d = []
            for inf in infos :
              infog = inf.split(":")
              if len(infog) == 3 :
                d.append({"mode" : infog[0], "temps" : infog[1], "nombre" : infog[2][1], "personne" : infog[2][0],  "forme" : res[0]})
            
            dico[res[2]] = d


#dico[res[2]] = [{"infogrammaticale" :res[10], "forme" : res[0]}]

print(dico["chanter"])
 
a = st.sidebar.text_input('''Entrez un verbe à l'infinitif''')
#for a in dico[a]:
  #st.text(a)
  #for info in a:
    #data = info.split(" ")
    #st.text(data[1:])
    #st.text(a[info]
st.write(pd.DataFrame(dico[a]))


#st.markdown("## Besoin d'aide?")
#st.info("Pour utiliser ce conjugueur, cliquez sur la flèche pointant vers la droite en haut à gauche de la page.  Ensuite, entrez un verbe à l'infinitif et tapez Entrée.  La conjugaison du verbe que vous avez entré s'affiche ! Extraire dans un fichier txt ou tout autre et imprimer???")

  #print(dico)
#a = input("Entrez un verbe à l'infinitif")
#for a in dico[a]:
  #print(a)
