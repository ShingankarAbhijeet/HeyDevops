'''
x,y,z=1,2,3
print (x, y)
for i in range(10):
    print(i)

x=8
print(type(x))
y= 'cool'
print(type(y))


x="awesomme"
def myfun():
    global x
    x = " fantastic"
myfun()
print("python is " + x)


def myfun():
    global x
    x =" fantastic"
myfun()
print("python is " + x) 


x= "awesome"
def my_fun():
    x = "fantastic"
    print("python is " + x)
my_fun()
print("python is " + x)


x=5
y=4
z="cool"
print(x+y)
#print(x+z)

x= "4"
y= '5'
print(x)
print(y)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



x = y = z = "Orange"
print(x)
print(y)
print(z)

x,y,z= "a","b","c"
print(x)
print(y)
print(z)

x= 5
y= "hello world!!"
print(type(x))
print(type(y))
print("helllo")

if 5>2:
    print("5 is greater")
    '''