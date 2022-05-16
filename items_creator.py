# -*- coding: utf-8 -*-
"""
Created on Wed May 11 13:44:00 2022

@author: Guillaume COSNIER
visit my website : https://www.guillaumecosnier.psychoscope.net
contact me at : guillaumecosnier.secretariat@gmail.com
subscribe to my channel : https://www.youtube.com/c/Lesingequibaille

IDs = U2I_WxxxxxxLxxxxxx_EnSeWeEvEn_xxxx
"""

"""
IMPORTATIONS
"""
import os
from mlconjug3 import Conjugator
cg = Conjugator(language='fr')
import spacy
nlp = spacy.load("fr_core_news_sm")

"""
VARIABLES ET DICTIONNAIRES
"""

mots = [{}, {}]
Logiques = [{}, {}]
Elements = {'entities' : [{}], 'events' : [{}], 'sentiments' : [{}], 'qualities' : [{}], 'weights' : [{}], 'others' : [{}]}

###CHARGER LES DICTIONNAIRES / LOAD DICTIONNARIES###
def load_elements(chemin) :
    True
def load_logics(chemin) :
    True
def load_words(chemin) :
    True
def load() :
    True

###SAUVEGARDER LES DICTIONNAIRES / SAVE DICTIONNARIES###    
def save_elements(chemin) :
    True
def save_logics(chemin) :
    True
def save_words(chemin) :
    True
def save() :
    True

"""
NON CATEGORISE
"""

class variable :
    def __init__(self) :
        True
        
"""
MANIPULATION DE MOTS
"""
class word :
    def __init__(self, token) :
        self.shape = str(token)
        self.pos = token.pos_
        self.lemma = token.lemma_
        self.morph = {}
        for i in list(token.morph) :
            self.morph[i.split('=')[0]] = i.split('=')[1]
            
    def set_number(self, number = 'Sing') :
        if number not in ['Sing', 'Plu'] :
            print("number MUST BE 'Sing' or 'Plu'")
            return
        if 'Number' in self.morph :
            if self.morph['Number'] == number :
                return
    
    def set_person(self, person = 1) :
        if self.pos == 'DET' :
            True
        elif 'Person' not  in self.morph :
            print("word has no person")
            return
    
    def set_gender(self, gender = 'Masc') :
        if 'Gender' not in self.morph :
            print("word has no gender")
            return
        if self.morph['Gender'] == gender :
            return
        if 'Locked' in self.morph :
            if 'Gender' in self.morph['Locked'] :
                print("can't change gender")
                return
        
        case = 0
        index = 1
        if self.shape[-index] == 's' :
            index += 1
            if gender == 'Masc' :
                if self.shape[-index] == 'e' :
                    self.shape = self.shape[:-index] + self.shape[index+1:]
                else :
                    print("Voilà une exception de genre à régler :", self.shape)
                    return
            else :
                
        elif self.shape[-index] == 'x' :
            

    #conjugue le verbe à un certain temps d'un certain mode / conjugate the verb to a certain tense of a certain mood
    def set_verb_shape(self, mood = 'Indicatif', tense = 'Présent') :
        #verifie que le mot est un verbe / verify that the word is a verb
        if self.pos != 'VERB' :
            print("word MUST BE 'VERB', not", self.pos)
            return
        
        #essaye d'obtenir la table de conjugaison avec mlconjug3 / try to obtain the conjugasion table with mlconjug3
        try :
            liste = cg.conjugate(self.lemma).conjug_info[mood][tense]
        except :
            False, """A FINIR"""
            return
        
        #si le nombre et le genre est déjà précisé dans les paramètres du mot, les appliquer, sinon première personne du singulier
           #if number and gender is already precised in the word's parameters, apply it, else : first person of singular 
        person = ''
        if 'Person' in self.morph :
            if mood == 'Impératif' or self.morph['Person'] not in ['1','2'] :
                self.morph['Person'] = '1'
        else :
            self.morph['Person'] = '1'
        person += self.morph['Person']
            
        if 'Number' in self.morph :
            if self.morph['Number'] == 'Plu' :
                person += 'p'
            else : 
                person += 's'
        else :
            self.morph['Number'] = 'Sing'
            person += 's'
            
        self.shape = liste[person]
        
    def translate_mood(self, direction = 1) :
        True
            
    

"""
PROCESSUS DE CREATION
"""

###CLASSE "ITEM" : PERMET DE DEFINIR UN OBJET ITEM DONT ON VA MANIPULER LES PROPRIETES. / 
    #CLASS ITEM : ALLOW TO DEFINE AN OBJECT ITEM TO MANIPULATE ITS PROPRIETIES###
class item :
    elements = {}
    ###INITIER L'ITEM AVEC DES PROPRIETES INITIALES. OPTIONNEL. / INITIATE ITEM WITH OPTIONNAL PROPRIETIES. OPTIONAL.###
    def __init__(self, entities = [], events = [], sentiments = [], qualities = [], weights = []) :
        self.elements['entities'] = entities
        self.elements['events'] = events
        self.elements['sentiments'] = sentiments
        self.elements['qualities'] = qualities
        self.elements['weights'] = weights
    
    ###APPLIQUER UN MODELE A L'ITEM, EN REMPLACANT LES ELEMENTS DU MODELE PAR CEUX DE L'ITEM.
        #APPLY A TEMPLATE TO THE ITEM BY REPLACING THE TEMPLATE'S ELEMENTS WITH THE ITEM'S ONES###
    def apply_template(self, template) :
        entities = self.elements['entities'].copy()
        events = self.elements['events'].copy()
        sentiments = self.elements['sentiments'].copy()
        qualities = self.elements['qualities'].copy()
        weights = self.elements['weights'].copy()
        it = []
        elements_used = {'entities' : [], 'events' : [], 'sentiments' : [], 'qualities' : [], 'weights' : [], 'others' : []}
        for i in template :
            if i == 'entity' :
                it.append(entities[0])
                elements_used['entities'].append(entities[0])
                del entities[0]
            elif i == 'event' :
                it.append(events[0])
                elements_used['events'].append(entities[0])
                del events[0]
            elif i == 'sentiment' :
                it.append(sentiments[0])
                elements_used['sentiments'].append(entities[0])
                del sentiments[0]
            elif i == 'quality' :
                it.append(qualities[0])
                elements_used['qualities'].append(entities[0])
                del qualities[0]
            elif i == 'weight' :
                it.append(weights[0])
                elements_used['weights'].append(entities[0])
                del weights[0]
            else :
                it.append(i)
                elements_used['others'].append(i)
        self.it = it
        self.elements_used = elements_used
        return self.it, elements_used
    
    """REDIGER L'ITEM EN RESPECTANT LES REGLES PROPRES A LA LANGUE VOULUE / WRITE THE ITEM RESPECTING THE TARGET LANGAGE'S RULES"""
    
    ###REDIGER L'ITEM EN FRANCAIS / WRITE THE ITEM IN FRENCH###
    def fr(self) :
        

###CREER UN OBJET TEMPLATE QUI COMPREND LES TYPES D'ELEMENTS IMPLIQUES, LES RELATIONS ENTRE CES ELEMENTS ET LA STRUCTURE DE L'ITEM
    #CREATE AN OBJECT TEMPLATE WHICH CONTAIN THE ELEMENTS' TYPES INCLUDED, THE RELATIONSHIP BETWEEN THOSE ELEMENTS AND THE ITEM'S STRUCTURE.###        
class template :
    def __init__(self, a) :
        True

"""
EXTRACTION DES ELEMENTS ET DE LA STRUCTURE D'UN ITEM
"""

def extract_item(str_item, mots, types, objects) :
    item = nlp(str_item)
    
    
    elements = []
    for i in item :
        if i in mots :
            if len(mots[i]['objects']) == 0:
                elements.append(i)
            else :
                elements.append(mots[i]['objects'])
        else :
            mots[i] = {'id_mot' : 'w_'+langue+'_' , 'nature' : 'unknown' , 'objects' : []}
            elements.append(i)
    return (str_item, item, elements, mots, types, objects)


"""
TEMPLATES BASIQUES
"""    

def relation_quantité(a, b, dimension, direction = 1) :
    if direction != 0 :
        direction = ' est plus '
    else : 
        direction = ' est moins '
    print(a + direction + dimension + ' ' + 'que' + ' ' + b)
    
def relation_appartenance(a, b, niveau = 1) :
    if niveau < 1 :
        niveau = 'certains '
    else :
        niveau = 'tous les '
    print(niveau, a, ' sont des ', b)

def ESV(dimension) :
    esv =\
    ['En général ma vie '+ dimension + ' correspond parfaitement à mes idéaux.',\
     'Mes conditions de vie ' + dimension + ' sont excellentes.',\
     'je suis satisfait(e) de ma vie ' + dimension, \
     "Jusqu'à maintenant, j'ai obtenu les choses importantes que je voulais de la vie " + dimension,\
     'Si je pouvais recommencer ma vie ' + dimension + ", je n'y changerais presque rien."]
    return esv

def prediction_minimale(a, nature_a, variable) :
    print(a,' est ',nature_a+ '. selon vous, quel est son/sa ', variable, ' ?')