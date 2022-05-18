# script part2c
# Sammy, Nikolai, Aron
# integral nummer (1), time_to_destination

import numpy as np
import roadster
import matplotlib.pyplot as plt

dist, speed = roadster.load_route('speed_anna.npz')
max_exponent = 22
l = [2**i for i in range(0, max_exponent)]

n_list = []
T = []
T_error = []

for e in l:
    time = roadster.time_to_destination(dist[-1], 'speed_anna.npz', e)
    T.append(time)
    
for i in range(len(T)-1):
    n_list.append(l[i+1])
    T_error.append(abs(T[i+1]-T[i]))
n_list = np.array(n_list)

O = [1/x for x in range(1, 2**max_exponent)]
P = [1/(x**2) for x in range(1, 2**max_exponent)]

fig, ax = plt.subplots()
plt.loglog(n_list ,T_error, label="Trapets integral 1")
plt.loglog(O, label="O(1/n)")
plt.loglog(P, label="O(1/n^2)")
plt.legend(loc="upper right")
ax.set(xlabel='n', ylabel='Integrationsfel', title='Konvergensstudie')
ax.grid()
fig.savefig("Konvergensstudie_2c.png")
plt.xlim(xmin=1)
plt.show()