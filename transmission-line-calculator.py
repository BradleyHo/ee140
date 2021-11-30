# EE 140 course at San José State University (SJSU)
# CLI program to compute values for transmission line theory
# This program computes values for VSWR, ρ, RL
# https://github.com/BradleyHo

import math

# This function computes ρ from VSWR
def rcvswr(x):
    y = (x-1)/(x+1) # ρ
    return y
    
# This function computes RL from VSWR
def rlvswr(x):
    z = -20*math.log(rcvswr(x),10) if rcvswr(x) != 0 else "∞" # RL
    return z

# This function computes VSWR from ρ
def vswrrc(y):
    x = (1+y)/(1-y) if y != 1 else "∞" # VSWR
    return x
    
# This function computes RL from ρ
def rlrc(y):
    z = -20*math.log(y,10) if y != 0 else "∞"  # RL
    if z == 0:
        z = 0.0
    return z

# This function computes ρ from RL
def rcrl(z):
    y = math.pow(10, -z/20) # ρ
    return y

# This function computes VSWR from RL
def vswrrl(z):
    x = (1+rcrl(z))/(1-rcrl(z)) if z != 0 else "∞" # VSWR
    return x

# Tell the user our menu options
print("Select a given parameter below to solve for the two others:")
print("1. Voltage standing wave ratio - VSWR")
print("2. Reflection coefficient - ρ = |Γ|")
print("3. Return loss - RL (dB)")
print("___________________________________________________________")

while True:
    # Take the input choice from the user
    choice = input("Enter choice (1/2/3):")

    # Check if the choice is valid: 1 of the 3 options
    if choice in ('1', '2', '3'):
        num1 = float(input("Enter the value for chosen parameter:"))

        # 1 input: VSWR
        # 2 outputs: ρ, RL
        if choice == '1':
            print("Given: VSWR =", num1)
            print("ρ =", rcvswr(num1))
            print("RL =", rlvswr(num1), "dB")

        # 1 input: ρ
        # 2 outputs: VSWR, RL
        elif choice == '2':
            print("VSWR =", vswrrc(num1))
            print("Given: ρ =", num1)
            print("RL =", rlrc(num1), "dB")

        # 1 input: RL
        # 2 outputs: VSWR, ρ
        elif choice == '3':
            print("VSWR =", vswrrl(num1))
            print("ρ =", rcrl(num1))
            print("Given: RL =", num1, "dB")
        
        # Check if the user wants another calculation
        # Repeatedly ask the user to enter a valid option yes or no (y/n) if input does not match 
        # Break the while loop if answer is n
        # Otherwise, the default is y to continue the next calculation
        next_calculation = input("Perform another calculation? (y/n):")
        while next_calculation.lower() not in ("y","n"):
            next_calculation = input("Invalid input. Enter choice (y/n): ")
        if next_calculation == "n":
            print("I hope it was useful. Good luck in EE 140!")
            break
    # Within the main while loop, accept either 1 of the 3 choices from the user if it is valid
    # Otherwise, repeatedly ask the user to input 1 or 2 or 3 (1/2/3) if the input does not match
    else:
        print("Invalid input. Enter (1/2/3):")