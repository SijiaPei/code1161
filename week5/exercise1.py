# -*- coding: UTF-8 -*-
import math
import requests
"""Refactoring.


This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
    print(countdown("Getting ready to start in",9,0,"Let's go!"))
    triangle = {"base": 3, "height": 4}
    triangle["hypotenuse"] = triangle["base"]**2 + triangle["height"]**2
    print("area ="+calculate_area(triangle["base"],triangle["height"]))
    print("side lengths are:")
    print("base: {}".format(triangle["base"]))
    print("height: {}".format(triangle["height"]))
    print("hypotenuse: {}".format(calculate_hypotenuse(triangle["base"],triangle["height"])))
    print("hypotenuse: {}".format(calculate_hypotenuse(5,6)))
    print("hypotenuse: {}".format(calculate_hypotenuse(40,30)))
    
# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    returnlist=[]
    step=1
    if (start>stop):
        step=-1
    for x in range(start,stop,step):
        a=message+str(x)
        returnlist.append(a)
    returnlist.append(completion_message)
    return returnlist

# TRIANGLES
# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    hypotenuse = math.sqrt(base**2 + height**2)
    return hypotenuse
      
def calculate_area(base, height):
    area = base*height/2
    return area
    
def calculate_perimeter(base, height):
    c = calculate_hypotenuse(base,height)
    perimeter = base+ height + c
    return perimeter

def calculate_aspect(base, height):
    if base>height:
        print("wide")
        return "wide"
    elif base<height:
        print("tall")
        return "tall"
    else:
        print("equal")
        return "equal"



# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {"area": calculate_area(base, height),
            "perimeter": calculate_perimeter(base, height),
            "height": height,
            "base": base,
            "hypotenuse": calculate_hypotenuse(base, height),
            "aspect": calculate_aspect(base, height),
            "units": units}


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)
    aspect = facts_dictionary["aspect"]
    if aspect == "tall":
        return tall.format(**facts_dictionary)
    elif aspect == "wide":
        return wide.format(**facts_dictionary)
    else:
        return equal.format(**facts_dictionary)

def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    facts_dictionary= get_triangle_facts(base, height, units="mm")
    diagram1=tell_me_about_this_right_triangle(facts_dictionary)
    if return_diagram and return_dictionary:
        facts_dictionary["diagram"]=diagram1
        return facts_dictionary
    elif return_diagram:
        return tell_me_about_this_right_triangle(facts_dictionary)
    elif return_dictionary:
        d2={"facts":{}}
        d2["facts"].update(facts_dictionary)
        return d2
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    pyramid_list = []
    pyramid_list = list_of_words_with_lengths(range(3,21,2))
    pyramid_list += list_of_words_with_lengths(range(20,3,-2))
    return pyramid_list 

def get_a_word_of_length_n(length):
    try:
        x=int(length)
    except Exception:
        print(" what you entered [{0}] is not a number".format(length))
        return None   
    if length<=0:
        return None
    baseURL = "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength={0}&maxLength={0}&limit=1"
    url = baseURL.format(length)
    r = requests.get(url)
    message = r.json()[0]['word']
    return message

def list_of_words_with_lengths(list_of_lengths):
    aaaaa = []
    for x in list_of_lengths:
        aaaaa.append( get_a_word_of_length_n(x))
    return aaaaa

if __name__ == "__main__":
    do_bunch_of_bad_things()
  
