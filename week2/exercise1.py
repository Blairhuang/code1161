"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

#I think this will print 
#what
#dose
#this
#do
#?
for word in some_words:# name'word'is not defined.
    print(word)
# it printed the same result

#I think this will print "error：unexpexted indent" because x is not defined value in list
for x in some_words:# name'x'is not defined
    print(x)
# it printed "IndentationError: unexpected indent"

# I think this will print "some_words contains more than 3 words"
print(some_words):['what', 'does', 'this', 'line', 'do', '?']

if len(some_words) > 3:
    print('some_words contains more than 3 words')
# it printed same result


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
