"""
Problem 2 (easy)
        Highest power of 2 less than or equal to given number
        Given a number n, find the highest power of 2 that 
        is smaller than or equal to n.
https://www.geeksforgeeks.org/highest-power-2-less-equal-given-number/
"""

def problem2(number):
    if number <= 0:
        return "Please provide input greater than 0"
    elif number == 1:
        return 1
    else:
        answer = 2
        count =2
        while 2 ** count <= number:
            answer = 2 ** count
            count +=1 
    return answer

#==============================RUN TESTS==============================
def run_test():
    inputs = [
        12,18,68,2,64,1,0,
        2048,3000,8192,10000
    ]
    outputs = [
        8,16,64,2,64,1,"Please provide input greater than 0",
        2048,2048,8192,8192
    ]
    for i,x in enumerate(inputs):
        obtained = problem2(x)
        passing= "False"
        if obtained == outputs[i]:
            passing = "Passed"
        print(f"Testing {x}, expected {outputs[i]}, obtained {obtained}")
        print(f"Test number {i+1} result {passing}")
        if passing == "False":
            break

run_test()