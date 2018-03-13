# secret=getrandom(word)--function(argument)
# wordindex= random.randint(0,len(wordlist)-1)---因为一共0-63 实际上是有64个
#while true:(infinite)
#counter=0
#   while true：
#       print('{}'.format())
#       counter+=1

#print('letters', end=' ')
#for i in range 

def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    import random
    a=random.randint(1,100)
    for i in range(1,10):
        n=input('enter the number: ')
        if n.isdigit():
            n=int(n)
            if n==a:
                return('Correct')
                break
            elif n>a:
                return('The number is bigger.')
            elif n<a:
                return('The number is smaller.')
        else:
            return('please enter an integer.')
        i+=1


