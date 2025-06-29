import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#read the csv
tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
pvflights = flights.pivot_table(values='passengers',index='month',columns='year')
iris = sns.load_dataset("iris")

#show the given no of rows
print(tips.head())

#create a histogram, kde(display the kernel density graph), bins(number of data points), for a single col only, bins = no. of bars on the graph
sns.displot(tips["total_bill"], kde=True, bins=30)

#create a jointplot xcord, ycord, data_set, kind of plot
#types of plots (scatter, hex, regression
sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")

#create plots with various combinations for numerical columns
#hue for categorical columns, palette for colour schemes
sns.pairplot(tips, hue="sex", palette="coolwarm")

#a | where the value exist
sns.rugplot(tips)

#barplot with catagerorical data on xcord and numeric values on y cord, data_set, estimator is the function to perform
sns.barplot(x="sex", y="total_bill", data=tips, estimator=np.mean)

#barplot with estimator as count
sns.countplot(x="sex", data=tips)

#creaet a boxplot
sns.boxplot(x="day", y="total_bill", data=tips, pallete="rainbow")

#create a violin plot
sns.violinplot(x="day", y="total_bill", data=tips, split=True, hue="sex", palette="Set1")

#create a strip plot
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1',split=True)

#create a swarmplot
sns.swarmplot(x="day", y="total_bill",hue='sex',data=tips, palette="Set1", split=True)

#create a heat map
sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1)

#create a clustermap
sns.clustermap(pvflights,cmap='coolwarm',standard_scale=1)

#get only the grid of the Pair Plot
g = sns.PairGrid(iris)
#display the given plots across the grid
g.map(plt.scatter)
#display the given plots on the diagonal of the grid
g.map_diag(plt.hist)
#display the given plots across the upper diagonal of the grid
g.map_upper(plt.scatter)
#display the given plots across the lower diagonal of the grid
g.map_lower(sns.kdeplot)

#make a custom grid using required cols of the df
#(data set, col to be shown vertically, col shown horizontally
g = sns.FacetGrid(tips, col="time", row="smoker", hue="sex")
#(tyoe of plot, col)
g = g.map(plt.scatter, "total_bill", "tips")

#Jointplot type of grids withe the two given plot types
j = sns.JointGrid(x="total_bill", y="tip", data=tips)
j = j.plot(sns.regplot, sns.distplot)

#create a regression plot
sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex", row="sex", col="time", palette="coolwarm", markers=['o', 'v'], scatter_kws={'s': 100}, aspect=0.6)

#set bg style for the plot
sns.set_style("white")
sns.set_style("ticks")

#set existence of spines for the plot
sns.despine(left=True, bottom=True, right=True, top=True)

#set figure size
plt.figure(figsize=(12,3))

#set scale type and size
sns.set_context("poster", font_scale=4)

plt.show()
