# Sammy Jonsson, Nikolai Bakken, Aron Wristel
import roadster
import matplotlib.pyplot as plt
import numpy as np

route = 'speed_anna.npz' # ändra till elsa eller anna beroende på behov
route_dist, route_speed = roadster.load_route(route) # unpacka arrayerna i speed_anna/elsa.npz
route_last = route_dist[-1] # sista elementet i distansarrayen, totala sträckan hon skrev
route_dist = np.linspace(0, route_last, 10000) # array intervallet 0, route_last, 100 000 punkter
route_speed = roadster.velocity(route_dist, 'speed_anna.npz') # kalla velocity passera in totala sträckan
# och speed_anna.npz, interpolerar på fler punkter för att få en utjämnad kurva

# plotta kurvan
fig, ax = plt.subplots()
ax.plot(route_dist, route_speed)
ax.set(xlabel='disance (km)', ylabel='speed (km/h)', title='Route Anna')
ax.grid()
fig.savefig("Route data.png")
plt.show()
