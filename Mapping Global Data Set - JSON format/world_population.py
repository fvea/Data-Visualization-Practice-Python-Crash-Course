import json 

import pygal
from pygal.style import * 

from country_code import get_country_code

# Load the data into a list(pop_data).
filename = 'population_data.json'
with open(filename) as f: 
    pop_data = json.load(f)

# Build a dictionary of population data(cc_populations).
cc_populations = {}
for pop_dict in pop_data: 
    if pop_dict['Year'] == '2010': 
        country_name = pop_dict['Country Name']
        population =  int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code: 
            cc_populations[code] = population


# Group populations into 3 population levels.
cc_pop1, cc_pop2, cc_pop3 = {},{},{}
for cc,pop in cc_populations.items(): 
    if pop < 1e7: 
        cc_pop1[cc] = pop # Population less than 10 million.
    elif pop < 1e9: 
        cc_pop2[cc] = pop # Population between 10 million and 1 billion.
    else: 
        cc_pop3[cc] = pop # Greater than 1 billion.

# See how many countries in each level.
print(len(cc_pop1), len(cc_pop2), len(cc_pop3))

# Create a World Map / Visualize Populations by Country.
wm_style = LightenStyle('#336676', step=10)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population 2010, by Country'
wm.add('>1bn', cc_pop3)
wm.add('10m-1bn', cc_pop2)
wm.add('0-10m', cc_pop1)


if __name__ == "__main__":
    wm.render_to_file('world_population.svg')


