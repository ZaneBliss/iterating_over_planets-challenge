planet_list = ['Mercury', 'Mars']

planet_list.append('Neptune')
planet_list.append('Jupiter')
planet_list.extend(['Saturn', 'Uranus'])
planet_list.insert(-1, 'Earth')
planet_list.insert(-1, 'Venus')
planet_list.append('Pluto')
rocky_planets = planet_list[:4]
planet_list.__delitem__(-1)

spacecrafts = [
    ('Pioneer 10', 'Jupiter'),
    ('Pioneer 11', 'Saturn'),
    ('Voyager 2', 'Uranus'),
    ('Galileo', 'Neptune'),
    ('Ulysses', 'Jupiter'),
    ('New Horizons', 'Pluto')
]

for planet in planet_list:
    for spacecraft in spacecrafts:
        if spacecraft[1] == planet: 
            print(spacecraft[0])
    