name = "Josh Jordan"
print(name.replace("J", "K")) #Kosh Kordan
print(name.replace("Josh","Kyle")) #Kyle Jordan

sentence = "Today is a good day."
print(sentence.split(" ")) #['Today', 'is', 'a', 'good', 'day.']
print(list(sentence)) #['T', 'o', 'd', 'a', 'y', ' ', 'i', 's', ' ', 'a', ' ', 'g', 'o', 'o', 'd', ' ', 'd', 'a', 'y', '.']

a = "I have a string {}".format("here it is")
print(a) #I have a string here it is
b = "I have a string {}".format(15)
print(b) ##I have a string here it is
c = "I have a string {}".format(["ab","cd"])
print(c) #I have a string ['ab', 'cd']
print("{}, {}, {}".format(20, "here is it", 3.14)) #20, here is it, 3.14
print("{0}, {0}, {0}".format(20, "here is it", 3.14)) #20, 20, 20
print("{1}, {2}, {0}".format(20, "here is it", 3.14)) #here is it, 3.14, 20
print("{}, {}, {}".format(20, "here is it", 3.14, 35)) #20, here is it, 3.14
print("{name}, {address}, {age}".format(name="Wilson", age=25, address="Tw")) #Wilson, Tw, 25

#fstring - python 3.6
myname = "Wilson"
age = 25
print(f"hello, my name is {myname}, I am {age} years old.") #hello, my name is Wilson, I am 25 years old.

string = "Good day is a good day."
print(string.count("good")) #1
print(string.lower().count("good")) #2
#find vs index
print(string.find("day")) #5 在index 5
print(string.find("apple")) #-1 因為找不到
print(string.index("day")) #5
#print(string.index("apple")) #ValueError: substring not found
#所以find找不到會出現-1, index找不到會出現error message
#index shouldn't be used when you've not sure the substring can be found
#index can be used to "string, list, temples" of python
#find just only be used to string of python

n1 = "Wilson"
print(n1.startswith("W")) # true
print(n1.startswith("w")) #false
print(n1.endswith("son")) #true


