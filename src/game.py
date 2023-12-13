"""
Author: M.A.Moghadasi
Date Created: 11/13/2023
Description: Rock,Paper,Scissors Game
"""

import random


class RockPaperScissors :
    """ The main class of Rock Paper Scissors game

    User will play with Computer. In this Game user and Computer will  choice between Rock,Paper,Scissors
    at same time and then the winner will detect based on the Main Rule of Game.
    """
    def __init__(self, name : str ) :
        self.choices = ['rock' , 'paper', 'scissors']
        self.player = name

    def get_user_choice(self)-> str :
        """get_user_choice Getting the choice of user
        """
        while True :
            user_input = input(f'Enter Your Choice ! {self.choices}  ').lower()
            if user_input in self.choices :
                return user_input
            else :
                print(f'Your Choice is Invalid ! Please select between {self.choices}')
                continue

    def get_computer_choice(self)-> str:
        """get_computer_choice getting the randomly choice between Rock,Paper,Scissors.
        """
        pc_input = random.choice(self.choices)
        return pc_input

    def detecting_winner(self,user : str, pc : str)-> str:
        """detecting_winner Detecting that which one are the winner base on their choises.

        Base on the rule of game and the choise of each players(pc or user) we detect that which one is the winner !

        :param user: the choise of user between Rock,Paper,Scissors.
        :type user: str
        :param pc: the choise of Computer between Rock,Paper,Scissors.
        :type pc: str
        :return: getting a text which introduce the winner of the game.
        :rtype: str
        """
        if user == pc :
            return 'Similar choice! no winner'
        elif user == 'q' :
            return
        else :
            win_condition = [('paper','rock'), ('rock', 'scissors'), ('scissors', 'paper')]
            for condition in win_condition :
                if condition[0] == user and condition[1] == pc :
                    return f'congratulations! {self.player} won the game !'
                elif (user,pc) not in win_condition :
                    return 'Fuck ! Computer won the game :/ '

    def play(self)-> str:
        """Play play the game

        -Getting the user choice .
        -Getting the computer choice .
        -Detectting the winner .
        -Print the result.

        :return: The result of the Game .
        :rtype: str
        """
        user_choice = self.get_user_choice()
        print(f'{self.player} has picked = {user_choice}')
        if user_choice == 'q':
            return 'GoodBye... !'
        else :
            pc_choice = self.get_computer_choice()
            print(f'Computer has picked = {pc_choice}')
        winner = self.detecting_winner(user_choice, pc_choice)
        print(winner)


if __name__ == '__main__':
    game = RockPaperScissors('amin')
    print(f'Hi {game.player} Lets play :) ')
    while True :
        game.play()
        play_again = input('Do you want to play again? type "y" to play again or "n" to quit ! ').lower()
        if play_again == 'y' :
                continue
        elif play_again == 'n':
            print(F'GoodBye {game.player} ...!')
            break
        else :
            print(f'Your input is invalid ! GoodBye {game.player} ... !')
            break

