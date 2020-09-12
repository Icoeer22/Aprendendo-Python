import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7,6,5,4,3,2,1]

plt.scatter(x,y)
plt.show()

x1 = np.arange(0,1000,1)
plt.plot(x1 , x1**2)
plt.show()