import random
import colorama
from colorama import Fore, Style
import pyfiglet
from time import sleep

# Initialize colorama
colorama.init(autoreset=True)

class RockPaperScissors:
    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0
        self.options = ["rock", "paper", "scissors"]
        self.winning_combinations = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
    
    def display_welcome(self):
        """Display welcome message using pyfiglet"""
        welcome_text = pyfiglet.figlet_format("ROCK PAPER SCISSORS", font="slant")
        print(Fore.CYAN + welcome_text)
        print(Fore.YELLOW + "=" * 60)
        print(Fore.WHITE + "Type ROCK, PAPER, SCISSORS or 'Q' to quit")
        print(Fore.YELLOW + "=" * 60 + "\n")
    
    def get_user_choice(self):
        """Get and validate user input"""
        while True:
            user_input = input(Fore.GREEN + "Your choice: ").lower()
            if user_input == "q":
                return user_input
            
            if user_input in self.options:
                return user_input
            else:
                print(Fore.RED + "Invalid choice! Please try again.")
    
    def get_computer_choice(self):
        """Generate computer's choice"""
        random_number = random.randint(0, 2)
        computer_pick = self.options[random_number]
        return computer_pick
    
    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner of the round"""
        if user_choice == computer_choice:
            self.display_tie(user_choice)
            return "tie"
        
        if self.winning_combinations[user_choice] == computer_choice:
            self.display_win(user_choice, computer_choice)
            self.user_wins += 1
            return "user"
        else:
            self.display_loss(user_choice, computer_choice)
            self.computer_wins += 1
            return "computer"
    
    def display_win(self, user_choice, computer_choice):
        """Display win message"""
        win_text = pyfiglet.figlet_format("YOU WIN!", font="small")
        print(Fore.GREEN + win_text)
        print(f"{Fore.CYAN}Your {user_choice.upper()} beats {computer_choice.upper()}")
    
    def display_loss(self, user_choice, computer_choice):
        """Display loss message"""
        loss_text = pyfiglet.figlet_format("YOU LOSE!", font="small")
        print(Fore.RED + loss_text)
        print(f"{Fore.CYAN}Computer's {computer_choice.upper()} beats your {user_choice.upper()}")
    
    def display_tie(self, choice):
        """Display tie message"""
        tie_text = pyfiglet.figlet_format("TIE!", font="small")
        print(Fore.YELLOW + tie_text)
        print(f"{Fore.CYAN}Both chose {choice.upper()}")
    
    def display_score(self):
        """Display current score"""
        print(Fore.YELLOW + "\n----- SCORE -----")
        print(f"{Fore.GREEN}You: {self.user_wins}")
        print(f"{Fore.RED}Computer: {self.computer_wins}\n")
    
    def display_goodbye(self):
        """Display goodbye message"""
        goodbye_text = pyfiglet.figlet_format("GOODBYE!", font="slant")
        print(Fore.MAGENTA + goodbye_text)
        print(f"{Fore.CYAN}Final Score - You: {self.user_wins} | Computer: {self.computer_wins}")
        
        if self.user_wins > self.computer_wins:
            print(Fore.GREEN + "Congratulations! You are the champion!")
        elif self.user_wins < self.computer_wins:
            print(Fore.RED + "Better luck next time!")
        else:
            print(Fore.YELLOW + "It's a tie! Well played!")
    
    def play_game(self):
        """Main game loop"""
        self.display_welcome()
        
        while True:
            user_choice = self.get_user_choice()
            if user_choice == "q":
                break
            
            print(Fore.CYAN + "\nRock...")
            sleep(0.5)
            print(Fore.CYAN + "Paper...")
            sleep(0.5)
            print(Fore.CYAN + "Scissors...")
            sleep(0.5)
            print(Fore.CYAN + "Shoot!\n")
            
            computer_choice = self.get_computer_choice()
            print(f"{Fore.YELLOW}Computer picked: {Fore.WHITE}{computer_choice.upper()}")
            
            self.determine_winner(user_choice, computer_choice)
            self.display_score()
        
        self.display_goodbye()
