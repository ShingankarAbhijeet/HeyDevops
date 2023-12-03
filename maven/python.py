# replace x in 1.28.x-* with the latest patch version
apt-mark unhold kubeadm kubelet kubectl && \
apt-get update && apt-get install -y kubeadm=1.26.9-00 kubelet=1.26.9-00 kubectl=1.26.9-00 && \
apt-mark hold kubeadm kubelet kubectl

'''
apt-mark unhold kubeadm kubectl kubelet && \
apt-get update && apt-get install -y kubeadm=1.25.14-00 kubelet=1.25.14-00 kubectl=1.25.14-00 && \
apt-mark hold kubeadm kubectl kubelet

 apt-mark unhold kubeadm kubectl kubelet && apt-get update && apt-get install -y kubeadm=1.25.14-00 kubelet=1.25.14-00 kubectl=1.25.14-00 && apt-mark hold kubeadm kubectl kubelet
 2052  k drain master --ignore-daemonsets --delete-emptydir-data
 2053  kubeadm upgrade plan
 2054* kubeadm vers
 2055  kubeadm upgrade apply v1.25.16
 2056  kubeadm upgrade apply v1.25.14
 2057  sudo systemctl daemon-reload
 2058  sudo systemctl restart kubelet
 2059  k uncordon master



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