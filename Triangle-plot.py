import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
pts = np.array([[1,7], [2,4], [6,1]])
p = Polygon(pts, closed=False)
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(1,7)
ax.set_ylim(1,8)
plt.show()