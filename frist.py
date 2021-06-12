
class computer():
    def __init__(self):
        self.name='dileshan'
        self.age=24

    def update(self):
        self.age=30

    def compare(self,other):               #### compare(who is calling,whom to compare)
        if self.age==other.age:
            return True
        else:
            return False

c1=computer()
c2=computer()

if c2.compare(c1):                 #### c2 is same and c1 is other
    print('same')
else:
    print('not same')

if c1==c2:                              #### c1 and c2 have different id, they are unequla
    print("values are same")
else:
    print('values are diffrent')


if c1.age==c2.age:                     #### c1.age andc2.age is 24
    print("values are same")
else:
    print('values are diffrent')




c1.name='prasad'
c1.age=22

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)

if c1==c2:
    print("values are same")
else:
    print('values are diffrent')


c1.update()

print(c1.age)
print(c1.name)

print(id(c1))
print(id(c2))


if c1.compare(c2):                 #### c1 is same and c2 is other
    print('same')
else:
    print('not same')
