def div42by(num):
    try:
        return 42/num
    except ZeroDivisionError:
        print("Can't divide by zero!")
 

print(div42by(0))