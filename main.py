from enum import Enum

class Char(Enum):
    PLAYER_2 = 'X'
    PLAYER_1 = 'O'
    EMPTY = '_'


class Game:
    def __init__(self):
        self.game_array = [[Char.EMPTY for _ in range(3)] for _ in range(3)]
        print('Welcome to Tic Tac Toe!')
        self.print_game()
        self.current_player = Char.PLAYER_1
        self.turns = 0
    
    def print_game(self):
        line = [' | '.join(self.game_array[i].value()) for i in range(3)]
        print('{' + '\n '.join(line) + '}')

    def check_input(self, player_y_coordinate: str, player_x_coordinate: str, char: Char):
        try:
            validation_x = player_x_coordinate.isnumeric()
            validation_y = player_y_coordinate.isnumeric()
            num_x = 0 <= int(player_x_coordinate) <= 2
            num_y = 0 <= int(player_y_coordinate) <= 2
            is_empty = self.game_array[int(player_y_coordinate)][int(player_x_coordinate)] == Char.EMPTY

            if not num_x or not num_y:
                print('Invalid input!')

            if not validation_x or not validation_y:
                print('Invalid input!')

            if not is_empty:
                print('This spot is already taken!')

            if all([validation_x, num_x, validation_y, num_y, is_empty]):
                self.game_array[int(player_y_coordinate)][int(player_x_coordinate)] = char
                return True
            return False
        except (ValueError, IndexError):
            print('Invalid input!')
            return False

    def set_move(self, player_y_coordinate: str, player_x_coordinate: str, char: Char):
        validation = self.check_input(player_y_coordinate, player_x_coordinate, char)

        while not validation:
            print(f'Player {char.value()}, please enter your y_coordinate.')
            player_y_coordinate = input()
            print(f'Player {char.value()}, please enter your x_coordinate.')
            player_x_coordinate = input()
            validation = self.check_input(player_y_coordinate, player_x_coordinate, char)

    def check_win(self):
        for row in self.game_array:
            if row.count(Char.PLAYER_1) == 3 or row.count(Char.PLAYER_2) == 3:
                print(f'Player {row[0].value()} has won!')
                return True
        
        for col in range(3):
            col_values = [self.game_array[i][col] for i in range(3)]
            if col_values.count(Char.PLAYER_1) == 3 or col_values.count(Char.PLAYER_2) == 3:
                print(f'Player {col_values[0].value()} has won!')
                return True
        
        if [self.game_array[i][i] for i in range(3)].count(Char.PLAYER_1) == 3 or [self.game_array[i][i] for i in range(3)].count(Char.PLAYER_2) == 3:
            print(f'Player {self.game_array[0][0].value()} has won!')
            return True
        
        if [self.game_array[i][2 - i] for i in range(3)].count(Char.PLAYER_1) == 3 or [self.game_array[i][2 - i] for i in range(3)].count(Char.PLAYER_2) == 3:
            print(f'Player {self.game_array[0][2].value()} has won!')
            return True
        
        return False

    def play_game(self):
        while self.turns < 9:
            print(f'Player {self.current_player}, please enter your y_coordinate.')
            player_y_coordinate = input()
            print(f'Player {self.current_player}, please enter your x_coordinate.')
            player_x_coordinate = input()
            self.set_move(player_y_coordinate, player_x_coordinate, self.current_player)
            self.print_game()
            if self.check_win():
                print('Game over!')
                return
            self.turns += 1
            self.current_player = Char.PLAYER_2 if self.current_player == Char.PLAYER_1 else Char.PLAYER_1

        print("It's a tie!")
        

if __name__ == '__main__':
    newGame = Game()

    while True:
        newGame.play_game()
        print('Would you like to play another game of Tic Tac Toe?')
        play_again = input()
        if play_again.lower() == 'no':
            break
        newGame = Game()
        print(newGame.print_game())
