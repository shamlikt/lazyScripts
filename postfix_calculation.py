def get_input():
    expression = raw_input("\n>")
    return list(expression)

def super_pop(stack,index=2):
    value1 = stack.pop()
    value2 = stack.pop()
    return value1,value2,stack

def calculator(value1,value2,operator):
    if operator == "+":
        result =  value2 + value1
    elif operator == "-":
        result = value2 - value1
    elif operator == "*":
        result = value2 * value1
    elif operator == "/":
        result = value2 / value1
    return str(result)

def evaluator(expression):
    operand = "123456789"
    operator = "+-/*"
    stack = []
    for data in expression:
        if data in operand:
            stack.append(data)
        elif data in operator :
            value1,value2,stack = super_pop(stack)
            new_data = calculator(int(value1),int(value2),data)
            stack.append(new_data)
            
    return int(stack[0])

def repeater():
    print "Do you want type another expression ? \nYES \tNO"
    answer = get_input()
    if ''.join(answer) == "YES" :
        return False
    elif ''.join(answer) == "NO":
        return True 
    else :
        print "Command Not found !\n\n"
        repeater()


if __name__ == '__main__':
    while True:
        expression = get_input()
        print evaluator(expression)
        if repeater():
            break
    
    
