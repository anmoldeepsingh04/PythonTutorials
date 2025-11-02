n = 15
m = 7
ans1 = n+m
# print("Addition of",n,"and",m,"is", ans1)
# ans2 = n-m
# print("Subtraction of",n,"and",m,"is", ans2)
# ans3 = n*m
# print("Multiplication of",n,"and",m,"is", ans3)
# ans4 = n/m
# print("Division of",n,"and",m,"is", ans4)
# ans5 = n%m
# print("Modulus of",n,"and",m,"is", ans5)
# ans6 = n//m
# print("Floor Division of",n,"and",m,"is", ans6)

def calc(a, b, op):
    if op == "+":
        return [a+b, "sum"]
    elif op == "-":
        return [a-b, "difference"]
    elif op == "*":
        return [a*b, "product"]
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            return [a/b, "division"]
        
x = 7
y = 0
t = calc(x, y, "*")
print("The ", t[1], " of ", x, " and ", y, " is ", t[0])
