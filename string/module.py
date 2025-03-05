print(len("")) #0

name = 'Wilson'
print(name.upper())
print(name.lower())
print(name.islower()) #False
print(name.isupper()) #False
print(name.upper().isupper()) #True
print(name.index("s")) #3
print(name.index("il")) #1
print(name.index("sn")) #ValueError: substring not found

name1 = 'Tony'
name1.upper()
print(name1) #Tony
name1 = name1.upper()
print(name1) #TONY

