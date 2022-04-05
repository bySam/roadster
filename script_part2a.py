#script part2a
import roadster
import numpy as np

route_dist, route_speed = roadster.load_route('speed_elsa.npz')
#a = roadster.time_to_destination(10, 'speed_anna.npz', 10)
a = roadster.total_consumption(65,"speed_anna.npz",10000)
print(a)

