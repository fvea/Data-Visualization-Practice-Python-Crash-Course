import matplotlib.pyplot as plt 

from die import Die

print(plt.style.available)
# Create D6
die_1 = Die()
die_2 = Die()

# Roll D6 1000 times and store results to results(list).
results = [die_1.roll() + die_2.roll() for i in range(1000)] 
max_result = die_1.num_sides + die_2.num_sides


# Analyse the results.
frequency = [results.count(value) for value in range(2,max_result+1)]

# Visualize
plt.style.use('ggplot')

values = [value for value in range(2,max_result+1)]

plt.bar(values,frequency,label='D6 + D6',color='#0080FF')

plt.xlabel('Values')
plt.xticks(ticks=list(values),labels=values)
plt.ylabel('Frequency')
plt.title('Rolling 2 D6 1000 times.')

plt.legend()
plt.grid(True)
plt.tight_layout()


plt.show()




