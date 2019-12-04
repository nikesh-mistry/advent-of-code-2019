import numpy as np

class Wire:

    def __init__(self, directions):
        self.coords = [(0,0)]

        self.apply_travel(directions)


    def apply_travel(self, directions):
        len_steps = len(directions)
        for counter, movement in enumerate(directions):
            if counter % 10 == 0:
                print(f"Step {counter} / {len_steps}")
            curr_x, curr_y = self.coords[-1]
            magnitude = int(movement[1:])
            if movement[0] == 'U':
                new_y = curr_y + magnitude
                for y in np.arange(curr_y + 1, new_y + 1, 1):
                    self.coords.append((curr_x, y))
            elif movement[0] == 'D':
                new_y = curr_y - magnitude
                for y in np.arange(curr_y - 1, new_y - 1, -1):
                    self.coords.append((curr_x, y))
            elif movement[0] == 'R':
                new_x = curr_x + magnitude
                for x in np.arange(curr_x + 1, new_x + 1, 1):
                    self.coords.append((x, curr_y))
            elif movement[0] == 'L':
                new_x = curr_x - magnitude
                for x in np.arange(curr_x - 1, new_x - 1, -1):
                    self.coords.append((x, curr_y))
            else:
                raise Exception("Unrecognised!")

    def get_coords(self):
        return self.coords

def find_crosses(wire_a, wire_b):
    coords_a = wire_a.get_coords()
    coords_b = wire_b.get_coords()

    return [i for i in coords_a if (i in coords_b) and (i != (0,0))]

def coords_to_distances(coords):
    return [abs(i[0]) + abs(i[1]) for i in coords]


with open("test.txt", 'r') as file:
    wires = {}
    for counter, line in enumerate(file):
        line_strip = str(line.strip())
        directions = [i for i in line_strip.split(",")]

        wires[counter] = directions

    wire_a = Wire(wires[0])
    wire_b = Wire(wires[1])

    print("Wires initialised.")
    print("Looking for crosses.")

    # find_crosses is inefficient, comment out below and replace with below crosses variable for quicker analysis
    crosses = find_crosses(wire_a, wire_b)
    print(wire_a.get_coords())
    print(wire_b.get_coords())
    print(crosses)

    # Below is crosses saved from previous run - useful when want to save time as find_crosses is inefficient
    # crosses = [(998, 349), (1211, 367), (1421, 367), (1733, 389), (1733, 417), (1733, 823), (1752, 1293), (1756, 1422), (1756, 1502), (1756, 1665), (1851, 1750), (1968, 1750), (2018, 1502), (2018, 1422), (1851, 1277), (1752, 1277), (1665, 1502), (1330, 1519), (1236, 1519), (735, 1747), (735, 1795), (1634, 1857), (1634, 1665), (1634, 1502), (1330, 1457), (831, 1747), (831, 1795), (1773, 1857), (1773, 1665), (1773, 1502), (1773, 1422), (1851, 1283), (2038, 1068), (2038, 823), (1832, 823), (1752, 1362), (1330, 1362), (1266, 1502), (1266, 1857), (76, 1747), (52, 1747), (-1361, 1087), (-998, 798), (-804, 611), (-998, 27), (-1838, 493), (-457, 949), (-457, 894), (-605, 561), (-743, 561), (-998, 561), (-1051, 561), (-1508, 1141), (-1568, 668), (-1978, 619), (-1544, 829), (-1118, 493), (-998, 233), (-743, 233), (-605, 154), (-67, 154), (257, 218), (257, 763), (257, 946), (108, 977), (-138, 977), (-201, 1945), (-125, 1747), (108, 1596), (531, 1747), (531, 1795), (264, 1795), (264, 1747), (365, 1747), (365, 1795), (166, 1795), (166, 1747), (267, 1747), (108, 1779), (-201, 1779), (-369, 1977)]

    # TASK 1
    distances = coords_to_distances(crosses)
    print(min(distances))

    # TASK 2
    sum_of_steps_for_intersection = []
    for c in crosses:
        n1 = wire_a.get_coords().index(c)
        n2 = wire_b.get_coords().index(c)

        sum_of_steps_for_intersection.append(n1+n2)
    print(sum_of_steps_for_intersection)
    print(min(sum_of_steps_for_intersection))

    print("Finished.")