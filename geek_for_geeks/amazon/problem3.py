"""
Problem 3
3. Given a binary string, count number of substrings that start and end with 1
        Given a binary string, count number of substrings that
        start and end with 1. For example, if the input string 
        is “00100101”, then there are three substrings “1001”,
        “100101” and “101”.

iterate through the string everytime we see a 1
    -do a count ahead see how many 1s there are in front of it.
    -Add that number to options.
        -print each possibility
"""
def iterative_approach(substring,index,item):
    count = 1
    while index > 0 and count < len(substring):
        if substring[count] == item:
            index -= 1
            if index == 0:
                return substring[:count+1]
        count +=1
        

def problem3(some_string):
    count = 0 
    substrings = []
    print("Printing: possibilities")
    for i,x in enumerate(some_string):
        if x == "1" and i < len(some_string)-1:
            count += some_string[i+1:].count("1")
            #========Looking for each substring#========
            counter = 0 
            while counter < some_string[i+1:].count("1"):
                curr_substirng = iterative_approach(some_string[i:],counter+1,"1")
                print(curr_substirng)
                substrings.append(curr_substirng)
                counter += 1
            #========Looking for each substring#========
    return count

def run_test():
    inputs = [
        "00100101","00100101100101","0110","1010000000",
        "100","00001000000"
    ]
    outputs = [
        3,15,1,1,
        0,0
    ]
    passing = True
    for x in range(len(inputs)):
        print(f"\nTest Number {x+1} input binary: {inputs[x]}")
        obtained=problem3(inputs[x]) 
        print(f"Expected {outputs[x]}, obtained {obtained}")
        if outputs[x] == obtained:
            print(f"Passed test {x+1} out of {len(inputs)}")
        else:
            print(f"Failed test {x+1}.-Try again")
            break

run_test()
