Grid={'1':' ', '2':' ', '3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}


print(Grid)

#printing Grid

def printTTT(a):
	c=0
	for v in a.values():
		if c==2 or c==5:
			print(v,'\n-+-+-')
		elif c==8:
			print(v)
			break
		else:
			print(v,end='|')
	

#the basic structure
#    | |
#  --+-+-
#    | |
#   -+-+-
#    | |


#Game logic
def game():

	player='O'
	count=0
	for x in range(10):
		printTTT(Grid)
		print("Enter position for ", player)
		pos=input()
		if Grid[pos]==' ':
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
			elif count>8:
				printTTT(Grid)
				print("****TIE****")
				break
		if player=='O':
			player='X'
		else:
			player='O'
game()
print("Game Over! \n Try Again? (y/n)")
restart=input()
if restart=='Y' or restart=='y':
	for k in Grid:
		Grid[k]=' '
	game()
else:
	print("Okay, Bye!\n\n****THE END****")


