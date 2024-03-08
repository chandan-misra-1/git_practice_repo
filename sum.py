import numpy as np
from scipy.stats import skew
x = np.random.normal(0, 2, 10000)
 # create random values based on a normal distribution
print(x)
x=45
y=93
print(skew(x))
