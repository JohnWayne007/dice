import random  # import random library

# get input from the user
print("Welcome to 'roll the dice'")
i = int(input("\nEnter the maximum value of Dice: "))

want = "y"  

while want == "y":
    print(random.randrange(1, i+1, 1))
    want = input("Do you want to roll the dice again (y/n): ")

print("\nThank you for rolling the dice")

