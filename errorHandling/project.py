

def collatz(number):
    #if number is even, then collatz() should print number//2 and return this value
    #if number is odd, then collatz() should print and return 3*number+1
    #write a program that lets the user type in an int and that keeps calling collatz
        #until the function returns the value1
    try:
        number = int(number)
    except ValueError:
        print("Wrong value: Please enter an integer.")

        
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1


number = input("Enter a number: \n")
while (number!=1):
    number = collatz(number)
    
        




