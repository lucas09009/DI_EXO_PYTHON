

#1)
my_fav_numbers = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
my_fav_numbers.discard(12)
print(my_fav_numbers)

friend_fav_numbers = set([13, 14, 15, 16, 17, 18, 19, 20, 21])

our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)


#2)
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Non, je ne peux rien ajouter à my_tuple car elle est immuable, c'est à dire qu'une fois définit, on ne peut plus les modifier



#3)
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
del basket[0]
basket.remove("Blueberries")    
basket.append("Kiwi")
basket.insert(0,"Apples")
def count(value, liste):
    c = 0
    for item in basket:
        if item == "Apples":
            c += 1
            return c
print(basket)



#4) Un float en python, c'est le terme utilisé pour désigner l'ensemble des nombres décimaux.
#La différence entre un entier et un float est la suivante: un entier(integer) est un nombre qui ne comporte pas de virgule, par contre
#un float est un nombre à virgules

import random 
b = random.randint(1,9)
nFloat = random.uniform(0, 10)
print(b)
print(nFloat)
# print(b*nFloat)

my_list = [ 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5] 



#5)
for i in range(1,21):
    print(i)

for i, item in enumerate(range(1,21)):
    if(i % 2 == 0):
        print(item)
   
   
#6)
my_name = "Doe"
your_name = input("Enter your name: ")
while my_name != your_name:
    your_name = input("Enter your name: ")
else:
    print("Congratulations")
    
    
#7)
yourfav_Fruits = input("Veuillez entrez vos fruits préférées en les séparant par un evirgule, Ex:apple,mango,cherry: ")
yourfav_Fruits = yourfav_Fruits.split(",")
print(yourfav_Fruits)

fruit_name = input("Entrez un nom quelconque de fruits: ")
if fruit_name in yourfav_Fruits:
    print("Vous avez choisi l'un de vos fruits préférés; Amusez-vous")
    
else:
    print("Vous avez choisi un nouveau fruit; J'espère que vous apprécierez")
    
    
    

#8)
my_list = []
garnitures = input("Veuillez entrer une garniture que nous devons ajouter à votre pizza; sinon saisissez <<quit>> pour quitter: ")
while garnitures != "quit":
    my_list.append(garnitures)
    print(garnitures, "sera ajoutée à votre pizza")
    garnitures = input("Veuillez entrer une garniture que nous devons ajouter à votre pizza; sinon saisissez <<quit>> pour quitter: ")
else:
    for item in my_list:
        print(item, end=",")
        if(item == my_list[-1]):
            print(" ont été ajoutée à votre pizza, le montant total s'élève à", len(my_list)*25, "euros")
        
        

#9)
prix_total = []
reponse = input("Etes-vous une famille? saisir oui, si oui et non sinon: ")
reponse = reponse.lower()

while(reponse == "oui"):
    
    age = input("voulez-vous un billet? si non, entrez <<quit>> ,si oui, entrez votre âge: ")
    if( age == "quit"):
        print("Votre dépense s'élève à:",sum(prix_total), "euros")
        print("Finished")
        break
    else:
        age = int(age)
    if (age >= 0) and (age < 3):
        print("Le billet est gratuit")
    elif( age >=3 ) and (age <= 12):
        print("Le billet est à 8 euros")
        prix_total.append(8)
        print("Votre dépense s'élève à:",sum(prix_total), "euros")
    elif( age > 12):
        print("Le billet est à 15 euros")
        prix_total.append(15)
        print("Votre dépense s'élève à:",sum(prix_total), "euros")
    else:
        print("Saisie invalide")
            



names = ["abalo", "afi", "rené", "mamadou", "amouzou"]
for item in names:
    print(item, end=",")
    age = input("Entrez votre âge: ")    
    age = int(age)
    if(age >= 16) and (age <= 21):
        print("Vous êtes autorisé à voir ce film")
    else:
        print("Vous n'êtes pas autorisé à voir ce film")
        names.remove(item)
for item in names:
    print(item, end=",")
    if (item == names[-1]):
        print("sont autorisées à voir ce film.")
    


#10)
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
for item in sandwich_orders:
    print("Avez-vous fini de cuisiner ",item, end="")
    reponse = input(",Saisissez soit oui, soit non: ")
    reponse = reponse.lower()
    if(reponse == "oui"):
        finished_sandwiches.append(item)
    elif(reponse == "non"):
        continue
    else:
        print("Réponse Invalide")
for item in finished_sandwiches:
    print("I made your ",item)
    
    
#11)
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Pastrami sandwich", "Sabih sandwich", "Pastrami sandwich"]
print("Nous sommes à court de <<Pastrami sandwich>> ")
while( "Pastrami sandwich" in sandwich_orders ):
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)
