myset = set({1,2,3})
print(myset) #{1, 2, 3}

mylist = [1,4,3,2,5,1,5]
print(set(mylist)) #{1, 2, 3, 4, 5}

s = set()
s.add(1)
print(s) #{1}
s.add(2)
print(s) #{1, 2}
s.add(2)
print(s) #{1, 2}
s.add(3)
s.discard(1)
print(s) #{2, 3}
s.clear()
print(s) #set()