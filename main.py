# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

from os import WCOREDUMP


player1 = 'Ruud Gullit'
player2 = 'Marco van Basten' 

goal_0 = 32
goal_1 = 54

scorers = player1 + " " + str(goal_0) + "," + " " + player2 + " " + str(goal_1)

#print (scorers)

report = f"{player1} scored in the {goal_0}nd minute" +"\n" f"{player2} scored in the {goal_1}th minute"
print (report)

player = 'Ronald Koeman' 

first_name = player[0:6]
first_name_start = player[:player.find(' ')-1]
first_name_end = player[:player.find(' ')+1]

print(first_name)

last_name = player[7:13]
last_name_start = player[:player.find(' ')+1]
last_name_end = player[:player.find(' ')-1]
last_name_len = len(last_name)

print(last_name_len)

name_short = f"{first_name[0]}. {last_name}"

print(name_short)

chant = f"{first_name}! " *6
chant=chant[:-1]

print(chant)

good_chant = True
bad_chant = False
print(good_chant != bad_chant)





















