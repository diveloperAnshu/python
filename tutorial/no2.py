while True:
    try:
        x=int(input("enter any number: "))
        
    except ValueError:
        print("Not an Integer.")
    else:
        break


print(f"the number entered is: {x}.")