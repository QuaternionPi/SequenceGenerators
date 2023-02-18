import time

def mod_test(number, modulus):
    return number % modulus == 0

def assert_test(number, message, test, *args):
    result = test(number, *args)
    if(result == True):
        print(message)
    
    return result
    
number = 1
maximum = 100
while number <= maximum:
    test_passed = False
    if test_passed == False:
        test_passed = assert_test(number, "FizzBuzz", mod_test, 15)
    if test_passed == False:
        test_passed = assert_test(number, "Fizz", mod_test, 3)
    if test_passed == False:
        test_passed = assert_test(number, "Buzz", mod_test, 5)
    if test_passed == False:
        print(number)

    number += 1

input()

