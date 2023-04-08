#EXERCICE 1

# Écrire un programme qui calcule et imprime une valeur selon cette formule donnée:
# Q = Square root of [(2 * C * D)/H]
# On trouvera ci-après les valeurs fixes de C et H:
# C a 50 ans.
# H a 30 ans.
# Demandez à l'utilisateur une chaîne de nombres séparées par des virgules, utiliser chaque numéro de l'utilisateur comme Ddans la formule
# et renvoient tous les résultats

# Par example, si l'utilisateur entre: 100,150,180
# Le produit devrait être:

# 18,22,24


#1)
import math
C = 50
H = 30
VALUE = input("Veuillez entrez des nombres séparées par une virgule, Ex:2,3,5: ")
VALUE = VALUE.split(",")
for item in VALUE:
    D = int(item)
    Q = math.sqrt( (2 * C * D)/H)
    print("La valeur de Q est:", Q)
    
    
    
    
#EXERCICE 2

#1)Stocker la liste des nombres dans une variable.
ma_liste = []
list1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
list2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
list3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
list4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
for item in list1:
    ma_liste.append(item)
for item in list2:
    ma_liste.append(item)
for item in list3:
    ma_liste.append(item)
for item in list4:
    ma_liste.append(item)
print(ma_liste,"\n")

#2)
#Imprimer les informations suivantes: La liste des numéros imprimé en une seule ligne 
for item in (ma_liste):
    print(item, end=",")
print("\n")


#Imprimer les informations suivantes:La liste des nombres triés par ordre décroissant (le plus grand à le plus petit) 
ma_liste.sort()
print(ma_liste,"\n")

#Imprimer les informations suivantes:La somme de tous les nombres
print(sum(ma_liste),"\n")
   
        
#3)Une liste contenant le premier et le dernier nombre.
uno_lista = []
uno_lista.append(ma_liste[0])
uno_lista.append(ma_liste[-1])
print(uno_lista,"\n")


#4)Une liste de tous les nombres supérieurs à 50
dos_lista = []
for item in ma_liste:
    if(item > 50):
        dos_lista.append(item)
print(dos_lista,"\n")

    
#5)Une liste de tous les nombres inférieurs à 10
tres_lista = []
for item in ma_liste:
    if(item < 10):
        tres_lista.append(item)
print(tres_lista,"\n")
        
        
#6)Une liste de tous les nombres au carré – par exemple pour [1, 2, 3) vous imprimeriez « 1 4 9 ».
cuatro_lista = []
for item in ma_liste:
    cuatro_lista.append(item**2)
print(cuatro_lista,"\n")


#7)Les chiffres sans double emploi – impriment également le nombre de numéros dans la nouvelle liste.
chiffres_uniques = set(ma_liste)
print(chiffres_uniques)
print(len(chiffres_uniques))


#8)La moyenne de tous les nombres.
moyenne = sum(ma_liste)/len(ma_liste)
print(moyenne)


#9)Le plus grand nombre. 
ma_liste.sort()
print(ma_liste[-1])


#10)Le plus petit nombre
ma_liste.sort()
print(ma_liste[0])



#11)
# Trouvez la somme sans utiliser de fonctions intégrées. 
somme = 0
for item in ma_liste:
    somme += item
print(somme)
    
    
# Trouvez la moyenne sans utiliser de fonctions intégrées. 
somme = 0
indice = 0
for item in ma_liste:
    somme += item  
    indice += 1
moyenne = somme/indice
print(moyenne)


# Trouvez le plus petit nombre sans utiliser de fonctions intégrées
a = ma_liste[0]
for i in range(1, indice):
    if(a > ma_liste[i]):
        a = ma_liste[i]
print(a)


# Trouvez le plus petit nombre sans utiliser de fonctions intégrées
a = ma_liste[0]
for i in range(1, indice):
    if(a < ma_liste[i]):
        a = ma_liste[i]
print(a)


#Au lieu d'utiliser des listes de nombres prédéfinies, demandez à l'utilisateur de 10 nombres entre -100 et 100. 
# Demandez à l’utilisateur un entier compris entre -100 et 100 – répétez cette question 10 fois. Chaque nombre doit être ajouté dans une
# variable que vous avez créée plus tôt. 

#12)
liste = []
saisie = int(input("Veuillez entrer 10 nombres entre -100 et 100 séparé par des vigules, Ex:5,8,9: "))
liste.append(saisie)
while len(liste) < 10:
    saisie = int(input("Veuillez entrer 10 nombres entre -100 et 100 séparé par des vigules, Ex:5,8,9: "))
    liste.append(saisie)
print(liste)


#génèrez 10 entiers aléatoires. Assurez-vous que ces entiers aléatoires ont une longueur comprise entre -100 et 100. 
#13)
import random
my_list = []
num_aleatoire = random.randrange(-100, 101)
my_list.append(num_aleatoire)
while len(my_list) < 10:
    num_aleatoire = random.randrange(-100, 101)
    my_list.append(num_aleatoire)
print(my_list)
    
    
    
#14)
nombreAleatoire = random.randint(50,100)    
print(nombreAleatoire)



#15)
#oui mon code fonctionnera, même si le nombre de nombres aléatoires n'est pas égale à 10, car le fonctionnement de notre code n'est pas
# conditionné au fait que le nombre de nombres aléatoires soit obligatoirement égale à 10.



#EXERCICE 3
text = "We can find real-life examples of data structures as well There are so many lists online about all sorts of topics.Another example is the use of tables to display schedules. A novel stores and organizes text in paragraphs. All these mediums store data and allow us to manipulate or access it in a certain way. Data structures are a crucial part of computer programming. Since we frequently deal with data manipulation, it is of paramount importance to organize it in an efficient and meaningful way."

#Imprimez un message bien formaté disant:Combien de caractères contient la variable
print(f"Notre texte contient {len(text)} caractères")


#Imprimez un message bien formaté disant:Combien de phrases contient la variable
phrase = 0
for item in text:
    if(item =="."):
        phrase += 1
print("Notre texte contient",phrase,"phrases")
    
    
#Imprimez un message bien formaté disant:Combien de mots contient la variable
mot = 0
for item in text:
    if(item == " "):
        mot += 1
print("Notre texte contient",mot,"mots")


#Imprimez un message bien formaté disant: Combien de mots uniques contient la variable
onlyWord = text.split(" ")
onlyWord = set(onlyWord)
print("Nous avons",len(onlyWord),'mots uniques')
print(onlyWord)


#Combien de caractères non-espaces blancs contient.
noSpace = len(text.replace(" ", ""))
print("Nombre de caractères non-espaces blancs:", noSpace)


#le montant moyen des mots par phrase dans le paragraphe.   
moyenneMot_phrase = len(text)/phrase
print(moyenneMot_phrase)



#le montant des mots non uniques dans le paragraphe.
value = mot - len(onlyWord)
print(value)



#EXERCICE 4
dict = {}
saisie = input("veuillez saisir une phrase: ")
saisie = saisie.split()
print(saisie)
for item in saisie:
    if(item in dict):
        dict[item] +=1
    else:
        dict[item] = 1
for item in dict:
    print(f"{item}:{dict[item]}")
