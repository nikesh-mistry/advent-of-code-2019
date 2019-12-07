import numpy as np

orbits = []
with open("input_test.txt", 'r') as file:
    for line in file:
        orbits.append(line.strip())

planetary_orbits = {}
planetary_orbits_rev = {}

for orbit in orbits:
    orbited, orbiter = orbit.split(")")
    planetary_orbits[orbiter] = orbited
    planetary_orbits_rev[orbited] = orbiter

# TASK 1

def get_num_orbits_from_centre(orbiter, planetary_orbits):
    # for orbiter in planetary_orbits:
    if orbiter == "COM":
        return 0
    else:
        orbited = planetary_orbits[orbiter]
        distance = get_num_orbits_from_centre(orbited, planetary_orbits) + 1
        return distance

orbit_generations = [get_num_orbits_from_centre(planet, planetary_orbits) for planet in planetary_orbits]
print(np.sum(orbit_generations))

# TASK 2
class Planet:
    def __init__(self):
        self.neighbours = []

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

planet_objects = {}
for orbiter in planetary_orbits:
    orbited = planetary_orbits[orbiter]

    if orbiter not in planet_objects:
        planet_objects[orbiter] = Planet()
    if orbited not in planet_objects:
        planet_objects[orbited] = Planet()
    planet_objects[orbiter].add_neighbour(orbited)
    planet_objects[orbited].add_neighbour(orbiter)

def find_planetary_separation(sources, target, planet_objects, already_found=set(), distance_counter=1):
    new_planets = []
    already_found.update(sources)
    for source in sources:
        for neighbour in planet_objects[source].neighbours:
            if neighbour not in already_found:
                new_planets.append(neighbour)
    if target in new_planets:
        return distance_counter
    else:
        already_found.update(new_planets)
        return find_planetary_separation(new_planets, target, planet_objects, already_found, distance_counter + 1)

sep = find_planetary_separation(["YOU"], "SAN", planet_objects)

# adding manual minus 2 factor due to definition of distance not including beginning and final orbital
print(sep - 2)
