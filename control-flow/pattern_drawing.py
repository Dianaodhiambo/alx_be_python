# Prompt the user to enter a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a variable for the while loop to iterate through each row
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks side by side
    for _ in range(size):
        print("*", end="")
    # Print a newline character to move to the next row
    print()
    # Move to the next row
    row += 1
