import math
import numpy as np
import matplotlib.pyplot as plt


def true_function(x):
    """
    >>> true_function(0)
    0.0
    """
    y = math.sin(math.pi * x * 0.8) * 10 
    return y


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
time = np.arange(-1,1,0.1)
y = [true_function(xi) for xi in time] 

plt.plot(time,y)
plt.show()
    
