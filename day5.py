def sayhi():
    print("Hello User")

print("top")
sayhi()
print("bottom")


def sayhi(name):
    print("hello " + name)

sayhi("Beck")
sayhi("Tom")


def sayhi(name, age):
    print("Hello " + name + " , you are " + age)

sayhi("Mike" , "20")
sayhi("Tom" , "30")