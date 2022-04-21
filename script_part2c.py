# script part2c
# Sammy, Nikolai, Aron
# integral nummer (1), time_to_destination

import numpy as np
import roadster
import matplotlib.pyplot as plt

route_dist, route_speed = roadster.load_route('speed_elsa.npz')

delintervall = 25
l = [2**i for i in range(0,delintervall)]

trapets_list = []
for num in l:
    a = roadster.time_to_destination(route_dist[-1], 'speed_elsa.npz', num)
    trapets_list.append(a)
trap_list_dif = []
for i in range(len(trapets_list)-1):
    trap_list_dif.append(abs(trapets_list[i+1]-trapets_list[i]))

x = np.array(l)
O = 1/(x**2) # hjälpinjer
P = 1/(x)

#plotta kurva i loglog
x_axis = range(1, len(x))
fig, ax = plt.subplots()
plt.loglog(x_axis ,trap_list_dif, label="Trapets integral 1")
ax.loglog(O, label="O(1/n^2)")
ax.loglog(P, label="O(1/n)")
plt.legend(loc="upper right")

ax.set(xlabel='Antal delinterval', ylabel='Integrationsfel', title='Konvergensstudie')
ax.grid()

fig.savefig("Konvergensstudie_2c.png")
plt.xlim(xmin=1)
plt.show()
