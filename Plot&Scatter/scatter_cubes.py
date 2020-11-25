import matplotlib.pyplot as plt 

x_values = list(range(1,1001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,y_values,s=10,edgecolors='none',c=y_values,cmap=plt.cm.viridis)
plt.title('Cube Numbers',fontsize=24)
plt.xlabel('Values',fontsize=14)
plt.ylabel('Cubes',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.savefig('cubes_plot.png')