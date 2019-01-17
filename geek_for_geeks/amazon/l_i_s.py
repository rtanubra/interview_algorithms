"""
L_I_S
Longest Increasing Subsequence
Given a sequence, find the length of the longest increasing 
subsequence from a given sequence .
The longest increasing subsequence means to find a subsequence 
of a given sequence in which the subsequence's elements are in sorted order, 
lowest to highest, and in which the subsequence is as long as possible. 
This subsequence is not necessarily contiguous, or unique.
{ 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 3
"""

def lis(some_arr):
    lengths= []
    count = 0
    inner_count = count
    while count < len(some_arr):
        inner_count = count + 1
        curr_arr = [some_arr[count]] 
        while inner_count < len(some_arr):
            if some_arr[inner_count] > curr_arr[-1]:
                curr_arr.append(some_arr[inner_count])
            else:
                break
            inner_count += 1
        lengths.append(len(curr_arr))
        curr_arr = list([])
        count +=1 
    return max(lengths)

def run_test():
    inputs = [
        [10, 22, 9, 33, 21, 50, 41, 60, 80],[10, 22,-5, 9, 33, 34,21, 50, 41, 60, 80,90,100],[10,20,30,40,-5,9,10,-3],
        [2,3,4,-3,1,2,8,9,-9,0,2,3,-8],[-100,-10,-3,0,2,10,-8,50,90,-3],[3,-2,-4,10]
    ]
    outputs = [
        3,5,4,5,6,2
    ]
    passing = True
    for x in range(len(inputs)):
        obtained = lis(inputs[x])
        print(f"Test {x+1} {inputs[x]} expecting {outputs[x]} obtained {obtained}")
        if obtained != outputs[x]:
            print(f"Failed Test{x+1}")
            passing = False
            break
    if passing:
        print("PASSED")

run_test()
