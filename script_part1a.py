#!/usr/bin/env python3
#Wed Mar 16 15:04:11 2022 +0100, 601cd27
# Sammy Jonsson, Nikolai Bakken, Aron Wristel
import numpy as np
import roadster
import matplotlib.pyplot as plt

speed_kmph = np.linspace(1., 200., 1000) # hastigheter jämnt fördelade intervallet 1, 200
consumption_Whpkm = roadster.consumption(speed_kmph) # stoppa in hastigheterna i consumption funk vi skrev i roadster

# plotta kurvan med matplotlib
fig, ax = plt.subplots()
ax.plot(speed_kmph, consumption_Whpkm)

ax.set(xlabel='speed (km/h)', ylabel='consumption (Whpkm)', title='Anna consumption')
ax.grid()

fig.savefig("consumption.png")
plt.show()


