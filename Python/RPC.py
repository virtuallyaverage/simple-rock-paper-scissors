import random as rd
import numpy as np
import json
from time import sleep

class Responses():
    def __init__(self, snark_level:int = 10, response_file:str ="response.json") -> None:
        #setup reading and set the snark level()
        #TODO:implement snark
        self.snark_level = snark_level
        self.response_file = self.__load_responses__(response_file)
        
        #create list for each category
        self.response_names = []
        #create dictionary for the length of each of the categories
        self.response_lengths = {}
        
        #get all category names in the file
        for dict_name in self.response_file:
            #append each name to our list of available names
            self.response_names.append(dict_name)
            
            #append each length to our dictionary
            self.response_lengths[dict_name] = len(self.response_file[dict_name])
        
    
    def get_msg(self, message_type:str):
        #check to see if it is a valid input
        if message_type not in self.response_names:
            print(f"your type of message \"{message_type}\" is not a valid input")
            print(f"valid inputs are: {self.response_names}")
        
        #pick a random message
        response_index = rd.randint(0, self.response_lengths[message_type]-1)
        
        #get selected message
        response = self.response_file[message_type][response_index]
        
        #return the message
        return response
        
    def __load_responses__(self, file_path):
        #load in the database from the file_path
        with open(file_path, "r") as file:
            database = json.load(file)
        return database 
    
    
class guess_alieses():
    """A class to correlate the users input to one of the three predefined courses
    
    """
    
    def __init__(self, file_path:str = "alias.json") -> None:
        #load in the database from the file_path
        with open(file_path, "r") as file:
            self.database = json.load(file)
        
        #default print strings
        self.not_found_message = "The value you provided did not correlate to Rock, Paper, or Scissors\nPlease enter a valid response: "
        self.repeat_offender = "That was wrong too, you can try again, OR NOT!: "
        
        #define the order we count rpc in 
        self.rpc_order = [(0, "rock"), (1, "paper"), (2, "scissors"), (100, "nuke")]
        self.number_key_pairs = {"rock": 0, "paper": 1, "scissors": 2, "nuke": 100}
            
    def get_alias(self, input_str):
        #see if it is an int(0, 1, 2) -> r, p, c, respectively
        if type(input_str) == int:
            #go through each pair of number and 
            for num, string in self.rpc_order:
                #if the number matches the input_str number, we return the value
                if input_str == num:
                    return string
            
            #TODO: implement error handling for the number to text correlator
            print("number to text not found")
            exit()
        
        #look through each key
        for _, key in self.rpc_order:
            #look through the possible values from each key
            for possible_match in self.database[key]:
                if possible_match.lower() == input_str.lower():
                    #return the number associated with that key
                    print(self.number_key_pairs[key], key)
                    return self.number_key_pairs[key], key
                
        #if not found spawn new instance of function(VEEEEEEERRY JANKY )
        print("input not found in list of keys")
        another_guessing = input("new guess? ").lower()
        #pass value back through all the functions created
        return self.get_alias(another_guessing)

    
    def get_winner(self, computer, user):
        #cases where ties
        if computer == user:
            return 'tie'
        
        #cases where computer wins
        elif computer > user or computer == 2 and user == 0:
            return 'computer'
        
        #cases where user wins
        elif user > computer or user == 2 and user == 0:
            return 'user'
        
        #if hell breaks loose
        else:
            print("you are a failure, because a creator is defined by their creations")
     
            
    
def do_round(replies, guess_alieses):
    user_start_prompt = "The computer has provided an answer, Please enter yours: "
    
    #get computer guesses
    computer_guess_num = rd.randint(0, 2)
    computer_guess_str = guess_alieses.get_alias(computer_guess_num)
    
    #get user guesses
    user_guess_str = input(user_start_prompt)
    user_guess_num, user_guess_key = guess_alieses.get_alias(user_guess_str)
    
    #find who wins
    winner = guess_alieses.get_winner(computer_guess_num, user_guess_num)
    
    #get message for who wins
    print("")
    if winner == 'computer':
        round_message = replies.get_msg('win')
    elif winner == 'user':
        round_message = replies.get_msg('loss')
    elif winner == 'tie':
        round_message = replies.get_msg('tie')
    else:
        round_message = "something went wrong, please try again"
        
    print(f"the computer guessed: {computer_guess_str}, and you guessed: {user_guess_key}\n")
    print("The computer says:")
    print(round_message)
  
    return replies, guess_alieses, winner
    
def main():
    #setup the response class
    replies = Responses()
    
    #setup the class for correlating input data to our desired inputs
    guess_alieses_ = guess_alieses()
    
    #setup init values
    keep_playing = True
    tie_num = 0
    computer_wins = 0
    user_wins = 0
        
    #send startup message
    print(replies.get_msg("introduce"))
    
    #start gameplay loop
    while keep_playing == True:
        
        #get the winner from a round
        replies, guess_alieses_, winner = do_round(replies, guess_alieses_)
        
        #keep tabs of totals
        if winner == "tie":
            tie_num += tie_num + 1
        elif winner == "computer":
            computer_wins += computer_wins + 1
        elif winner == "user":
            user_wins += user_wins + 1
            
        print("")
        print(f"totals:")
        print(f"ties: {tie_num}")
        print(f"computer wins: {computer_wins}")
        print(f"user wins: {user_wins}")
            
        #see if still wants to play
        if input("\nKeep playing? (y/n): ").lower() == "y":
            keep_playing = True
        else:
            print("Exiting, Thanks for Playing!")
            sleep(1.5)
            
        
    
    
        
if __name__ == "__main__":
    main()