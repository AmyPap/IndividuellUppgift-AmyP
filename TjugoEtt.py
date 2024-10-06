import random
import sys
import time
import pyinputplus as pyip

# This class represents a deck of cards and is responsible for creating and managing the deck
# It includes methods for initializing(constructor), shuffling, and drawing cards from the deck and resetting the deck back to 52 cards
class Deck:
    def __init__(self)->None:
        self.deck: dict[str, str|int] = self.create_deck()

    def create_deck(self) -> dict[str, int|str]:
        colors: list[str] = ['Hearts♥', 'Diamonds♦', 'Spades♠', 'Clubs♣']
        values: list[int|str] = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'] # Ace is set as 'Ace' for now; its value can be 1 or 11 in the game
        deck_of_cards: dict[str,int|str] = {} 
        for color in colors:
            for value in values: # creates key:value pair  where the card_name is the key and the card_value is the value
                card_name = f'{color} {value}'
                card_value = 10 if value in ['Jack', 'Queen', 'King'] else value #ternary operator
                deck_of_cards[card_name] = card_value  
        return deck_of_cards 

    # Method that selects a random card and ensures it won't be drawn again.
    def pick_random_card(self) -> tuple[str, str|int]: 
        # Using a debugger showed that a KeyError occurs if the deck is empty.
        # This won’t happen in my current game (Twenty-One), but could occur in other card games where players draw more cards.
        try:
            random_card: str = random.choice(list(self.deck.keys())) # Convert keys to a list so random.choice can be used.
            card_value: str|int = self.deck.pop(random_card) # Remove the card from the deck and store its value in card_value.
            return random_card , card_value 
        except (KeyError , IndexError):
            print('Deck of cards is empty!')
            self.reset_deck()
            return self.pick_random_card()

    # Resets the deck, making all cards available again.
    def reset_deck(self) -> None:
        self.deck = self.create_deck()

# This class contains the main game logik for the game TjugoEtt(TwentyOne).
# Class includes methods to handle the player's turn, the dealer's turn and the main game loop.
class Tjugoett:
    def __init__(self):
        self.deck: Deck = Deck() # self.deck instance # # Creates a new deck of cards.
        self.player_hand:list[int] = []  # A list to store the value of the player's cards.
        self.dealer_hand:list[int]= []  # A list to store the value of the dealer's cards.

    # Method that handles player's turn
    def player_turn(self):
        player_total_sum: int = 0
        continue_playing: bool= True
        
        while continue_playing:
            random_card , card_value = self.deck.pick_random_card() # Player draws from the shared deck.
            
            # The player decides the value of Ace (1 or 11)
            if 'Ace' in random_card:
                while True:
                    choice: str = input(f'Your card is {random_card}. Choose value (1 or 11): ')
                    if choice == '1':
                        card_value = 1
                        break
                    elif choice == '11':
                        card_value = 11
                        break
                    else:
                        print('Please choose either 1 or 11.') # Ensur valid inputs
                    
            self.player_hand.append(card_value) # Adds the card's value to the player's hand.
            player_total_sum += card_value 
            print(f'Your card is: {random_card}, Value: {card_value}')
            print(f'Total sum: {player_total_sum}') # Displays the total card values so the player doesn't have to count.
            
            # Ends the game immediately if the player wins or busts
            if player_total_sum == 21:
                print('\nYou win ! ! !')
                return player_total_sum
            elif player_total_sum > 21:
                print('\nSorry, You bust.')
                return player_total_sum
            
            continue_playing = pyip.inputYesNo('\nOne more card? Yes/No: ') == 'yes' #inline conditional
            time.sleep(0.8)
                
        return player_total_sum

    # Method that handles the dealer's turn
    def dealer_turn(self, player_total: int):
        dealer_total_sum: int = 0
        while dealer_total_sum < 17: # Dealer stops drawing cards when the sum is >= 16
            random_card, card_value = self.deck.pick_random_card() # Dealer draws from the same shared deck.

            # Determines the value of Ace (1 or 11)so it can be added correctly to the total_sum. 
            if 'Ace' in random_card:
                card_value = 11 if dealer_total_sum <= 10 else  1 

            self.dealer_hand.append(int(card_value)) # card_value must be an int.
            dealer_total_sum += int(card_value)
            
            print(f"Card is: {random_card}, Value: {card_value}")
            print(f"Dealer's total sum: {dealer_total_sum}\n")
            time.sleep(1) # Adds a delay to make it feel more realistik.
            
            # Determines if the dealer should stop drawing.
            if 16 <= dealer_total_sum <= 21:
                return dealer_total_sum
            elif dealer_total_sum > 21:
                print('Dealer busts. You win!')
                return dealer_total_sum
    
    # Method with main game loop
    def play_game(self)-> None:
        while True:
            self.deck.reset_deck()  # Ensures the deck contains all 52 cards.
            self.player_hand.clear() # Clears the hands before starting a new game. 
            self.dealer_hand.clear() 

            print('\n      -YOUR TURN:-     ')
            time.sleep(0.8)
            player_total: int = self.player_turn()

            if player_total == 21: # Ends the game if the player has sum 21
                print('Congratulations!') 
            elif player_total < 21: # Dealer's turn if player has < 21

                print("\n     -DEALER'S TURN:-      ")
                dealer_total: int = self.dealer_turn(player_total)

                 # Determines the winner after the dealer's turn.
                if dealer_total <= 21:
                    if dealer_total > player_total:
                        print('\nSorry, Dealer won.')
                    elif dealer_total < player_total:
                        print('\nYou won!!!')
                    else:
                        print('\nSorry, Dealer won.')
            else:
                print('Dealer wins.') # If player total > 21

            # Question that restart the game if answer isn't no.
            play_again: str = pyip.inputYesNo("\nDo you want to play again? Yes/No: ")
            if play_again == 'no':
                print('\nOk! Thank you for playing!')
                sys.exit() 

# Runs the game if the user wants to play.
if __name__ == "__main__":
    play_game: str = pyip.inputYesNo('Welcome to Twenty-One! Do you want to play? Yes/No: ')
    if play_game == 'yes':
        game: Tjugoett = Tjugoett()  # Create a new game of TwentyOne
        game.play_game() # Start the game
    else:
        print(' Thank you! Bye!')

