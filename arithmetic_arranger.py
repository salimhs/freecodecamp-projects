#Arithmetic Formatter FCC project
import math



def arithmetic_arranger(problems, display=False):
    
    #Seperating the problem into lists
    topLine = ""
    operator = ""
    bottomLine = ""
    lines = ""
    solution = ""

    #Checking for too many problems (Rule #1)
    if len(problems) > 5:
        return "Error: Too many problams."

    #Main function
    for problem in problems: 
        isolate = problem.split() #isolating everything into lists
        topLine = isolate[0]
        operator = isolate[1]
        bottomLine = isolate[2]

        #Checking if operand has a max of four digits in width & making sure they are numbers (Rule #3 & #4)
        if topLine.isdigit() and bottomLine.isdigit():
            if len(topLine) > 4 < len(bottomLine):
                return "Error: Numbers cannot be more than four digits"
            else:
                return "Error: Numbers must only contain digits."

    #Checking for operators (Rule #2)
    if operator != "+" and operator != "-":
        #return "Error: Operator must be '+' or '-'."






        return problems()

print(arithmetic_arranger["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
