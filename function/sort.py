x = [4, 2, 3, 1]
y = sorted(x)
print("the list x is", x, ". Also, the list y is", y)
#the list x is [4, 2, 3, 1] . Also, the list y is [1, 2, 3, 4]
y = sorted(x, reverse=True)
print("the list x is", x, ". Also, the list y is", y)
#the list x is [4, 2, 3, 1] . Also, the list y is [4, 3, 2, 1]

#tuple
x = (4,2,3,1)
y = sorted(x)
print(x) #(4, 2, 3, 1)
print(y) #[1, 2, 3, 4]

#dict keys
x = {"name": "wilson", "age":25}
y = sorted(x)
print(x) #{'name': 'wilson', 'age': 25}
print(y) #['age', 'name']

#set: unordered collection of unique objects
x = {4,5,3,2,1}
y = sorted(x)
print(x) #{1, 2, 3, 4, 5}
print(y) #[1, 2, 3, 4, 5]

#string
x= "how are you doing today?"
y = sorted(x)
print(x) #how are you doing today?
print(y) #[' ', ' ', ' ', ' ', '?', 'a', 'a', 'd', 'd', 'e', 'g', 'h', 'i', 'n', 'o', 'o', 'o', 'o', 'r', 't', 'u', 'w', 'y', 'y']
