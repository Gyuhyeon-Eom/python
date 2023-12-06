import numpy as np
import matplotlib.pyplot as plt
from numpy import log as ln

address = 'https://url.kr/k43ayv'
data = np.loadtxt(address)
L = data[:, 0]
M = data[:, 1]

x = ln(L)
y = ln(M)

b_new = 0  
a_new = 0  
learning_rate = 0.01  
epochs = 1000  

for epoch in range(epochs):
    y_pred = a_new + b_new * x
    error = y_pred - y
    a_gradient = 2 * np.mean(error)
    b_gradient = 2 * np.mean(error * x)
    a_new -= learning_rate * a_gradient
    b_new -= learning_rate * b_gradient


f_gradient_descent = a_new + b_new * x


print("Optimized a:", a_new)
print("Optimized b:", b_new)


plt.scatter(x, y, marker='x', label="data")
plt.plot(x, f_gradient_descent, label="Gradient Descent Regression", color='red')
plt.legend()
plt.xlabel('ln(L)')
plt.ylabel('ln(M)')
plt.title('Regression using Gradient Descent')
plt.show()