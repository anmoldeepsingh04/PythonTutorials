question = ["What is 1?", "What is 2?", "What is 3?", "What is 4?"]
ans = [1, 2, 3, 4]
for i in question:
    print(i)
    for k in range(1, 5):
        print(k)
    # num = 0
    num = int(input("Enter your answer "))
    # print("This is: ", ans[question.index(i)])
    # print(num == ans[question.index(i)])
    # print(type(num))
    if(num == ans[question.index(i)]):
        print("Correct! \n")
    else:
        print("Loser!")
        break