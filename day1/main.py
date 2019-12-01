# NOTE below code is purely for speed of result
# quality/design of code may not be up to usual standards

def get_fuel(mass):
    x = (mass // 3) - 2
    return x

# below is test cases
test_cases = [12, 14, 1969, 100756]

fuel_required_for_components = []
with open("inputs_mass.txt", 'rb') as file:
    for line in file:
        mass = int(line)
        # print(mass)
        fuel = get_fuel(mass)

        fuel_required_for_components.append(fuel)

import numpy as np
print(np.sum(fuel_required_for_components))

def get_fuel_required_by_fuel(mass, count):
    additional_fuel = get_fuel(mass)

    if additional_fuel <= 0:
        return count
    else:
        count += additional_fuel
        return get_fuel_required_by_fuel(additional_fuel, count)

# for m in test_cases:
#     fuel = get_fuel(m)
#     print("Mass = {}, fuel = {}.".format(m, fuel))
#     extra_fuel = get_fuel_required_by_fuel(fuel, 0)
#     total_fuel = fuel + extra_fuel
#     print("Mass = {}, orig fuel = {}, total fuel = {}".format(m, fuel, total_fuel))

extra_fuel_per_component = []

for f in fuel_required_for_components:
    extra_fuel_required = get_fuel_required_by_fuel(f, 0)
    extra_fuel_per_component.append(extra_fuel_required)

combined_total_fuel = np.sum(fuel_required_for_components) + np.sum(extra_fuel_per_component)
print(combined_total_fuel)
