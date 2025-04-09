a = {1,3,4,5}
b = {3,4,7,8}
print(a.difference(b)) #{1, 5}
print(b.difference(a)) #{8, 7}
print(a.intersection(b)) #{3, 4}
print(b.intersection(a)) #{3, 4}
print(a.union(b)) #{1, 3, 4, 5, 7, 8}
print(b.union(a)) #{1, 3, 4, 5, 7, 8}

print(a.isdisjoint(b))
print(a.issubset(b))
print(a.issuperset(b))