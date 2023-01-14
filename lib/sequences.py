#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []
    if length > 0:
        fibonacci_sequence.append(0)
        if length > 1: 
            fibonacci_sequence.append(1)
        if length > 2: 
            for index in range(2, length):
                fibonacci_sequence.append(
                    fibonacci_sequence[index - 1] + fibonacci_sequence[index - 2])
                        #taking the last element of the index and adding second to last element of the index
    print(fibonacci_sequence)
            