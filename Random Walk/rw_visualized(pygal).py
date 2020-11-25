import pygal

from pygal.style import DarkColorizedStyle

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walks()

dark_colorized_style = DarkColorizedStyle()
scatter = pygal.XY(stroke=False,style=dark_colorized_style)
scatter.add('Random Walk',list(zip(rw.x_values,rw.y_values)))
scatter.add('Start',[(0,0)])
scatter.add('End', [(rw.x_values[-1], rw.y_values[-1])])
scatter.render_to_file('rw.svg')