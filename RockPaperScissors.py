import random
#user ko puchenge ki konsa lega?
#e.g. user ne paper liya
#AI ko ek list de denge aur random.choice(list) li madad se ek random sign choose karenge
#Signs ko evaluate karenge aur result btaenge
#while loop ke andar fit kardenge

print("Welcome to stone paper scissors!")
print("Here, you will play against computer- try to win!")

aiscore = 0
playerscore = 0
signs = {
    "stone" : 1,
    "paper" : 2,
    "scissors" : 3
}
aisigns = ["Stone" , "Paper" , "Scissors"]
while True :
    print(signs)
    user_choice = abs(int(input("Which sign you want to choose? (1,2, or 3) : ")))
    if user_choice > 3 :
        print(f"Please choose a valid number, from 1, 2, or 3. You gave {user_choice}, and that is not in the option...")
        continue
    elif user_choice == 0 :
        print("Nope, Zero isn't allowed here, choose from 1,2, or 3")
        continue

    print(f"Did you choose {aisigns[user_choice - 1]} ?")
    confirmation = str(input("Yes or No : ")).lower()
    if confirmation in "yes" :
        print("Alright! great choice, let's see if you can beat computer...")

    elif confirmation in "no":
        print("Oh! if that's the case, then choose again, take your time!")
        continue
    else:
        print("Kindly type something 'valid'...")
        continue

    ai_choice = random.choice(aisigns)
    print("STONE!")
    print("PAPER!")
    print("SCISSORS!")
    print("GO!")
    print("")
    print(f"AI: I choose {ai_choice}!")
    print("")
    print("Checking...")
    #signs = {
#     "stone" : 1,
#     "paper" : 2,
#     "scissors" : 3
# }
# aisigns = ["Stone" , "Paper" , "Scissors"]

    if user_choice == 1 : #stone
        if ai_choice == "Stone" :
            print("It's a draw!")
        elif ai_choice == "Paper" :
            print("You lost!")
            print("")
            print("AI gained one point")
            print("")
            aiscore += 1
            print(f"AI score : {aiscore}")
            print(f"Player score : {playerscore}")
        elif ai_choice == "Scissors" :
            print("You won!")
            print("")

            print("You gain one point!")
            print("")

            playerscore += 1
            print(f"AI score : {aiscore}")
            print(f"Player score : {playerscore}")

    elif user_choice == 2 :#paper
        if ai_choice == "Paper" :
            print("It's a draw!")
        elif ai_choice == "Scissors" :
            print("You lost!")
            print("AI gained one point")
            aiscore += 1
            print(f"AI score : {aiscore}")
            print(f"Player score : {playerscore}")
        elif ai_choice == "Stone" :
            print("You won!")
            print("You gain one point!")
            playerscore += 1
            print(f"AI score : {aiscore}")
            print(f"Player score : {playerscore}")
        
    elif user_choice == 3 :#scissors
        if ai_choice == "Scissors" :
            print("It's a draw!")
        elif ai_choice == "Stone" :
            print("You lost!")
            print("AI gained one point")
            aiscore += 1
            print(f"AI score : {aiscore}")
            print(f"Player score : {playerscore}")
        elif ai_choice == "Paper" :
            print("You won!")
            print("You gain one point!")
            playerscore += 1
            print(f"AI score : {aiscore}")
            print(f"Player score : {playerscore}")