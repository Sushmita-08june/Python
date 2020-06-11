# game
import random
list1 = ["Rock","Paper","Scissor"]
tie=0
user=0
system=0
B = int(input("Enter the number of attempts you wanna try : "))
a=B
for i in range(B):
    user1 = input("Enter the value: ")
    system1 = random.choice(list1)
    print("user entered: ",user1)
    print("System entered: ",system1)
    if user1 == system1:
        tie=tie+1
        print("Its tie")
    elif user1 == "Rock" and system1 == "Paper":
        system=system+1
        print("System won")
    elif user1 == "Rock" and system1 == "Scissor":
        user=user+1
        print("User won")
    elif user1 == "Paper" and system1 == "Rock":
        user=user+1
        print("User won")
    elif user1 == "Paper" and system1 == "Scissor":
        system=system+1
        print("System won")
    elif user1 == "Scissor" and system1 == "Rock":
        system=system+1
        print("System won")
    elif user1 == "Scissor" and system1 == "Paper":
        user=user+1
    a=a-1
    print("attempts remaining : ",a)
print("User won "+ str(user) + " times")
print("System won " + str(system) + " times")
print("It was tie " + str(tie) + " times")
if (tie>user) and (tie>system):
    print("Its tie between user and system")
elif tie<user>system:
    print("User wins")
elif tie<system>user:
    print("System wins")
