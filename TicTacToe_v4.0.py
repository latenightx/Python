Grid={'9':' ', '8':' ', '7':' ','6':' ','5':' ','4':' ','3':' ','2':' ','1':' '}
# print(Grid)
 
def s(x=1,y=1):
		for i in range(5):
			if x==1:
				print(' ',end='')
			elif x==2:
				print('_',end='')	
		if y==1:		
			print('|',end='')
		elif y==2:
			print('')
		elif y==3:
			print(end='')

#printing Grid
					
def printTTT(a):
	c=1
	for v in a.values():
		if c==3 or c==6:
									
			print(' ',v,' ')
			s(2)
			s(2)
			s(2,2)
			c+=1
			continue
		elif c==9:
			print(' ',v,' ')
			s()
			s()
			s(1,2)
			print('')
			break
		elif c==1 or c==4 or c==7:
			s()
			s()
			s(1,2)
			print(' ',v,' ',end='|')
			c+=1
			continue		
		print(' ',v,' ',end='|')
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

	while True:
		player=input(' Choose X or O: ')
		if player!='O' and player!='X':
			print(" Invalid Input,Try Again")
			continue
		else:
			break
	count=0
	while True:
		
		printTTT(Grid)
		print("Enter position for ", player,'\n   ')
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
				print('',player, "Has Won!!")
				break
			elif Grid['4']==Grid['5']==Grid['6']!=' ':
				printTTT(Grid)
				print('',player, "Has Won!!")
				break
			elif Grid['7']==Grid['8']==Grid['9']!=' ':
				printTTT(Grid)
				print('',player, "Has Won!!")
				break
			elif Grid['1']==Grid['5']==Grid['9']!=' ':
				printTTT(Grid)
				print('',player, "Has Won!!")
				break
			elif Grid['3']==Grid['5']==Grid['7']!=' ':
				printTTT(Grid)
				print('',player, "Has Won!!")
				break
			elif Grid['1']==Grid['4']==Grid['7']!=' ':
				printTTT(Grid)
				print('',player, "Has Won!!")
				break
			elif Grid['5']==Grid['2']==Grid['8']!=' ':
				printTTT(Grid)
				print('',player, "Has Won!!")
				break
			elif Grid['3']==Grid['6']==Grid['9']!=' ':
				printTTT(Grid)
				print('',player, "Has Won!!")
				break
			if count>8:
				printTTT(Grid)
				print(" ****TIE****")
				break
		if player=='O':
			player='X'
		else:
			player='O'
game()
print(" Game Over!\n Try Again?\n Yes(y)/No(n)")
while True:
	
	restart=input()
	if restart=='Y' or restart=='y':
		for k in Grid:
			Grid[k]=' '
		game()
		print(" Game Over!\n Try Again?\n Yes(y)/No(n)")


		continue
		
	elif restart=='n' or restart=='N':
		print(" Okay, Bye!\n\n ****THE END****")
		break
	else :
		print(" Wrong Input\n Try Again!")
		continue
    
    
    
#New Changes:
#   CHOOSE YOUR OWN CHARACTER!


#Made By Zaid, Kiranmayi and Shoaib!
