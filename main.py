import random
import string

adjektivliste = ['træt', 'langsom', 'lugtende', 'våd', 'tyk', 'luftig', 'hvid', 'stolt', 'modig']

substantivliste = ['æble', 'dinosaur', 'bold', 'toaster', 'ged', 'drage', 'hummer', 'and', 'panda']

farveliste = ['rød', 'orange', 'gul', 'grøn', 'blå', 'lilla']

print('Velkommen til passwordgeneratoren')
count = 3

while True:
    while count > 0:
        adjektiv = random.choice(adjektivliste)
        substantiv = random.choice(substantivliste)
        farve = random.choice(farveliste)
        nummer = random.randrange(1, 100)
        special_karakter = random.choice(string.punctuation)
        password = adjektiv + substantiv + farve + str(nummer) + special_karakter
        print(f"Her er dit nye passwowrd {password}")
        count -= 1
    count = 3
    response = input("Vil du lave et mere? j eller n")
    if response == "n":
        break
print("Program afsluttes")