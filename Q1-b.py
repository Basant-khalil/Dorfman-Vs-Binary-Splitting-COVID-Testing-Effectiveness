import matplotlib.pyplot as plt
import numpy as np
import math

# 1.b - 1
p = np.arange(0.0, 0.4, 0.0005)
n = np.arange(0, 25)
n_star = []
for diff_p in p:
    max = 0
    max_n = 0
    for i in n:
        num = i / (i + (1-i) * math.pow(1-diff_p, i))
        if(num > max):
            max = num
            max_n = i
    n_star.append(max_n)
x_axis = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.xticks(x_axis)
y_axis = range(0, 26, 2)
plt.yticks(y_axis)
plt.xlabel("p")
plt.ylabel("n*")
plt.title("p vs n*")
plt.plot(p, np.array(n_star), color='c')
plt.savefig('images/1.b-1.png')
