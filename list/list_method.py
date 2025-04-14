fr = ["jason", "tony", "jerry", "kevin"]
fr.insert(2, "david")
print(fr) #['jason', 'tony', 'david', 'jerry', 'kevin']
fr.append("aron")
fr.append(15.0)
print(fr) #['jason', 'tony', 'david', 'jerry', 'kevin', 'aron', 15.0]
my_pop = fr.pop()
print(fr) #['jason', 'tony', 'david', 'jerry', 'kevin', 'aron']
print(my_pop) #15.0
fr.remove("kevin")
print(fr) #['jason', 'tony', 'david', 'jerry']

fr.sort()
print(fr) #['david', 'jason', 'jerry', 'tony'] 按照字母排序
fr = fr[::-1] #['tony', 'jerry', 'jason', 'david'] 同等於reverse的功能 因為[::]會打印出全部加上-1就變成反序排列
print(fr)



a = [13,100,21,35,33,-3]
a.sort()
print(a) #[-3, 13, 21, 33, 35, 100]
a.reverse() 
print(a)#[100, 35, 33, 21, 13, -3]
print(a[len(a)-1]) #-3
a.clear()
print(a) #[]


x = [3,5,9,10]
y = x
y[0] = 12
print(x) #[12, 5, 9, 10]
print(y) #[12, 5, 9, 10]
print('---------------')

x1 = 10
y1 = x1
y1 = 20
print(x1) #10
print(y1) #20

xx = [1,2,3,4,5,6]
yy = x.copy()
yy[0] = 15
print(xx) #[1, 2, 3, 4, 5, 6]
print(yy) #[15, 5, 9, 10]

aa = [1, 2, [4,5,6], 2, 1, [4, 3, [-10,4]]]
print(aa[2][1]) #5
print(aa[5][2][0]) #-10

mylist = ['a', 'b', 'c', 'd']
mystring = ' and ' .join(mylist)
print(mystring) #a and b and c and d