class MyNum(object):
    def __init__(self, value):
        try:
            value = int(value)
        except:
            value = 0
        self.val = value

    def increment(self):
        self.val = self.val + 1

aa = MyNum('Hello')
bb = MyNum(100)
aa.increment()
aa.increment()
bb.increment()

print(aa.val)
print(bb.val)