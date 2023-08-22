import random
from art import logo

launch = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while not (launch == "y" or launch == "n"):
  launch = input("You enter an invalid input. Type 'y' or 'n': ").lower()

if launch == "y":

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
           11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
           11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
           11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  remaining_cards = []
  user_cards = []
  computer_cards = []
  user_score = 0
  computer_score = 0
  another_card = ""
  
  def show_hands():
    user_score = current_score(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

  def show_final_hands():
    user_score = current_score(user_cards)
    computer_score = current_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

  def user_turn():
    if current_score(user_cards) == 21:
        computer_turn()
        return
    
    show_hands()
    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    while not (another_card == "y" or another_card == "n"):
      another_card = input("You enter an invalid input. Type 'y' or 'n': ").lower()

    if another_card == "y":
      user_cards.append(int(random.choice(cards)))
      remove_cards(user_cards)
      if current_score(user_cards) > 21:
        if 11 in user_cards:
          user_cards[user_cards.index(11)] = 1
          user_turn()
        else:
          computer_turn()
      else:
        user_turn()
    else:
      computer_turn()

  
  def computer_turn():
    while current_score(computer_cards) < 17: 
     computer_cards.append(int(random.choice(cards)))
     remove_cards(computer_cards)
     if 11 in computer_cards:
       computer_cards[computer_cards.index(11)] = 1
      
    user_score = current_score(user_cards)
    computer_score = current_score(computer_cards)

    end_score(user_score,computer_score)

  def current_score(score_list):
    actual_score = 0
    for score in score_list:
      actual_score += score
    return actual_score

  def end_score(user_end_score, computer_end_score):
    show_final_hands()
    if (computer_end_score <= 21 and computer_end_score > user_end_score) or (computer_end_score <= 21 and user_end_score > 21) :
      print("You lose.")
    elif (user_end_score <= 21 and user_end_score > computer_end_score) or (user_end_score <= 21 and computer_end_score > 21):  
      print("You Win !")
    elif not computer_end_score == 21 and user_end_score == 21:
      print("Blackjack ! You Win !!!")
    else:
      print("Draw")
    print(cards)  


  def remove_cards(cards_list):
       cards.remove(cards_list[-1])

  def blackjack():
    user_cards.append(int(random.choice(cards)))
    remove_cards(user_cards)
    user_cards.append(int(random.choice(cards)))
    remove_cards(user_cards)
    computer_cards.append(int(random.choice(cards)))
    remove_cards(computer_cards)
    user_turn()
    
  print(logo)
  blackjack()
