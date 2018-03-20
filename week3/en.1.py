# leaderboard=[]

while True:
    try:
        input_variable = int(input("enter a numnber: "))
        input_float = float(input("enter a float: "))
        print("you input the number {}".format(input_variable))
        print("you input the number {}".format(input_float))
        break #in a function you would return
    except:
        print("not a number\n try again!")

        #is digit用于str(‘number')
        #try and except 是指如果try不满足的话直接跳到except 但是if中间就是如果不符合不会跳到elif
        