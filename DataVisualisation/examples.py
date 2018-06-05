from random import choice, randint

import pygal


class RandomWalk:
    def __init__(self, num_points=50000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice((1, -1))
            x_distance = choice((0, 1, 2, 3, 4))
            x_step = x_direction * x_distance
            y_direction = choice((1, -1))
            y_distance = choice((0, 1, 2, 3, 4))
            y_step = y_direction * y_distance
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


# rw = RandomWalk()
# rw.fill_walk()
# point_numbers = list(range(rw.num_points))
# plt.figure(figsize=(10,6))
# plt.scatter(rw.x_values,rw.y_values, c= point_numbers, cmap=plt.cm.Blues,edgecolors='none',s=1)
#
#
# plt.scatter(0,0, c= 'green', s = 100)
# plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

#
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)
#
# plt.show()

"""y = [random.randint(0,100) for x in range(100000)]
x = [random.randint(0,100) for z in range(100000)]

plt.scatter(x,y, edgecolors='none', s=30)
plt.axis([0,100,0,100])
plt.show()"""


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


die = Die()

results = [die.roll() for x in range(10000)]
frequencies = [results.count(value) for value in range(1, 7)]

hist = pygal.Bar()
hist.force_uri_protocol = 'http'
hist.labels = "Wynik"
hist.x_title = "Wynik"
hist._y_title = "Czestotliwosc"
hist.add("D6", frequencies)
hist.render_to_file('die_visual.svg')


# wm = World()
# wm.force_uri_protocol = 'http'
# wm.title = " North, Central and South America"
#
# wm.add("North America",['ca', 'mx', 'us'])
# wm.add("Central America", ['bz', 'cr','gt','hn', 'ni', 'pa', 'sv'])
# wm.add("South America", ['ar','bo','br','cl', 'co', 'ec','gf','gy','pe','py','sr','uy','ve'])
# wm.render_to_file('americas.svg')

# wm = World()
# wm.force_uri_protocol = "http"
# wm.title = "Population in North America's countries"
# wm.add("North America", {'ca': 43126000, 'mx': 13423000, 'us': 309349000})
# wm.render_to_file('na_population.svg')