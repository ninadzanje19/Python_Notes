import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv('df1',index_col=0)
df2 = pd.read_csv('df2')

#style for plot
plt.style.use("ggplot")
plt.style.use("fivethirtyeight")
plt.style.use("bmh")
plt.style.use("dark_background")
df1['A'].hist()

#create area plot with custom alpha
df2.plot.area(alpha=0.4)

#create bar plot, if stacked=True the bars will be stacked for diff cols
df2.plot.bar()
df2.plot.bar(stacked=True)

#create a histogram with no. of bins can be given
df1['A'].plot.hist(bins=50)

#create line graph with figure size and line width
df1.plot.line(x=df1.index,y='B',figsize=(12,3),lw=1)

#create scatetr plot(s = size, cmap= colour)
df1.plot.scatter(x='A',y='B',s=df1['C']*200, cmap="coolwarm")

#create box plot
df2.plot.box()

#create hex plot
df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df.plot.hexbin(x='a',y='b',gridsize=25,cmap='Oranges')

#create kde plot for one col
df2['a'].plot.kde()

#create kde plot for all cols
df2.plot.density()

plt.show()
