from random import choice
import matplotlib.pyplot as plt

class RandomWalk(object): 
    def __init__(self):
        self.num_points = 5000
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self): 
        while len(self.x_values) < self.num_points: 
            x_distance = choice([0,1,2,3,4])
            x_direction = choice([1,-1])
            x_steps = x_direction * x_distance

            y_distance = choice([0,1,2,3,4])
            y_direction = choice([1,-1])
            y_steps = y_direction * y_distance

            if x_steps == 0 and y_steps == 0: 
                continue

            self.x_values.append(self.x_values[-1] + x_steps)
            self.y_values.append(self.y_values[-1] + y_steps)

if __name__ == "__main__":
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values,rw.y_values,s=15)
    plt.show()




