import math 
class Vector:
    def __init__(self,components):
        self.components = list(components)
        self.dim = len(self.components)
    
    def __add__(self,other):
        return Vector([a+b for a,b in zip(self.components,other.components)])

    def __sub__(self,other):
        return Vector([a-b for a,b in zip(self.components,other.components)])

    def dot(self,other):
        return sum(a*b for a,b in zip(self.components,other.components))

    def magnitude(self):
        return sum(x**2 for x in self.components) ** 0.5

    def normalize(self):
        m = self.magnitude()
        return Vector([x/m for x in self.components])

    def cosine_similarity(self,other):
        return self.dot(other) / (self.magnitude() * other.magnitude())

    def __repr__(self):
        return f"Vector({self.components})"
    
    def angle_between(self,other):
        return math.acos(self.cosine_similarity(other))



if  __name__=="__main__":

    a = Vector([1,2,3])
    b = Vector([2,34,45])

    print(f"a+b : {a+b}")
    print(f"a dot b : {a.dot(b)}")
    print(f"a repr : {a}")
    print(f"angle : {a.angle_between(b):.3f}")


