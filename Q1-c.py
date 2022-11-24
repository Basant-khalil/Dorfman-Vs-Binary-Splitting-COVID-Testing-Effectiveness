import matplotlib.pyplot as plt
import numpy as np
import math
import random

# Q1 - c
# Manually checked correct by expectation theorem!

p = [0.01, 0.04, 0.07, 0.1]
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

total_test_lst = []
for index in range(4):
    p_cur = p[index]
    n_star_cur = n_star[index]
    total_test = 0
    for run in range(1000):
        population = 10000
        while(population != 0):
            n_cur = min(n_star_cur, population)
            population = population - n_cur
            infected = False
            for prob in range(n_cur):
                rand_num = random.random()
                if(rand_num < p_cur):
                    infected = True
                    break
            if(infected):
                total_test = total_test + n_cur
            else:
                total_test = total_test + 1
    average_test = total_test/1000
    total_test_lst.append(average_test)

print(total_test_lst)

plt.xticks(p)
plt.xlabel("p")
plt.ylabel("average number of tests")
plt.title(
    "p vs average number of tests to clear (N=10000)")
plt.plot(p, np.array(total_test_lst), '.-c')
plt.savefig('images/1.c-1.png')

plt.clf()

ratio_lst = []
for i in total_test_lst:
    ratio_lst.append(i/10000)
plt.xlabel("p")
plt.ylabel("ratio of tests by Dorfman over indiviual")
plt.title(
    "p vs ratio of tests to clear by Dorfman over indiviual (N=10000)")
plt.plot(p, np.array(ratio_lst), '.-c')
plt.savefig('images/1.c-2.png')
