
import random

def guessing_game():
    print('Welcome to the guessing game!(Remember,you only have 3 chances.)')
    print('A number between 10 and ?')

   
    while True:
        A=input('enter the number you like:  ')
        if A.isdigit():
            print('OK,from 10 to '+A)
            break
        else:
            print('PLZ enter an integer.')
    
    guessed=False
    count=1       
    while not guessed:
        actual_number=random.randint(10,int(A))
        guessed_number=input('now enter a guessed number: ')
        if guessed_number.isdigit():
            if int(guessed_number)>actual_number and count<3:
                count+=1
                print('too big')
            elif int(guessed_number)<actual_number and count<3:
                count+=1
                print('too small')
            elif int(guessed_number)==actual_number and count<3:
                count+=1
                print('YOU GOT IT!')
                guessed=True
            else:
                print('game over.')
                guessed=True
        else:
            print('PLZ enter an integer.')



guessing_game()








        



      

