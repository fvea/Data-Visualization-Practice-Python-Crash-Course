import matplotlib.pyplot as plt 

from rw import RandomWalk


while True:
    rw = RandomWalk() 
    rw.generate_data()
    plt.scatter(rw.x_values,rw.y_values)
    plt.show()

    keep_running = input("Keep running? (y/n): ")
    if keep_running == 'n': 
        break
    