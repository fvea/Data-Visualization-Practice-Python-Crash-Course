import matplotlib.pyplot as plt 

plt.style.use('fivethirtyeight')

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,edgecolor='none',s=10,c=y_values,cmap=plt.cm.viridis)
# Set chart title and label axes.
plt.title('Square Numbers', fontsize=14)
plt.xlabel('Values',fontsize=8)
plt.ylabel('Squares',fontsize=8)
# Set size of tick labels.
plt.tick_params(axis='both',which='major',labelsize=8)
# Set the range for each axis.
plt.axis([0,1100,0,1100000])
plt.show()
plt.tight_layout()
#plt.savefig('squares_plot.png')