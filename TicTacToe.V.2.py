Grid={'1':' ', '2':' ', '3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
# print(Grid)

#printing Grid

def printTTT(a):
	c=1
	for v in a.values():
		if c==3 or c==6:
			print(v,'\n-+-+-')
			c+=1
			continue
		elif c==9:
			print(v)
			break
		print(v,end='|')
		c+=1
	

#the basic structure
#    | | 
#   -+-+-
#    |X|
#   -+-+-
#    | |

   
   #       |     |	 
   #    X  |     |  O
   #  _____|_____|_____
   #       |     | 
   #       |     |   
   #  _____|_____|_____            
   #       |     |
   #       |     |
   #       |     |
 
#Game logic
def game():

	player='O'
	count=0
	while True:
		printTTT(Grid)
		print("Enter position for ", player)
		pos=input()
		if pos!='1' and pos!='2' and pos !='3' and pos!='4'and pos!='5'and pos!='6'and pos!='7'and pos!='8'and pos!='9':
			print('Invalid Response,Try Again')
			continue

		elif Grid[pos]==' ':
			Grid[pos]=player
			count+=1

		else:
			print("Position already taken by ", Grid[pos], "Try another position")
			continue
		if count>=5:
			if Grid['1']==Grid['2']==Grid['3']!=' ':
				printTTT(Grid)
				print(player, " Has Won!!")
				break
			elif Grid['4']==Grid['5']==Grid['6']!=' ':
				printTTT(Grid)
				print(player, " Has Won!!")
				break
			elif Grid['7']==Grid['8']==Grid['9']!=' ':
				printTTT(Grid)
				print(player, " Has Won!!")
				break
			elif Grid['1']==Grid['5']==Grid['9']!=' ':
				printTTT(Grid)
				print(player, " Has Won!!")
				break
			elif Grid['3']==Grid['5']==Grid['7']!=' ':
				printTTT(Grid)
				print(player, " Has Won!!")
				break
			elif Grid['1']==Grid['4']==Grid['7']!=' ':
				printTTT(Grid)
				print(player, " Has Won!!")
				break
			elif Grid['5']==Grid['2']==Grid['8']!=' ':
				printTTT(Grid)
				print(player, " Has Won!!")
				break
			elif Grid['3']==Grid['6']==Grid['9']!=' ':
				printTTT(Grid)
				print(player, " Has Won!!")
				break
			if count>8:
				printTTT(Grid)
				print("****TIE****")
				break
		if player=='O':
			player='X'
		else:
			player='O'
game()
print("Game Over!\n Try Again?\nYes(y)/No(n)")
while True:
	
	restart=input()
	if restart=='Y' or restart=='y':
		for k in Grid:
			Grid[k]=' '
		game()
		print("Game Over!\n Try Again?\nYes(y)/No(n)")


		continue
		
	elif restart=='n' or restart=='N':
		print("Okay, Bye!\n\n****THE END****")
		break
	else :
		print("Wrong Input\nTry Again!")
		continue
		

# TikTacToe v2 made by Zaid and Shoaib
# What's New?
# 1) Try again bug fix:
#        - The code now can be run n number of times.
#        - Gives  alert warning when invalid input is entered.
# 2) Enhanced user friendly instructions. 
# 3) Code simplified.
