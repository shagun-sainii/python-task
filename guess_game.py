#task 1 , guess game
#by shagun 
import random
computer_choice = random.randint(1,10)
print("you got three chances to win!!")
i = 3
while i >= 1 :
    user_input = int(input("enter your number "))
    if (user_input == computer_choice):
        print("you won!!")
        break 
    else :
        print("try again !! chances left =" , i-1  )
    i -= 1
if(i<1) :
    print(" oops , chances are over !! , the number was ", computer_choice)
