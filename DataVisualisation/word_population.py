import json

from pygal.maps.world import COUNTRIES
from pygal.maps.world import World
from pygal.style import RotateStyle

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None


filename = 'population_data.json'


with open(filename) as f:
    pop_data = json.load(f)

cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float((pop_dict['Value'])))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population

cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{},

for cc, pop in cc_population.items():
    if pop <10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RotateStyle('#336699')
wm = World(style = wm_style)
wm.force_uri_protocol = "http"
wm.title = "World population in 2010 (for particular countries)"
wm.add("0 - 10 mln", cc_pops_1)
wm.add("10 mln - 1 mld", cc_pops_2)
wm.add(" > 1 mld", cc_pops_3)
wm.render_to_file('world__population.svg')