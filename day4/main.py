import numpy as np

def check_number_string(number_string):
    number_string = str(number_string)

    if len(number_string) != 6:
        return False

    consecutive_match = False

    no_match_indices = []
    for i in np.arange(0, len(number_string) -1):
        if number_string[i] == number_string[i + 1]:
            # consecutive_match = True # TOGGLE THIS FOR PART 1
            # following if statement is for part 2 ONLY!!!
            if (i + 2) < len(number_string):
                if number_string[i + 1] == number_string[i + 2]:
                    no_match_indices.append(i + 1)
                else:
                    # i.e. consecutive numbers not part of larger group
                    if i not in no_match_indices:
                        consecutive_match = True
            else:
                if i not in no_match_indices:
                    consecutive_match = True
        if number_string[i] > number_string[i+1]:
            return False

    if not consecutive_match:
        return False
    return True

counter = 0
for num in np.arange(134792, 675810 + 1):
    if check_number_string(num):
        counter += 1
print(counter)