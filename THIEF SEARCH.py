# function to determine the current location of a thief
def collatz_search(starting_house_number, days_passed):
    # set first house thief hid to variable, number
    number = starting_house_number
    # set day thief hid in first house, day 1 to variable,day_num
    day_num = 1
    # loops through days from day 1 till days_passed
    while day_num <= days_passed:
        # sets number to (n/2)th house if current house number is even
        if number % 2 == 0:
            number = number/2
        # sets number to (3n + 1)th house if current house number is odd
        else:
            number = 3*number + 1
        # increments days by one till it gets to days_passed
        day_num += 1
    # returns house number that the thief is currently hiding in
    return number


print(collatz_search(7, 9))


