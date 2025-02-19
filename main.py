import pandas as pd
import matplotlib.pyplot as plt
import pypsa
import numpy as np

import data

terna_2022 = data.Terna()
network = pypsa.Network()

bus_name = "copper plate"

network.add("Bus", bus_name, v_nom=1.0)

network.snapshots=terna_2022.time
network.add("Load", "carico", bus=bus_name, p_set=terna_2022.consumo)
network.add("Generator", "ftv", bus=bus_name, p_set=terna_2022.gen_pv)


print(network.generators)

ax = network.loads_t.p_set.plot.line()
network.generators_t.p_set.plot.area(subplots=True, ax=ax)
ax.set_xlim(pd.Timestamp('2022-04-01'),pd.Timestamp('2022-04-15'))

plt.tight_layout()
plt.show()