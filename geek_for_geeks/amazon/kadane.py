"""
Kadane Algorithm: LEVEL MEDIUM

Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

egs 
1,2,3,-2,5 --> 9
-1,-2,-3,-4--> -1
1,2,3,-5,10,12 -> 22
"""

def kad(some_arr):
    my_sums = []
    arrs = []
    i=0
    while i < len(some_arr):
        for x in range(1,len(some_arr)+1):
            arrs.append(some_arr[i:i+x])
            my_sums.append(sum(some_arr[i:i+x]))
        i+=1
    #print(f"Max obtained is: {max(my_sums)}, from {arrs[my_sums.index(max(my_sums))]}")
    if len(my_sums) == 0:
        return 0
    return max(my_sums)
    

def test_fx():
    inputs = [
        [1,2,3,-2,5],[1,2,3,-10,10,12],[-1,-2,-3,-4],[1,2,3,-5,10,12],[2],[]
    ]
    outputs = [
        9,22,-1,23,2,0
    ]
    for x in range(len(inputs)):
        expected = outputs[x]
        obtained = kad(inputs[x])
        print(f"Test #{x+1} {inputs[x]}, expecting {outputs[x]}")
        if expected == obtained:
            print("pass")
        else:
            print(f"failed test number {x+1}")
            print(f"Obtained {obtained}, instead of {expected}")
            break
    

test_fx()