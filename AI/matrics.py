from vectors import Vector
import random



class Matrix:
    def __init__(self,rows):
        self.rows = [list(row) for row in rows ]
        self.shape = [len(rows),len(rows[0])]
    
    def __matmul__(self,other):
        if(isinstance(other,Vector)):
            return Vector([
                sum(self.rows[i][j] * other.components[j] for j in range(self.dim[1]))
                for i in range(self.dim[0]);
            ])

            print("HEllo")
        
        rows = []
        for i in range(self.dim[0]):
            row = []
            for j in range(self.dim[1]):
                row.append(
                    sum(rows[i][k] * rows[k][j] for k in range(len(self.dim[1])))
                )
            rows.append(row)
        return Matrix(rows)

    def transpose(self):
        return Matrix([[self.rows[j][i] for j in range(self.dim[0])] 
        for i in range(self.dim[1])
        ])

    def __repr__(self):
        return f"Matrix : {self.rows}"






















