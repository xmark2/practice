import random

class MyRandomClass(object):
    def dothis(self):
        self.rand_val = random.randint(1,10)

myinst = MyRandomClass()
myinst.dothis()
print(myinst.rand_val)
