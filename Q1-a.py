import matplotlib.pyplot as plt
import numpy as np
import math

# 1.a - 1
n = 100
p = np.arange(0.0, 0.4, 0.001)
mean = []
for i in p:
    num = n + (1-n) * math.pow(1-i, n)
    mean.append(num)
plt.xlabel("p")
plt.ylabel("E[Dn]")
plt.title("p vs E[Dn] (n=100)")
plt.plot(p, np.array(mean), color='c')
plt.savefig('images/1.a-1.png')


# 1.a - 2
p = 0.01
n = np.arange(10, 200)
mean = []
for i in n:
    num = i + (1-i) * math.pow(1-p, i)
    mean.append(num)
plt.xlabel("n")
plt.ylabel("E[Dn]")
plt.title("n vs E[Dn] (p=0.01)")
plt.xlim([10, 200])
plt.ylim([0, 200])
plt.plot(n, np.array(mean), color='c')
plt.savefig('images/1.a-2.png')
