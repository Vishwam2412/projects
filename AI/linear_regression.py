import random
import math

random.seed(42)

TRUE_W = 3.0
TRUE_B = 7.0
N_SAMPLES = 100

X = [ random.uniform(0,10) for _ in range(N_SAMPLES) ]
y = [ TRUE_W*x + TRUE_B + random.gauss(0,2.0) for x in X]
print(f"Generated {N_SAMPLES} samples")
print(f"True relationship: y = {TRUE_W}x + {TRUE_B} (+ noise)")
print(f"First 5 points: {[(round(X[i], 2), round(y[i], 2)) for i in range(5)]}")


class LinearRegression:

    def __init__(self,learning_rate):
        self.weight = 0.0
        self.bias = 0.0
        self.lr = learning_rate
        self.cost_history = []

    def predict(self , X):
        return [ self.weight * x + self.bias for x in X ]
    
    def compute_cost( self , X , y):
        prediction = self.predict(X)
        n = len(y)
        cost = sum( (pred-actual)**2  for pred , actual in zip(prediction,y)) / n
        return cost
    def compute_gradient( self , X , y ):
        prediction = self.predict(X)
        n = len(y)
        dw = 2/n * sum((pred - actual)*x for pred , actual , x in zip(prediction,y,X))
        db = 2/n * sum((pred - actual) for pred , actual in zip(prediction,y))
        return dw , db

    def fit(self , X , y , epochs=1000 , every=200):
        for epoch in range(epochs):
            dw , db = self.compute_gradient( X , y)
            self.weight -=  self.lr*dw
            self.bias -= self.lr * db
            cost = self.compute_cost(X,y)
            self.cost_history.append(cost)
            if epoch % every == 0:
                print( f" Epoch : {epoch:4d} | Weight : {self.weight:.4f} | Bias : {self.bias:.4f} | Cost : {cost:.4f}" )
    def r_squared(self , X , y):
        prediction = self.predict( X )
        y_mean = sum(y)/len(y)
        ss_res = sum( (pred-actual)**2 for pred , actual in zip(prediction,y) )
        ss_tot = sum( (actual-y_mean)**2 for actual in y  )
        return 1 - (ss_res/ss_tot)


print("=== Training Linear Regression (Gradient Descent) ===")
model = LinearRegression(learning_rate=0.005)
model.fit(X, y, epochs=1000, every=200)
print(f"\nLearned: y = {model.weight:.4f}x + {model.bias:.4f}")
print(f"True:    y = {TRUE_W}x + {TRUE_B}")
print(f"R-squared: {model.r_squared(X, y):.4f}")







