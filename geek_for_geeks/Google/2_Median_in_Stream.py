"""
Problem 2: HARD - semicomplete. (using numpy FULL COMPLETE)
Median in steam 

Given an input stream of N integers the task is to insert integers to stream and
print the median of the new stream 
formed by each insertion of X to the stream
EG
5, 15, 1, 3 shoulr return 5,10,5,4

For each element added to the stream print the 
        floor of the new median in a new line.

Thoughts:
    -Not sure what the task here is. 
    -Seems if we are using numpy median method we have a quick and efficient way to find this.
    -If the goal is not to use that, well then we have a process that takes quite some time to complete.
"""
import numpy as np
import time
import random
#================Helper function to add a number in an ordered fashion==============
def add_to_array(some_arr, number):
    index = 0
    while index < len(some_arr) and some_arr[index] < number:
        if some_arr[index] >= number:
            break
        index+=1 
    some_arr.insert(index,number)
    return some_arr

#================Helper function to find the floored median of a list==============
def find_median(some_arr):
    if len(some_arr) % 2 == 0:
        half = int(len(some_arr) / 2)
        small_number = some_arr[half-1]
        large_number = some_arr[half]
        return int((small_number+large_number)/2)
        
    else:
        half = int(len(some_arr)/2)
        return some_arr[half]

#==========Main function using self implementation of median and sort in stream ========
def problem2(given_arr):
    start = time.time()
    my_arr = [given_arr[0]]
    medians = [given_arr[0]]
    count = 1
    if len(given_arr) ==1:
        return medians
    else:
        while count < len(given_arr):
            my_arr = add_to_array(my_arr,given_arr[count])
            medians.append(find_median(my_arr))
            count += 1

    #==visual inspection==Delete to save===
    """
    print("Visual Inspection:")
    for i,x in enumerate(medians):
        print(f"Median of: {given_arr[:i+1]}")
        obtained = x 
        print(x)
    """
    end = time.time()
    print(f"Completed in {end-start}")
    return medians

def tester(given_arr):
    start = time.time()
    medians = []
    count = 0
    while count < len(given_arr):
        medians.append(int(np.median(given_arr[:count+1])))
        count += 1
    end= time.time()
    print(f"Tester completed in {end-start}")
    return medians


def run_tests():
    input_lengths = [3,6,8,100,1000,10000,20000]
    inputs = []
    outputs = []

    def create_random_numbers(length):
        stream = []
        for x in range(length):
            stream.append(random.randint(1,100000))
        return stream
    
    for x in input_lengths:
        curr_input = create_random_numbers(x)
        inputs.append(curr_input)
        outputs.append(str(tester(curr_input)))

    for i,x in enumerate(inputs):
        print(f"Test {i+1}/{len(inputs)}, input length {len(x)}")
        expected = outputs[i]
        obtained = str(problem2(x))
        if expected == obtained:
            print(f"Passed test {i+1}/{len(inputs)}")
        else:
            print(f"Failed test {i+1}")
            break
 
run_tests()

    



    