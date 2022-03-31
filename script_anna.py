# script anna punkt
# Sammy Jonsson, Nikolai Bakken, Aron Wristel
import roadster
import matplotlib.pyplot as plt
import numpy as np

route = 'speed_anna.npz'
route_dist, route_speed = roadster.load_route(route)


# plotta som punktdiagram datan direkt ur speed_anna/elsa
plt.scatter(route_dist, route_speed)
plt.show()

