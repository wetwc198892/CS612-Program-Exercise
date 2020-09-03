import numpy as np
nwalks = 5000
nsteps = 1000
np.random.seed(1234)
steps = np.random.normal(loc=0, scale=0.25, size=(nwalks, nsteps))
steps = np.where(steps>=0, 1, -1)
walks = steps.cumsum(1)
hit50 = (walks<=-50).any(1)
print(hit50.sum())
crossing_times = (walks[hit50] <= -50).argmax(1)
print(crossing_times.mean())