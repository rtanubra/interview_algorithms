"""
Problem 1 (easy)
Replace every element with the greatest element on the right side
Given an array of integers, 
        replace every element with the next greatest element
        (greatest element on the right side) in the array. 
        Since there is no element next to the last element, 
        replace it with -1. For example, 
        if the array is {16, 17, 4, 3, 5, 2}, 
        then it should be modified to {17, 5, 5, 5, 2, -1}.
https://www.geeksforgeeks.org/replace-every-element-with-the-greatest-on-right-side/
"""
def p1(arr):
    count = len(arr)-1
    new_arr = [None]*len(arr) #Build an array of None equal length
    if len(arr) >= 1:
        new_arr[count]= -1
        count -= 1
    else:
        return []
    while count >= 0:
        new_arr[count] = max(arr[count+1:])
        count -=1
    return new_arr
#==========HELPER TEST FUNCTION TO COMPARE EXPECTED ARR TO NEW ARR ==========
def compare_arr(arr_1,arr_2):
    if len(set(arr_1)) != len(set(arr_2)):
        return False
    else:
        set_1 = list(set(arr_1))
        for x in set_1:
            if arr_1.count(x) != arr_2.count(x):
                return False
    return True

#==========Run Testing ==========
def run_tests():
    inputs = [
        [16,17,4,3,5,2],
        [8,2,5,81,9,3],
        [],
        [56],[80],[13],
        [32,4,9,0,12,23,5,3]
    ]
    outputs = [
        [17,5,5,5,2,-1],
        [81,81,81,9,3,-1],
        [],
        [-1],[-1],[-1],
        [23,23,23,23,23,5,3,-1]
    ]
    for i,x in enumerate(inputs):
        obtained = p1(x)
        if compare_arr(outputs[i],obtained)==True:
            passing = "Pass"
        else:
            passing = "Failed"
        print(f"TESTING {x}")
        print(f"Test Number {i+1} result {passing}")
        if passing == "Failed":
            break

run_tests()