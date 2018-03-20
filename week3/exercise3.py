"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
x"""


from exercise1 import not_number_rejector
from exercise1 import super_asker


import random
print('Welcome to the guessing game!(Remenmber,you only have 3 chances.)')
print('A number between () and () ?')

def advancedGuessingGame():

    while True:
        try:
            input_variable1 = int(input("enter a small number for lower bond: "))
            input_variable2 = int(input('enter a big number for larger bond: '))
            if input_variable1<input_variable2:
                print("you input the number {} and {}".format((input_variable1),(input_variable2)))
                break
            else:
                print('ENTER AGAIN')
        except ValueError:
            print("try again!")
    
    guessed=False
    count=1       
    while not guessed:
        actual_number=random.randint(int(input_variable1),int(input_variable2))
        try:
            guessed_number = int(input("enter a guessed numnber: "))
            print("you input the number {}".format(guessed_number))
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
        except:
            return("not a number\n try again!")
        return "You got it!"

    #RETURN 是final stage 如果在函数中间放入return的话，函数会自动停止

if __name__ == "__main__":
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

