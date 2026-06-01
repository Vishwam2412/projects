from vectors import Vector
import random



class Matrix:
    def __init__(self,rows):
        self.rows = [list(row) for row in rows]
        self.shape = (len(self.rows),len(self.rows[0]))

    def __matmul__(self,other):
        if isinstance(other,Vector):
            return Vector([sum(
                self.rows[i][j] * other.components[j] for j in range(self.shape[1]))
                for i in range(self.shape[0])
            ])


        rows = []

        for i in range (self.shape[0]):
            row = []
            for j in range (self.shape[1]):
                row.append(sum(
                    self.rows[i][k]*other.rows[k][j]
                    for k in range (self.shape[1])
                ))
            rows.append(row)
        return Matrix(rows)

    def transpose(self):
        return Matrix([
            [self.rows[j][i] for j in range(self.shape[0])]
            for i in range(self,shape[1])
        ])

    def __repr__(self):
        return f"Matrix({self.rows})"

if __name__=="__main__":

    x = Matrix([[1,2,3],[2,3,4],[1,2,1],[0,9,8]])
    z = Matrix([[7,3,3],[2,2,2],[1,2,1],[0,9,8]])
    y = Vector([7,8,6,6])
    
    #a = x @ y
    #b = x@z
    #print( f"a*b(vector) : {a}")
    #print( f"a*b(Matrix) : {b}")
    ##print( f"transpose : {}")
    #
    #print(x)
    
    random.seed(23)
    
    weights = Matrix([[random.gauss(0,0.5) for _ in range(3) ] for _ in range(3) ])
    input_vector = Vector([1.0,0.5,-0.3])
    
    output = weights @ input_vector
    
    print(f"Input (3D) : {input_vector}")
    print(f"Input (Matrix) : {weights}")
    print(f"output (2D) : {output}")























