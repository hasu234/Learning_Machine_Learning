# Description: Yield is a keyword that is used like return, except the function will return a generator.

# Iterables
print("--------------Iterables---------------")
mylist = [x*x for x in range(3)]
print(mylist)
for i in mylist:
    print(i)

# Generators
print("--------------Generators---------------")
mygenerator = (x*x for x in range(3))
print(mygenerator)
for i in mygenerator:
    print(i)

# Yield
print("--------------Yield---------------")
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!

for i in mygenerator:
    print(i)
