from pylab import *

values = []

number = input('Write a number: ')

intNumber = int(number)

def collatz(number):
    if (number % 2 == 0):
        num = int(number/2)
        values.append(num)
    else:
        num = int((number*3)+1)
        values.append(num)

    if (num != 1):
        collatz(num)
        
collatz(intNumber)
plot(values)
xlabel('Iterations')
ylabel('Values')
title(f'Collatz Conjecture Graph || Number: {number}')
draw()
show()
