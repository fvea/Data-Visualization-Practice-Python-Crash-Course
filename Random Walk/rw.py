from random import choice
import matplotlib.pyplot as plt 

class RandomWalk(object): 
    def __init__(self):
        self.nums = 5000
        self.x_values = [0]
        self.y_values = [0]

    def generate_data(self): 
        while len(self.x_values) < self.nums:
            x_distance = choice([0,1,2,3,4]) 
            x_direction = choice([1,-1])
            x_step = x_direction * x_distance

            y_distance = choice([0,1,2,3,4])
            y_direction = choice([1,-1])
            y_step = y_direction * y_distance

            if y_step == 0 and x_step == 0: 
                continue

            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)

if __name__ == "__main__":
    rw = RandomWalk()
    rw.generate_data()
    plt.scatter(rw.x_values,rw.y_values,s=15)
    plt.show()


     

