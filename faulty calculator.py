# 45*3=555 56+9=77 56/6=4

print("Enter the operator you want use")

op = input()

########################################################################################################################
if op == "*" :
    print("Enter 1st no.")
    n1 = int(input())

    if n1== 45 :
        print("Enter 2nd no.")
        n2 = int(input())

        if n2==3:
            print("Answer is:555")
        else:
            print("Answer is:",n1*n2)

    else:
        print("Enter 2nd no.")
        n21 = int(input())
        print("Answer is:",n1*n21)
########################################################################################################################
elif op == "+":
    print("Enter 1st no.")
    n1 = int(input())

    if n1 == 56:
        print("Enter 2nd no.")
        n2 = int(input())

        if n2 == 9:
            print("Answer is:77")
            else:
            print("Answer is:", n1 + n2)


    else:
        print("Enter 2nd no.")
        n21 = int(input())
        print("Answer is:", n1+n21)
########################################################################################################################
elif op == "/" :
    print("Enter 1st no.")
    n1 = int(input())

    if n1== 56 :
        print("Enter 2nd no.")
        n2 = int(input())

        if n2==6:
            print("Answer is:4")
            else:
            print("Answer is:", n1 / n2)


    else:
        print("Enter 2nd no.")
        n21 = int(input())
        print("Answer is:",n1*n21)
3#######################################################################################################################
