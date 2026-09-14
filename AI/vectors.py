from numpy import diff
from pandas._libs.tslibs.timedeltas import Components
class Vector:
    def __init__(self,component):
        self.component = component
        self.dim = len(component)
    
    def __sum__(self,other):
        return [x+y  for x , y in zip(self.component,other.component)]

    def __difference__(self,other):
        return [x-y  for x , y in zip(self.component,other.component)]
    
    def __magnitude__(self):
        return sum(x**2 for x in self.component)**0.5

    def __normalize__(self):
        magnitude = self.__magnitude__()
        return [x/magnitude for x in self.component]
    
    def __dot__(self,other):
        return sum(x*y for x ,y in zip(self.component,other.component))

    def __scale__(self,a):
        return [x*a for x in self.component]
    
    def __gram_schmidt__(self,other):
        z = Vector(self.__normalize__())
        b = other.__normalize__()
        n =  z-(b.__scale__(other.__magnitude__()))
        return n.__normalize__()
    
    def __repr__(self):
        return f"Vector({self.component})"



