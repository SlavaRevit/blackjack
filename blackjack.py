import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


coins_availible = [1,5,25,50,100,500]
for coin in coins_availible:
    print(coin)
def make_deposit():
    bank = 700
    deal = []
    play_again = True
    while play_again == True:
        chose_coin = int(input("Chose coin from list above: or type 'Deal' to make deal "))
        continue_or_no = str(input("Make one more deal? 'y' to make a deal or 'n' to play "))

        if continue_or_no == "y":
            deal.append(chose_coin)
            play_again = True 
        elif continue_or_no == 'n':
            play_again = False
            deal.append(chose_coin)
        
    for coin in deal:
        bank -= coin
    print(f"Your deal is {sum(deal)}")
        
    print(f"Now your bank is: {bank}")
    
    start_game = input("Start the game? press: 'Deal' ").lower()
    
    if start_game == "Deal":
        game()
        
        
def game():
    my_cards = []
    computer_card = []
    
    for i in range(2):
        random_card = random.choice(cards)
        my_cards.append(random_card)
    
    for x in range(1):
        compute_random_card = random.choice(cards)
        computer_card.append(compute_random_card)
    
    print(my_cards, sum(my_cards))
    print(computer_card) 
    take_a_card = True
    
    while take_a_card == True:
        next_card = input("What your choose 'stand' or 'hit' ")
        
        if next_card == "hit":
            new_card = random.choice(cards)
            my_cards.append(new_card)
            print(my_cards, f"Sum is:{sum(my_cards)}")

        elif next_card == "stand":
            ask_for_card = True
            while ask_for_card == True:
                if sum(computer_card) > 17:
                    ask_for_card = False
                    
                comp_card_next = input("Chose one card for computer? type 'yes' or 'no' ")
                
                if comp_card_next == "yes":
                    new_comp_card = random.choice(cards)
                    computer_card.append(new_comp_card)
                    print(computer_card, sum(computer_card))
                else:
                    ask_for_card = False
            
            take_a_card = False

        
    sum_of_my_cards = sum(my_cards)
    sum_of_computer_cards = sum(computer_card)
    
    if sum_of_my_cards > 21:
        print(f"You loose, your sum is {sum_of_my_cards}")
        print(f"Computer sum is : {sum_of_computer_cards}")
    elif sum_of_computer_cards > 21:
        print(f"You win with {sum_of_computer_cards} , sum of cumputer cards: {sum_of_computer_cards} ")
    elif sum_of_my_cards < 21 and sum_of_my_cards > sum_of_computer_cards:
        print(f"You win, your sum is {sum_of_my_cards}")
        print(f"Computer sum is : {sum_of_computer_cards}")
    
    
make_deposit()
game()

# new changes == 
# making this changes is really great to work with git