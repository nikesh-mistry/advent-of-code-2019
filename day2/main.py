import numpy as np
import copy

def intcode_computer(input_list, overrides = {}):

    for k, v in overrides.items():
        input_list[k] = v

    for i in np.arange(0, len(input_list), 4):
        opcode = input_list[i]

        if opcode == 99:
            return input_list
        else:
            a = input_list[input_list[i + 1]]
            b = input_list[input_list[i + 2]]

            if opcode == 1:
                c = a + b
            elif opcode == 2:
                c = a * b
            else:
                raise Exception("Unrecognised opcode!")

            input_list[input_list[i + 3]] = c

    raise Exception("Escape condition not found!")

def perform(input, overrides):
    print("Input is:", input)
    print("Overrides are:", overrides)
    print("Output is:", intcode_computer(input, overrides=overrides))

# test_list = [1,9,10,3,2,3,11,0,99,30,40,50]
# perform(test_list)
# print("-------------")
# perform([1,0,0,0,99])
# print("-------------")
# perform([2,3,0,3,99])
# print("-------------")
# perform([2,4,4,5,99,0])
# print("-------------")
# perform([1,1,1,4,99,5,6,0,99])
# print("-------------")


master_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,10,31,35,2,6,35,39,1,39,13,
           43,1,43,9,47,2,47,10,51,1,5,51,55,1,55,10,59,2,59,6,63,2,6,63,67,1,5,67,71,2,9,71,75,1,75,6,79,1,6,79,
           83,2,83,9,87,2,87,13,91,1,10,91,95,1,95,13,99,2,13,99,103,1,103,10,107,2,107,10,111,1,111,9,115,1,115,
           2,119,1,9,119,0,99,2,0,14,0]

# TASK 1
print("------------------- TASK 1 -------------------")
input_1 = copy.deepcopy(master_input)
perform(input_1, overrides={1: 12, 2: 2})

# TASK 2
print("------------------- TASK 2 -------------------")
for i in np.arange(100):
    for j in np.arange(100):
        input = copy.deepcopy(master_input)
        output = intcode_computer(input, overrides={1: i, 2: j})
        if output[0] == 19690720:
            print("Input 1 (noun) is {}, input 2 (verb) is {}.".format(i, j))
            print((100 * i) + j)