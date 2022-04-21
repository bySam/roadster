#script part2b, Sammy, Nikolai, Aron

import roadster
import numpy as np

route_dist, route_speed = roadster.load_route('speed_anna.npz')
distans = route_dist[-1]
a = roadster.total_consumption(distans, 'speed_anna.npz', 10000)
print('Annas bil tog', a, 'wattimmar att köra', distans, 'km')
