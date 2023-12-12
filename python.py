def try_recursion(k):    # => fucntion calls itself
    if (k>0):
        result = k + try_recursion(k - 1)
        print(result)
    else:
        result =0
    return result
print("\n\nRecursin example results")
try_recursion(6)
'''
def my_fun():
    pass    # -> fun can not be empty but if you want add pass


def my_fun(x):
    return 5*x
print(my_fun(3))
print(my_fun(5))
print(my_fun(6))


def my_fun(food):
    for i in food:
        print(i)
fruits = ["apple", "banana", "cherry"]
my_fun(fruits)

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_fun(*kids):
    print("younges kid is "  + kids[0])
my_fun("abz","last", "gcp")


def my_fun(fname,lname):
    print(fname +  " "+ lname)
my_fun("abz", "last")

def my_fun(fname):
    print(fname + "refsnes")
my_fun("emil")
my_fun("david")
my_fun("python")

#Functions
def my_fun():
    print("hello")
my_fun()

for x in [0, 1, 2]:
  pass
print (x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for i in adj:
    for j in fruits:
        print(i,j)


for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("finished")

for x in range(7):
    print(x)
else:
    print("finaly finisheds")


for i in range(2,30,3):
    print(i)

for x in range(2,6):
    print(x)



#range()  => loop through set of codes

for x in range(6):
    print(x)



fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i== "banana":
        continue
    print(i)


fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i == "banana":
        break
    print(i)



fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)
    if i == "banana":
     break

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