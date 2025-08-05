class demo:
    a = 4

o = demo()
print(o.a) # prits the class attribute becausee instand attribute is not present
o.a = 0 # Instance attribute is set
print(o.a) # prints the instance attribute becouse instance attribute is present
print(demo.a)
# class attribute is not change