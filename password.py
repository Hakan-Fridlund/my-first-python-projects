"""
Assignment: Write a program where the user gets to write a password. the program should:
1 Have at correct password stored in the code.
2 Let the user try it multiple times, commonly 3 tries
3 Handle errors, which means:
if the user writes something that is not a sting, fex presses enter directly -> handle it
if the user writes the wrong password -> give a clear error message
if the user writes the correct password -> close directly
Give a message when out of tries
use try/except to catch errors like: empty input, disrupted input et.c.
"""
password = "Gecko"

def log_in(prompt):
    attempts = 0
    while True:
        try:
            attempt = input(prompt)
            if attempt == password:
                print("You are logged in")
                break
        except ValueError:
            print("faulty input")
        else:
            attempts += 1
            if attempts >= 3:
                print("Your account is locked, too many login attempts!")
                break
            print(f"Wrong password, you have {3-attempts} attempts left")

def main():
    log_in("Write your password: ")


main()
