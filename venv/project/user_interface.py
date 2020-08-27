class UserInterface:

    @staticmethod
    def get_user_input_string(prompt):
        print(prompt);
        return input();

    @staticmethod
    def display_information(message):
        print(message);

    @staticmethod
    def display_player_information(player):
        print(f'\nName: {player.name}\nMoney: {player.money}\n');