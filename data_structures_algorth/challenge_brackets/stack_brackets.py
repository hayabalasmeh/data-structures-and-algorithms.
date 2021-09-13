

from data_structures_algorth.challenge_stack_and_queue.stack_queue import Stack
# from data_structures_algorth.challenge_brackets.stack_brackets

def brackets_checker(test:str):
   
    checker = Stack()
    round=["(",")"] 
    curly= ["{","}"]
    square= ["[","]"]
    for bracket in test:
        if bracket == '{' or bracket == '(' or bracket == "[":
           checker.push(bracket)
    
        elif bracket == ')' or bracket == "]" or bracket == "}":
            """in case the test started with closing then we will check if the stack is empty then this is unbalanced"""
            if checker.is_empty():
                return False
            elif bracket in round and checker.top.value in round:
                checker.pop()
            elif bracket in curly and checker.top.value in curly :
                checker.pop()
            elif bracket in square and checker.top.value in square:
                checker.pop()
            else:
                return False
    if checker.is_empty():
        return True
    else:
        return False

if __name__ == "__main__" :
    
    print(brackets_checker('{faop,}'))
    if 'h' in ['u','[']:
        print('fffffffff')
    




