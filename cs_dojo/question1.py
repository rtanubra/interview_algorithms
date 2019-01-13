"""
Facebook Coding Interview Question and Answer #1: All Subsets of a Set
https://www.youtube.com/watch?v=bGC2fNALbNU

Given an array of unique items:
find all unique subsets. 
of length =0 -> len(set)

Logic for My solution:
    iterate through the possible lengths of choices: (0 subset to len(subset) == len(set))
        iterate through the given array make these two decisions:
            1. Do we have to pickup based on how many more choices we have and what our desired lenght is
            2. Pickup or not pickup 

Logic for CS DOJO solution:
    iterate through given array:
        at each point make 2 choices:
            1. choose to select 
            2. choose not to select.
    thoughts here:
        
Thoughts going forward: can this be done through an iterative approach without recursion at all!
"""

def my_solution(given_array):
    initial_array = list(given_array)
    answers = [] #Build an answer list to compare my solution vs CS DOJO
    def recur_subset(given_array,chosen,index,curr_length=0):
        if len(chosen) == curr_length:
            answers.append(chosen)
            print(chosen)
        else:
            #Do I have to pickup? based on desired length of subset.
            if  curr_length - len(chosen) == len(given_array) - index:
                #I have to pickup
                recur_subset(given_array[:index]+given_array[index+1:],chosen+[given_array[index]],index,curr_length)
            else:
                #Pickup
                recur_subset(given_array[:index]+given_array[index+1:],chosen+[given_array[index]],index,curr_length)
                #Do not pickup
                recur_subset(given_array,chosen,index+1,curr_length)

    for x in range(len(initial_array)+1):
        recur_subset(given_array,[],0,x)   

def cs_dojo(given_array):
    #Expected solution
    print(f"Expected number of solutions is {2**len(given_array)}")
    answers = []

    def final_solver(some_arr):
        new_arr = []
        for x in some_arr:
            if x != None:
                new_arr.append(x)
        return new_arr

    def helper(given_array,subset,i):
        if i == len(given_array):
            true_answer = final_solver(subset)
            answers.append(true_answer)
            print(true_answer)
        else:
            #pickup
            helper(given_array,subset[:i]+[given_array[i]]+subset[i+1:],i+1)
            #Do not pickup
            helper(given_array,subset,i+1)
    helper(given_array,[None]*len(given_array),0)

##Use this to run
def run_solution(arr):
    print(f"Exploring {arr}")
    print(f"Expected Solution should have {2**len(arr)} possible sets including a 0 and full set")
    print("RUNNING REY'S SOLUTION")
    my_solution(arr)
    print("RUNNING CS DOJO SOLUTION")
    cs_dojo(arr)
    print("\n"*2)


##run these tests to see the differences
#run_solution([1,2,3])
#run_solution([1,2,3,4,5])
#run_solution([1,2])
