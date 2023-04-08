#1)

ma_liste1 = ["john", "Doe", "Alex", "Bernard", "Arnold", 3, 4, 5, 6, 7, 8, 9]
ma_liste2 = ["adjo", "bruno", "daniel", "godwin", "julien"] 
ma_liste1.extend(ma_liste2)
print(ma_liste1)

#ou
ma_liste1 = ["john", "Doe", "Alex", "Bernard", "Arnold", 3, 4, 5, 6, 7, 8, 9]
ma_liste2 = ["adjo", "bruno", "daniel", "godwin", "julien"] 
for item in ma_liste2:
    ma_liste1.append(item)
print(ma_liste1)



#2)

for item in range(1500, 2501):
    if(item % 5 == 0):
        print("les multiples de 5 sont:",item)
    if(item % 7 == 0):
        print("les multiples de 7 sont:", item)
        
        


#3)
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']   
name = input("Saisir un nom:")
if (name in names):
    i = (names.index(name))
    print(i)
    j = names.index(name,i+1)
    print(j)

    


#4)
ma_list = []
num1 = int(input("Veuillez entrer un nombre: "))
ma_list.append(num1)

num2 = int(input("Veuillez entrer un nombre: "))
ma_list.append(num2)

num3 = int(input("Veuillez entrer un nombre: "))
ma_list.append(num3)

ma_list.sort()
print("le plus grand nombre est:", ma_list[-1])




#5)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for item in alphabet:
    if(item == "A" or item == "E" or item == "I" or item == "O" or item == "U" or item == "Y"):
        print(item, "est une voyelle")
    else:
        print(item, "est une consonne")




#6)
words = input("Entrez sept mots séparées par une virgule, Ex: course,sommeil,balade,santé,virage,girafe,ballon: ")
words = words.split(",")
letter = input("Veuillez entrer une lettre: ")
for i, item in enumerate(words):
    if letter in item:
        print("Dans le mot",item,"la lettre",letter, "se trouve à la position",item.index(letter))
    else:
        print("La lettre",letter,"ne se trouve dans",item)
        
        


#7)
ma_list = list(range(1,1000001))    
print(min(ma_list))
print(max(ma_list))
print(sum(ma_list))




#8)
saisie = input("Veuillez saisir des nombres séparées par une virgule, Ex:23,20,15,19: ")
saisie = list(saisie)
ma_tuple = tuple(saisie)
print(saisie)
print(ma_tuple)





#9)
import random 
perd = 0
gagne = 0
saisie = int(input("Veuillez saisir un nombre entre 1 à 9:"))
while saisie not in list(range(1,10)):
    saisie = int(input("Veuillez saisir un nombre entre 1un à 9:"))
    
else:
    num_aleatoire = random.choice(range(1,10))
    while(num_aleatoire != saisie):
        perd +=1
        num_aleatoire = random.choice(range(1,10))
        print("Vous feriez mieux la prochaine fois,",num_aleatoire,"est différent de",saisie)
        saisie = (input("Veuillez saisir un nombre entre 1 à 9, sinon arrêter en saisissant<<quit>>: "))
        
        if(str(saisie) == "quit"):
            print("Vous avez fait",perd,"match et vous avez perdu ",perd,"fois")
            break
        
        elif int(saisie) >=1 and int(saisie) <=9:
            continue
        
        else:
            print("Saisie invalide")
            saisie = (input("Veuillez saisir un nombre entre 1 à 9, sinon arrêter en saisissant<<quit>>: "))

    else:
        gagne += 1
        print("Congratulations, score: Vous avez fait",gagne+perd,"match et vous avez gagné ",gagne,"fois et perdu",perd, end=' ')
        print("vous avez choisi le même numéro que la machine",num_aleatoire)
       
   