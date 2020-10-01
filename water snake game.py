import random
initial = 0
chances = 10

Your_Score = 0
Computer_Score = 0
No_of_Draw = 0

while initial<chances:
    lst = ['Water', 'Snake', 'Gun']
    user = input("Press Key: \'w\' for  Water, \'s\' for Snake, \'g\' for Gun\n")
    comp = random.choice(lst)
    # Your_Score = 0
    # Computer_Score = 0

    if user == 's' and comp == 'Water':
        print("I Chosed",{comp})
        print("You Win, I Lose")
        Your_Score += 1
    elif user == 's' and comp == 'Gun':
        print("I Chosed", {comp})
        print("You Lose, I Win")
        Computer_Score += 1
    elif user == 'w' and comp == 'Snake':
        print("I Chosed", {comp})
        print("You Lose, I Win")
        Computer_Score += 1
    elif user == 'w' and comp == 'Gun':
        print("I Chosed", {comp})
        print("You Win, I Lose")
        Your_Score += 1
    elif user == 'g' and comp == 'Snake':
        print("I Chosed", {comp})
        print("You Win, I Lose")
        Your_Score += 1
    elif user == 'g' and comp == 'Water':
        print("I Chosed", {comp})
        print("You Lose, I Win")
        Computer_Score += 1
    else:
        print("Draw")
        No_of_Draw +=1


    initial = initial + 1

print("Your Score",Your_Score)
print("My Score",Computer_Score)
print("No. Of Draw's",No_of_Draw)

