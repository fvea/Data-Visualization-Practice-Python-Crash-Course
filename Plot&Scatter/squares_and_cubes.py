import matplotlib.pyplot as plt 

plt.style.use('ggplot')

x_values = list(range(1,6))
square_values = [x ** 2 for x in x_values]
cube_values = [x ** 3 for x in x_values]

plt.plot(x_values,square_values,label='Squares',marker='.')
plt.plot(x_values,cube_values,label='Cubes',marker='o')

plt.xlabel('Values')
plt.ylabel('Squares and Cubes')
plt.title('Squares and Cubes of Numbers (1-5)')
#plt.grid(True)
plt.legend()
plt.tight_layout()
plt.axis([0,6,0,130])
plt.show()
