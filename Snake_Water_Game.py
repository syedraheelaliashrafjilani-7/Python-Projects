import random 
'''
1 used for Snake
-1 used for Water
0 used for Gun
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter Your Choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

#By now we have 2 Numbers (variables), you and Computer

print(f"You Choose {reverseDict[you]}\nComputer Choose {reverseDict[computer]}")

if(computer == you):
    print("It's a Draw!")

else:
    if(computer==-1 and you==1):
        print("You Win!")
    
    elif(computer==-1 and you==-1):
        print("You Lose!")
    
    elif(computer==1 and you==-1):
        print("You Lose!")

    elif(computer==1 and you==0):
        print("You Win!")
    
    elif(computer==0 and you==-1):
        print("You Win!")

    elif(computer==0 and you==1):
        print("You Lose!")
    
    else:
         print("Something Went Wrong!")

       