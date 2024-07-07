# Ask the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Loop from 1 to 10
for i in range(1, 11):
    # Calculate the product
    result = number * i
    # Print the multiplication result
    print(f"{number} * {i} = {result}")
