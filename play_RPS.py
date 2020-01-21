from random import randint
options = ["ROCK", "PAPER", "SCISSORS,"]

message = {
  "tie" : "Tie",
  "won" : "Player Won",
  "lost" : "Computer Won",
}

def play_RPS():
  user_choice = raw_input("Enter Rock, Paper or Scissors: ")
  user_choice.upper()
  computer_choice = options[0:2]

def decide_winner(user_choice, computer_choice):
  print str(user_choice)
  print str(computer_choice)
  if user_choice == computer_choice:
    print message[tie]
  elif user_choice == options[0] and computer_choice == options[2]:
    print message[won]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message[won]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message[won]
  elif computer_choice == options[0] and user_choice == options[2]:
    print message[lost]
  elif computer_choice == options[1] and user_choice == options[0]:
    print message[lost]
  elif computer_choice == options[2] and user_choice == options[1]:
    print message[lost]
  else:
      print "invalid"


      decide_winner(user_choice, computer_choice)
      play_RPS()                                
