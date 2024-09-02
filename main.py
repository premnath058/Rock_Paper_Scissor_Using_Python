import random

print("Winning rules of the game ROCK, PAPER, SCISSORS are : \n"
      +"Rock VS Papar --> Paper Wins \n"
      +"Rock VS Scissor --> Rock Wins \n"
      +"Paper VS Scissor --> Scissor Wins \n")

while True:
    print("Enter your choice : \n 1 - Rock \n 2 - Papar \n 3 - Scissor \n")

    choice = int(input("Enter your choice: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice please..."))
        
    
    if choice == 1:
        choice_name = "Rock"
        
    elif choice== 2:
        choice_name = "Paper"
        
    else:
        choice_name = "Scissor"
        
    
    print("User choice is : ", choice_name)
    print("Now It's Computers turn...")

    comp_choice = random.randint(1,3)

    while comp_choice == choice:
        comp_choice = random.randint(1,3)
        
    
    if comp_choice == 1:
        comp_choice_name = "Rock"
        
    elif comp_choice == 2:
        comp_choice_name = "Paper"
        
    else:
        comp_choice_name = "Scissor"
        
    
    print("Computer choice is : ", comp_choice_name)
    print(choice_name, "VS", comp_choice_name)

    if choice == comp_choice:
        print("It's a Draw", end = "")
        result = "Draw"
        
    
    if choice == 1 and comp_choice == 2:
        print("Paper Wins -->", end = "")
        result = "Paper"
        
    elif choice == 2 and comp_choice == 1:
        print("Paper Wins -->", end = "")
        result = "Paper"
        
    
    if choice == 1 and comp_choice == 3:
        print("Rock Wins -->", end = "")
        result = "Rock"
        
    elif choice == 3 and comp_choice == 1:
        print("Rock Wins -->", end = "")
        result = "Rock"
        
    
    if choice == 2 and comp_choice == 3:
        print("Scissor Wins -->", end = "")
        result = "Scissor"
        
    elif choice == 3 and comp_choice == 2:
        print("Scissor Wins -->", end = "")
        result = "Scissor"
        
    
    if result == "Draw":
        print("<== It's a Tie ==>")
        
    if result == choice_name:
        print("<== You won ==>")
        
    if result == comp_choice_name:
        print("<== You Lost ==>")
        
    print("Do you want play again? (Y/N)")
    
    ans = input().lower()
    if ans == "n":
        break
    
print("Thanks for Playing...")
    



        
