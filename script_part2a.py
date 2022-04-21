#script part2a, Sammy, Nikolai, Aron
import roadster
import numpy as np

route_dist, route_speed = roadster.load_route('speed_elsa.npz')
distans = route_dist[-1]
a = roadster.time_to_destination(distans, 'speed_elsa.npz', 10000)
print('Det tog', a * 60, 'minuter att köra', distans, 'km')
