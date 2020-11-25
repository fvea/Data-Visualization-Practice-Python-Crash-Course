import pygal

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = [] 
for roll_num in range(1000): 
    results.append(die.roll())

#Analyze the Result.
frequencies = [] 
for value in range(1,die.num_sides+1): 
    frequencies.append(results.count(value))

#print(*frequencies, sep=' ')

# Visualize the Results. 
hist = pygal.Bar()

hist.title = 'Results of rolling D6 1000 times.'
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = 'Result'
hist.y_title = 'Frequency'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')