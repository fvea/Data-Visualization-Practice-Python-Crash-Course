import matplotlib.pyplot as plt 

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(5000) 
    rw.fill_walks()

    # Set the size of the plotting window.
    plt.figure(figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,s=15,c=point_numbers,cmap=plt.cm.Blues,
        edgecolors='none')

    # Emphasize the first and last points.
    plt.scatter(0,0,s=50,c='green',edgecolors='none')
    plt.scatter(rw.x_values[-1],rw.y_values[-1],s=50,c='red',edgecolors='none')

    # Remove the axes.
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Keep running? (y/n): ")
    if keep_running == 'n': 
        break