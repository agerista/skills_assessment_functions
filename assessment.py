"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.
def is_hometown(city):
    """Determines whether a given city is my hometown"""

    if city == "Andover":
        return True

    else:
        return False

is_hometown("Andover")
is_hometown("Minneapolis")
is_hometown("San Francisco")

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.


def full_name(first_name, last_name):
    """Concatenates first name and last name into one string"""

    return first_name + " " + last_name

full_name("Balloonicorn", "Jones")
full_name("Hackbright", "Student")
full_name("Happy", "Bootcamper")

# def fancy_full_name(first_name, last_name):
#     """Concatenates first name and last name and greets the user"""

#     first_name = raw_input("Enter your first name:  ")
#     last_name = raw_input("Enter your last name:  ")

#     print "Hello %s %s, it is great to meet you!" % (first_name, last_name)

# fancy_full_name("first_name", "last_name")

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.


def same_place(hometown, first_name, last_name):
    """Checks to see if user is from my hometown"""

    city = hometown
    if is_hometown(city):
        print "Hi, {0}, we're from the same place!" .format(full_name(first_name, last_name))

    else:
        print "Hi, {0}, where are you from?" .format(full_name(first_name, last_name))

same_place("Andover", "Sammy", "Smith")
same_place("Minneapolis", "Bob", "Jones")
same_place("San Francisco", "Balloonicorn", "Jones")

###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""

    if fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry":
        return True

    else:
        return False


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    if is_berry(fruit) is True:
        return 0

    elif is_berry(fruit) is False:
        return 5

    else:
        print "I do not understand."


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    new_list = []

    for l in lst:
        new_list.append(l)
    new_list.append(num)

    return new_list
# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(base_price, state_abbreviation, tax_percentage=.05):
    """Calculates an items total cost by adding tax and additional fees required
    by state law.
    """

    RECYCLING_FEE = .03
    HIGHWAY_SAFETY_FEE = 2.00
    COMMONWEALTH_FUND_FEE_A = 1.00
    COMMONWEALTH_FUND_FEE_B = 3.00

    total_price = (base_price * tax_percentage) + base_price

    if state_abbreviation == "CA":
        total_price = (total_price * RECYCLING_FEE) + total_price
        return round(total_price, 1)

    elif state_abbreviation == "PA":
        total_price = total_price + HIGHWAY_SAFETY_FEE
        return round(total_price, 1)

    elif state_abbreviation == "MA":

        if total_price < 100:
            return round(total_price + COMMONWEALTH_FUND_FEE_A, 1)

        else:
            return round(total_price + COMMONWEALTH_FUND_FEE_B, 1)

    else:
        return total_price


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

# def arbitrary_list(lst, *args):
#     """Takes a list and an arbitrary amount of arguments and appends them to a list"""

#     for arg in args:
#         lst.append(arg)

#     #print lst
#     return lst

# arbitrary_list([1, 2, 3, 4, 5], 6, 7, 8, 9)

def arbitrary_list(lst, *args):
    """Takes a list and an arbitrary amount of arguments and appends them to a list"""

    lst.extend(arg for arg in args)
    print lst
    return lst

arbitrary_list([1, 2, 3, 4, 5], 6, 7, 8, 9)
arbitrary_list(["dog", "cat", "mouse"], "unicorn", "whale", "dolphin")

# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def make_this_multiple(word):
    """Takes in a word as a string."""

    def multiplier(x):
        """Triples the string of make_this_multiple."""

        x = 3
        return word * x

    return multiplier


times3 = make_this_multiple("hello")
print times3("hello")

###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
