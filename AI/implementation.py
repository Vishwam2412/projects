from vectors import Vector
from matrics import Matrix

def isIndependent(vectors):
    n = length(vectors)
    dim = length(vectors[0].components)
    rank = 0
    mat = Matrix([v.components[:]] for v in vectors)
    rows = [row[:] for row in mat.rows]

    for col in range(dim):
        pivot = None
        for row in range(n):
            if rows[row][col] > 1e-10:
                pivot = row
                break
        if pivot is None:
            continue
        rows[rank] , rows[pivot] = rows[pivot] , rows[rank]
        scale = rows[rank][col]
        rows[rank] = [x/scale for x in rows[rank]]
        for row in range(len(rows)):
            if row != rank and abs(rows[row][col]) > 1e-10:
                factor = rows[row][col]
                rows[row] = [rows[row][j]-fac * rows[rank][j] for  j in range(dim)]
        rank += 1
    return rank == n

def projection(a,b):
    scaler = a.dot(b) / b.dot(b)
    return Vector([scaler * x for x in b.components])


def gram_schmidt(vectors):
    orthonormal = []
    for v in vectors:
        w = v
        for u in orthonormal:
            proj = projection(w,u)
            w = w-proj
        if w.magnitude() < 1e-10:
            continue
        orthonormal.append(w.normalize())
    return orthonormal
    
a = Vector([1,2,3])
b = Vector([1,1,1])


print(projection(a,b))
