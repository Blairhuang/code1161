import json

list=[1,2,3,4,5]
filename='numbers.json'
with open (filename,'w') as f_obj:
    json.dump(list,f_obj)




import random
def guessing_game():
    user_name=input('enter your name:  ')
    print('Welcome to the guessing game, '+user_name)
    while True:
        low=input('please enter the LOWEST number: ')
        high=input('PLZ enter the HIGHEST number: ')
        count=1
        if low.isdigit()and high.isdigit():
            print('range is between '+str(low)+'and '+str(high))
            actual_number=random.randint(int(low),int(high))
            break
        else:
            print('plz enter an integer.')   
            
    guess=False
    while not guess:
        guessed_number=input('enter a guessing number: ')       
        try:
            if guessed_number.isdigit()and guessed_number==actual_number and count>=0:
                print('U got it.')
                count-=1
                guess=True
            elif guessed_number.isdigit()and int(guessed_number)>int(actual_number) and count>=0:
                print('Too big')
                count-=1
            elif guessed_number.isdigit()and int(guessed_number)<int(actual_number) and count>=0:
                print('Too small')
                count-=1
            elif count<0:
                print('game over.')
                count-=1
                guess=True
        except:
            print('plz enter an integer.')
print(guessing_game())
    
import requests
import json

