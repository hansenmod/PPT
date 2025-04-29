import random
random_tuple=tuple([random.randint(0,100) for _ in range(10000)])
class MyClass(object):

    """Docstring for MyClass. """
    i=0

    def __init__(self,a):
        """TODO: to be defined. """
        self.num=tuple([random.randint(0,10) for _ in range(10)])

    def __next__(self):
        if MyClass.i<=len(self.num)-1:
            temp=self.num[MyClass.i]
            MyClass.i+=2
            return temp

        else: raise  StopIteration
    def __iter__(self):
        """TODO: Docstring for __iter__.
        :returns: TODO

        """
        return self
class MySubClass(MyClass):

    """Docstring for MySubClass. """

    def __init__(self):
                """TODO: to be defined. """
                self.st='nnn'
        
b=MyClass(19)
c=MySubClass()
i=-2
def g():
    """TODO: Docstring for g.
    :returns: TODO
    """
    global i
    i+=2
    return i
def f():
    """TODO: Docstring for f.
    :returns: TODO

    """
    raise StopIteration

d=type('nn',(object,),{'__init__':lambda self:setattr(self,'mytupl',tuple([random.randint(0,10) for _ in range(10)])),'__next__':lambda self:self.mytupl[i] if g()>=0 and i<=len(self.mytupl)-1 else f(),'__iter__':lambda self:self})()
print(d.mytupl)
for item in d:
    print(item)
tuple1=(1,2,3,4)
print(list(tuple1).index(3))
fk=(lambda:[x for x in range(1000)])
'''


'''
mydic={}.fromkeys(fk(),random.randint(0,100))
myset={1,2,3}
myset.add(5)
print(myset)
anset=myset.union([7,8])
print(anset)
aset=anset-set([1,2,3])
beset=anset.difference([1,2,3])
print(aset)
print(beset)
mydic={'a':1,'b':2}

