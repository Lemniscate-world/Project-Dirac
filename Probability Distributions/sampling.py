import numpy as np

n = np.random.randint(0,10,10000)
h = np.bincount(n)
print(h)
h = h/h.sum()
print(h)

# Samples from a binomail distribution to simulate events with a known probability
t = np.random.binomial(5, 0.3, 1000)
s = np.bincount(t)
print(s)
s = s/s.sum()
print(s)

# With the bernoulli form, we can samplebinary outcomes, 0 or 1
t = np.random.binomial(1, 0.5, 10000)
s = np.bincount(t)
print(s)

# Poisson Distribution
t = np.random.poisson(5, 10000)
s = np.bincount(t)
print(s)
print(t.max())
s = s/s.sum()
print(s)