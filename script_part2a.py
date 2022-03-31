#script part2a
import roadster
import numpy as np

route_dist, route_speed = roadster.load_route('speed_anna.npz')
a = roadster.time_to_destination(65, 'speed_anna.npz', 1000)
print(a)

