# Ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low):

    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:
        try:
            # Ask the user for a number
            response = int(input(question))

            # Check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Main routine goes here
for item in range(0, 1):
    integer = int_check("Integer: ", 0)
    print(integer)

for item in range(0, 1):
    width = int_check("Width: ", 1)
    print(width)

print()

for item in range(0, 1):
    height = int_check("Height: ", 1)
    print(height)
