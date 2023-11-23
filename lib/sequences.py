#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []

    if length <= 0:
        print(fibonacci_list)
    elif length == 1:
        fibonacci_list.append(0)
        print(fibonacci_list)
    elif length==2:
        fibonacci_list.append(0)
        fibonacci_list.append(1)
        print(fibonacci_list)
    else:
        fibonacci_list=[0,1]
        for length in range(2,10):
            next_number = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_number)
        print (fibonacci_list)   
 

print_fibonacci(10)