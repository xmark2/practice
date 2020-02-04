class Joe(object):
    def callme(self):
        print('calling "callme" method with instance:  ')
        print(self)

thisjoe = Joe()

thisjoe.callme()
print(thisjoe)




myint = 5
mystr = 'hello'

print(type(myint))
print((type(mystr)))

class MyClass(object):
    pass

this_object = MyClass()
print("this {0}".format(this_object))


that_object = MyClass()
print("that {0}".format(that_object))