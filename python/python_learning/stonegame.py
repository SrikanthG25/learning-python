import random
game=['r','p','s']
n=int(input("Enter the no of chance : "))
chance=n
No_of_chance=0
human_point=0
computer_point=0
print("    !__Rock__ , __paper__ , __scissors__!")
print(" \n r for rock \n p for paper \n s for scissors ")
while No_of_chance < chance:
    user=input('rock,paper,scissor  : ')
    machine=random.choice(game)
    if user==machine:
        print("Tie both 0 point for each other")

    # Rock
    elif user=='r' and machine=='p':
        computer_point=computer_point+1
        print(f"your play {user} and machine play {machine} \n")
        print("machine win 1 points \n")
        print(f"computer_point is {computer_point} and user point is {human_point} \n")
    elif user=='r' and machine=='s':
        computer_point=computer_point+1
        print(f"your play {user} and machine play {machine} \n")
        print("human win 1 points \n")
        print(f"computer_point is {computer_point} and user point is {human_point} \n")
    #paper
    elif user=='p' and machine=='r':
        computer_point=computer_point+1
        print(f"your play {user} and machine play {machine} \n")
        print("human win 1 points \n")
        print(f"computer_point is {computer_point} and user point is {human_point} \n")
    elif user=='p' and machine=='s':
        computer_point=computer_point+1
        print(f"your play {user} and machine play {machine} \n")
        print("machine win 1 points \n")
        print(f"computer_point is {computer_point} and user point is {human_point} \n")
    #scissor
    elif user=='s' and machine=='r':
        computer_point=computer_point+1
        print(f"your play {user} and machine play {machine} \n")
        print("machine win 1 points \n")
        print(f"computer_point is {computer_point} and user point is {human_point} \n")
    elif user=='s' and machine=='p':
        computer_point=computer_point+1
        print(f"your play {user} and machine play {machine} \n")
        print("human win 1 points \n")
        print(f"computer_point is {computer_point} and user point is {human_point} \n")
    else:
        print("Enter a valid input : ")
    
    No_of_chance=No_of_chance+1
    print(f"{chance - No_of_chance} is left out of {chance} \n")
print("-- Game Over --")
if computer_point==human_point:
    print("Tie")
elif computer_point>human_point:
    print("Machine Wins and User loss")
else:
    print("User Wins and Machine loss")
print(f"User point is {human_point} and Machine point is {computer_point}")