import random
import os

play = input("Do you want to play? (yes or no)")

def playAgain(play):
  if play.lower() == "no":
    print("Game Over")
  elif play.lower() == "yes":
    card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    userCard = []
    dealerCard = []
    os.system('clear')
    
    for i in range(2):
      x = random.randint(0,12)
      userCard.append(card[x])
    userScore = sum(userCard)
    print(f"Your cards are {userCard}. This means that your score is {userScore}")

    for x in range(2):
      x = random.randint(0,12)
      dealerCard.append(card[x])
    print(f"The dealer's first card is {dealerCard[0]}")
    dealerScore = sum(dealerCard)

    if userScore == 21 and len(userCard) == 2:
      print("BLACKJACK!!!!! CONGRATULATIONS!!!!")
      playAgain(play)

    elif dealerScore == 21 and len(dealerCard) == 2:
      print("Dealer has BLACKJACK, better luck next time :)")
    
    def play2(userScore):
      question = input("Do you want to stand or hit? ")
      
      if question.lower() == "stand":
        
        dealerScore = sum(dealerCard)
        userScore = sum(userCard)
        print(f"The dealer's cards are {dealerCard}. This adds up to {dealerScore}")
        
        while dealerScore < 17:
          z = random.randint(0,12)
          dealerCard.append(card[z])
          dealerScore = sum(dealerCard)
          print(f"The dealer has drawn again: his new score  is {dealerScore}. His cards are {dealerCard}.")

        if userScore < 21 and dealerScore > 21:
          print("YOU WIN!")
          print(f"Your score was {userScore}, the dealer's score was {dealerScore}. His cards are {dealerCard}. Your cards are {userCard}.")

        elif userScore > dealerScore and userScore < 21:
          print("YOU WINNN!!")
          print(f"Your score was {userScore}, the dealer's score was {dealerScore}. His cards are {dealerCard}. Your cards are {userCard}.")

        elif userScore > 21 and dealerScore < 21:
          print("you lose :(")
          print(f"Your score was {userScore}, the dealer's score was {dealerScore}. His cards are {dealerCard}. Your cards are {userCard}.")

        elif userScore > 21 and dealerScore > 21:
          print("you lose :(")
          print(f"Your score was {userScore}, the dealer's score was {dealerScore}. His cards are {dealerCard}. Your cards are {userCard}.")

        elif dealerScore > userScore and dealerScore < 21:
          print("you lose :(")
          print(f"Your score was {userScore}, the dealer's score was {dealerScore}. His cards are {dealerCard}. Your cards are {userCard}.")

        elif userScore == dealerScore:
          print("tie")
          print(f"Your score was {userScore}, the dealer's score was {dealerScore}. His cards are {dealerCard}. Your cards are {userCard}.")

      elif question.lower() == "hit":
        dealerScore = sum(dealerCard)
        a = random.randint(0,12)
        if a == 12 and userScore > 11:
          userCard.append(1)
        elif a == 12 and userScore < 11:
          userCard.append(card[a])
        else:
          userCard.append(card[a])
        userScore = sum(userCard)
        print(f"Your new cards are {userCard}. This means that your new score is {userScore}")
        if userScore > 21:
          print("You lose :(, you exceeded 21")
          print(f"Your score was {userScore}, the dealer's score was {dealerScore}. His cards are {dealerCard}.")
        else:
          play2(userScore)

      playAgain2 = input("Do you want to play again? (yes/no)")
      if playAgain2.lower() == "yes":
        playAgain(play)
      elif playAgain2.lower() == "no":
        print("Thanks for playing")
      else:
        print("Invalid Repsonse, Automatically Ending.")

    play2(userScore)
  else:
    print("Answer Not Applicable")
playAgain(play)
    
