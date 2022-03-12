number = input('Write a number: ')

intNumber = int (number)
sum = int(0)

def collatz (number, sum):
    if (number%2==0):
        num = int (number/2)
    else:
        num = int ((number*3)+1)
    
    sum = int (sum + 1)      
    print(f"{sum} >>> {num}")
    
    if (num != 1):
        collatz(num, sum)
        
collatz(intNumber, sum)
