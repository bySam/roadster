#!/usr/bin/env python3
#Wed Mar 16 15:04:11 2022 +0100, 601cd27
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import route_nyc 

### Given contour plot ###
n_fine = 100
t_fine = np.linspace(0, 24, n_fine)
x_fine = np.linspace(0, 60, n_fine)
tt_fine, xx_fine = np.meshgrid(t_fine, x_fine)
zz_fine = route_nyc.route_nyc(tt_fine,xx_fine)
w, h = plt.figaspect(0.4)
fig = plt.figure(figsize=(w, h))
plt.axes().set_aspect(0.2, adjustable='box')
cs = plt.contourf(tt_fine,xx_fine,zz_fine, 50, cmap=cm.get_cmap('jet'))
plt.xlabel('Time [hour of day]',fontsize=18)
plt.ylabel('Distance [km]',fontsize=18)
plt.title('Speed [km/h]',fontsize=18)
fig.colorbar(cs)
plt.savefig("speed-data-nyc.eps", bbox_inches='tight')

time_h4, distance_km4, speed_kmph4 = route_nyc.nyc_route_traveler_euler(4, 0.01)
time_h9, distance_km9, speed_kmph9 = route_nyc.nyc_route_traveler_euler(9.5, 0.01)

plt.plot(time_h4, distance_km4, 'b--', linewidth = 3, label= 'Resan startar kl. 4')
plt.plot(time_h9, distance_km9, 'g-.', linewidth = 3, label= 'Resan startar kl. 9.30')
