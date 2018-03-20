"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""


import random

def advancedGuessingGame():
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



advancedGuessingGame()








        



      












        



      










        



      

  
"""Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
if __name__ == "__main__":
    advancedGuessingGame()
      


