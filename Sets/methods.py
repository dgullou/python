a = {1,3,4,5}
b = {3,4,7,8}
print(a.difference(b)) #{1, 5}
print(b.difference(a)) #{8, 7}
print(a.intersection(b)) #{3, 4}
print(b.intersection(a)) #{3, 4}
print(a.union(b)) #{1, 3, 4, 5, 7, 8}
print(b.union(a)) #{1, 3, 4, 5, 7, 8}

print(a.isdisjoint(b)) #False 因為有交集 (意思：兩個集合有沒有交集。)
print(a.issubset(b))
#False 意思：檢查一個集合是不是另一個集合的子集合。
# a = {1, 2}
# b = {1, 2, 3}
# print(a.issubset(b))  # True，a 是 b 的子集合
print(a.issuperset(b))
#Fasle 意思：檢查一個集合是不是另一個集合的超集合（即包含對方所有元素）
# a = {1, 2, 3}
# b = {1, 2}
# print(a.issuperset(b))  # True，a 是 b 的超集合

# isdisjoint	沒有交集	{1,2}.isdisjoint({3}) → True
# issubset	是對方的子集合	{1,2}.issubset({1,2,3}) → True
# issuperset	是對方的超集合	{1,2,3}.issuperset({1}) → True