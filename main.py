def add(num_1, num_2, op):
    if op == 1:
        return f"{num_1} + {num_2} = {num_1 + num_2}"
    elif op == 2:
        return f"{num_1} - {num_2} = {num_1 - num_2}"
    elif op == 3:
        return f"{num_1} x {num_2} = {num_1 * num_2}"
    elif op == 4:
        return f"{num_1} / {num_2} = {num_1 / num_2}"
    else:
        return "\nERROR: Please select a valid operation."


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
o = int(input("\nChoose the operation:\n1-add   2-subtract\n3-multiply   4-divide\nEnter here: "))
result = add(x, y, o)
print(result)
