"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.
<<<<<<< HEAD


See example for first print statement
"""


import platform
=======

See example for first print statement
"""
import platform

>>>>>>> a0fec480311b6bb045bdb79ae1c35177118a8ce3
# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

for word in some_words:
<<<<<<< HEAD
#I think this will print "world" by calling the print function
    print(word) # it printed" word"

for x in some_words:
 #I think this will print "x" by calling the print function 
    print(x) # it print "x"

#I think this will print"some_worlds" by calling the print function 
print(some_words) # it print "some_words"

if len(some_words) > 3:
    # i think this will print "some_words contains more than 3 words"
    print('some_words contains more than 3 words') #it printed "some_words contains more than 3 words"

# it will define usefulFunction
def usefulFunction():# it defined useFuction
=======
    print(word)

for x in some_words:
    print(x)

print(some_words)

if len(some_words) > 3:
    print('some_words contains more than 3 words')

def usefulFunction():
>>>>>>> a0fec480311b6bb045bdb79ae1c35177118a8ce3
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
<<<<<<< HEAD
#I think this will print"platform.uname()" by calling the print function
    print(platform.uname())#it printed "platform.uname()"
=======
    print(platform.uname())
>>>>>>> a0fec480311b6bb045bdb79ae1c35177118a8ce3

usefulFunction()
