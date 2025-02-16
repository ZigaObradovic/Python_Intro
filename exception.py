
try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't devide by zero")
except ValueError:
    print("Enter only numbers please")
# except Exception 
except Exception:
    print("Something went wrong!")
finally:
    print("do some cleanup here")
