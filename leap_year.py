'''
Write a function that returns true or false depending on 
whether its input integer is a leap year or not.

A leap year is defined as one that is divisible by 4,
but is not otherwise divisible by 100 unless it is
also divisible by 400.

For example, 2001 is a typical common year and 1996
is a typical leap year, whereas 1900 is an atypical
common year and 2000 is an atypical leap year.
'''

def is_leap_year(n: int):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

def is_leap_year_no_if(n: int):
    return (n % 400 == 0) or ((n % 4 == 0) and not (n % 100 == 0))