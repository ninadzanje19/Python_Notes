"""#################################Mathplotlib Notes###############################################"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

print(x)
print(y)

"""#Functional Method
#create a plot(x cord, y cord)
plt.plot(x, y)
#labels to the cords
plt.xlabel("X Label")
plt.ylabel("Y Label")

#title to the plot
plt.title("Matplotlib")

#create a subplot on the canvas(no. of rows, no. of cols, no. of plot)
plt.subplot(1, 2, 1)

#final arg is the colour of the plot
plt.plot(x, y, 'r')

plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')
"""

#Object Oriented Method
#create a plot object
fig = plt.figure()

#add axis [%from bottom, %from left, %height, %widthh
#axes is the actual graph whereas figure is the canvas
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

#create the plot
"""axes.plot(x, y)"""

#set title for the plot
axes.set_title("Matplotlib")

#create a figure object and array of axes object
fig, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(x, y)
axes[0].set_title("First Plot")

axes[1].plot(y, x, color="#0000FF", alpha=0.5, lw=0.5, ls="-", marker="+", markersize=8, markerfacecolor="red", markeredgewidth=3, markeredgecolor="green")
axes[1].set_title("Second Plot")

#change the figure size
"""fig_size = plt.figure(figsize=(8, 2))
ax = fig_size.add_axes([0, 0, 1, 1])
ax.plot(x, x**2, labels="x ** 2")
ax.plot(x, x**3, labels="x ** 4")

#diplay legend(content in the labels attribute
ax.legend()"""
#diplay's neatly
plt.tight_layout()

#save the figure, more dpi = more quality
"""fig.savefig("my_plot.png", dpi=200)"""

#display the plot
plt.show()