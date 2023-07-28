import random

class Game:
    def get_user_item(self):
        while True:
            user_input = input("select an item (rock/paper/scissors) : ")
            if user_input in ['rock','paper','scissors']:
                return user_input
            print("Invalid")
    
    def get_computer_item(self):
        return random.choice(['rock','paper','scissors'])
    
    def get_game_result(self, user_item, computer_item) :
        if user_item == computer_item :
            return 'draw'
        
        if (user_item == 'rock' and computer_item == 'scissors') or \
           (user_item == "paper" and computer_item == "rock") or \
           (user_item == "scissors" and computer_item == "paper"):
            return 'win'
        return 'loss'
            
    
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"You selecter {user_item}. The computer selectes {computer_item}. You {result}")
        return result
   