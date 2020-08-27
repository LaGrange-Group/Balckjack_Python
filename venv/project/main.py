from deck import *
from player import *
from user_interface import *


class Game:
    def __init__(self):
        self.deck = Deck();
        self.player = Player();

    def run_game(self):
        UserInterface.display_information(f'Welcome {self.player.name}!');
        self.display_welcome();
        self.action_menu();

    def display_welcome(self):
        UserInterface.display_information(f'This is BlackJack. The goal of the game is to get as close to 21 as possible without going over and to beat the dealer!');

    def action_menu(self):
        choice = UserInterface.get_user_input_string('Please select and option:\n1) View Player Info\n2) Play Round\n3) Cash Out');
        switcher = {
            '1': lambda: UserInterface.display_player_information(self.player), # Make method to return to action_menu
            '2': self.play_round,
            '3': self.cash_out
        }
        action = switcher.get(choice, self.action_menu);
        action();

    def cash_out(self):
        print('Cashing out!');

    def play_round(self):
        print('Playing Round!');
        self.action_menu();

game = Game();
game.run_game();