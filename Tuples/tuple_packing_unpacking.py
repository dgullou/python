x = 10,15
print(x) #(10, 15)
print(type(x)) #<class 'tuple'>

x1 = ('jason',25)
print(x1[0]) #jason
print(x1[1]) #25
name, age = x1
print(name) #jason
print(age) #25

a, b = (15,100)
print(a) #15
print(b) #100

xx = 25
yy = 35
#let yy=25, xx=35
temp = xx
xx = yy
yy = temp
print(xx) #35
print(yy) #25

#or

x1 = 25
y1 = 35
x1,y1 = y1,x1
print(x1,y1) #35 25

c = ([1,2,3], "jason")
c[0][1] = 100
print(c) #([1, 100, 3], 'jason')