'''
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the
number and for the multiples of five print "Buzz". For
numbers which are multiples of both three and five
print "FizzBuzz".

Sample output:
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
'''

def fizzbuzz(n: int):
    ''' Descrição '''
    pass


def main():
    numbers = [fizzbuzz(n) for n in range(1, 101)]
    print(*numbers, sep='\n')


if __name__ == '__main__':
    main()