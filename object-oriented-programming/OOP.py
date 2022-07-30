# class -> instanciate -> instances

# Class is store in memory.
# We are using that memory every time we create an object using that stored class

class BigObject: # Class
    pass;

obj1 = BigObject(); # Instanciate
obj2 = BigObject(); # Instanciate
obj3 = BigObject(); # Instanciate

print(type(BigObject)) # prints type
print(type(obj1)) # prints __main__.BigObject