from random import choice
import matplotlib.pyplot as plt

class RandomWalk(object): 
    """A class to generate random walks."""
    def __init__(self,num_points = 5000): 
        """Initialize attributes of a walk."""
        self.num_points = num_points
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        x_direction = choice([1,-1])
        x_distance = choice([0,1,2,3,4])
        x_step = x_direction * x_distance

        y_direction = choice([1,-1])
        y_distance = choice([0,1,2,3,4])
        y_step = y_direction * y_distance

        return (x_step,y_step)


    def fill_walks(self):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            x_step,y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0: 
                continue
        
            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

if __name__ == "__main__":
     # Make a random walk, and plot the points.
    rw = RandomWalk(5000) 
    rw.fill_walks()

    # Set the size of the plotting window.
    plt.figure(figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,s=15,c=point_numbers,cmap=plt.cm.Blues,
        edgecolors='none')

    # Emphasize the first and last points.
    plt.scatter(0,0,s=15,c='green',edgecolors='none')
    plt.scatter(rw.x_values[-1],rw.y_values[-1],s=15,c='red',edgecolors='none')

    # Remove the axes.
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.show()
