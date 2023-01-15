print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
selected_side = input('You\'re at a crossroda. Which side you wanna go? Type "Left" or "Right".\n').lower()
if (selected_side == "left"):
  selected_activity = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for the boat or "Swim" to swim accross.\n').lower()
  if (selected_activity == "wait"):
    selected_door = input('You have arrived at the island unharmed. There is a house with 3 doors. One red, one blue and one yellow. Which color would you like to choose? Type "Red" or "Blue" or "Yellow".\n').lower()
    if (selected_door == "red"):
      print('YOU\'VE BURNED BY FIRE!!! GAME OVER!!!')
    elif (selected_door == "yellow"):
      print('WOOHOO! YOU\'VE FOUND THE TREASURE!!! YOU WIN!!!')
    elif(selected_door == "blue"):
      print('OH NO! YOU\'VE BEEN EATEN BY A BEAST!!! GAME OVER!!!')
    else:
      print('YOU HAVE CHOOSE THE DOOR THAT DOESN\'T EXIST!!! GAME OVER!!!')
  else:
    print("ATTACKED BY AN ANGRY TROUT!!! GAME OVER!!!")
else:
  print("FALLEN INTO A HOLE!!! GAME OVER!!!")
