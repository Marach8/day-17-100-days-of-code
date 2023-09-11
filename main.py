from getpass import getpass as input
print('\033[32mEPIC BATTLE BETWEEN TWO PLAYERS\033[0m')

x = 0
y = 0
while True:
  print()
  print('In this game, you have to enter R for rock, S for scissors and P for paper.')
  print()
  
  player_1 = input('Player_1 > ').upper()
  print()
  player_2 = input('Player_2 > ').upper()
  print()
  
  if player_1 == 'R' and player_2 == 'P':
    print("Hey! player_1's Rock Smashed Player_2's Paper")
    x += 1
    
  elif player_1 == 'R' and player_2 == 'S':
    print("Huh! a Rock and a Scissors are both hard materials. That should be a tie 😊")
    
  elif player_1 == 'P' and player_2 == 'S':
    print("Player_2 has won!")
    y += 1
    
  elif player_1 == player_2:
    print("Wooo! that's a tie !")
    
  elif player_2 == 'R' and player_1 == 'P':
    print("Hey! player_2's Rock Smashed Player_1's Paper")
    y += 1
    
  elif player_2 == 'R' and player_1 == 'S':
    print("Huh! a Rock and a Scissors are both hard materials. That should be a tie 😊")
    
  elif player_2 == 'P' and player_1 == 'S':
    print("Player_1 has won!")
    x += 1
  if x == 3 or y == 3:
    break
  
print()  
if x > y:
  print(f'\033[33mplayer_1 has {x} points while player_2 has {y} points. Therefore player_1 won.\033[0m')
else:
  print(f'\033[32mplayer_1 has {x} points while player_2 has {y} points. Therefore player_2 won.\033[0m')