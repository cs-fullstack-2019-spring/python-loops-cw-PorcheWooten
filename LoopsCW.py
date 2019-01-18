def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()

# Print -20 to and including 50. Use any loop you want.

def problem1():
    for negNums in range(-20,51):
        print(negNums)


# Create a loop that prints even numbers from 0 to and including 20.

def problem2():
    for evenNums in range(0,21,2):
        print(evenNums)

# Prompt the user for 3 numbers.
# Then print the 3 numbers along with their average after the 3rd number is entered.
# Refer to example below replacing ```NUMBER1```, ```NUMBER2```, ```NUMBER3```, and ```THEAVERAGE``` with the actual values.

def problem3():
    num1 = int(input("Enter number 1 "))
    num2 = int(input("Enter number 2 "))
    num3 = int(input("Enter number 3 "))
    sum = (num1 + num2 + num3)
    avg = (sum / 3)
    print("The average of " + str(num1) + ", " + str(num2) + ", " + str(num3) + " is " + str(avg))


# Password Checker - Ask the user to enter a password.
# Ask them to confirm the password.
# If it's not equal, keep asking until it's correct or they enter 'Q' to quit.

def problem4():
    while True:
        password = input("Enter password ")
        password2 = input("Reenter password ")
        if password != password2:
               print("TRY AGAIN!!!")
        elif password2 == "q":
                break




if __name__ == '__main__':
    main()