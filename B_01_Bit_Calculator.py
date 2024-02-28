# Generates heading (e.g. ***** Heading *****
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Please choose a data type (image/text/integer)
This program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). 
For text, we assume that ascii encoding is being used (8 bits per character).
Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit. 
    ''')


# Asks users for file type (integer/image/text/***)
def get_filetype():

    while True:
        response = input("File Type: ").lower()

        # Check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # Checks if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # Checks if it's an image
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        # Checks if it's text
        elif response in ['text', 'txt', 't']:
            return "text"

        # If the response is invalid output an error
        else:
            print("PLease enter a valid file type")


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


# Calculate how many bits are needed to represent an image
def image_calc():
    # Get the image dimensions
    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)

    # Calculate the number od pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # Set up answer and return it
    answer = (f"Number of pixels: {width} x {height} = {num_pixels}"
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")
    return answer


# Calculate how many bits are needed to represent an image
def integer_calc():
    # Ask the user to enter an integer (more than/equal to 0)

    integer = int_check("Integer: ", 0)

    # Convert the integer to binary and work out the number of bits needed
    raw_binary = bin(integer)

    # Remove the leading '0b' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # Set up answer and return it
    answer = f"{integer} in binary is {binary}. We need {num_bits} bits to represent it."

    return answer


# Calculate number of bits needed to represent text in ascii
def calc_text_bits():

    # Get text from user
    response = input("Enter some text: ")

    # Calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"{response} has {num_chars} characters."
              f"\n We need {num_chars} x 8 bits to represent it"
              f"\n which is {num_bits} bits")
    return answer


# Main routine goes here

# Display instructions if required
want_instructions = input("Press <enter> to read the instructions or any key to continue")

if want_instructions == "":
    instructions()
while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    # If user chose 'i', ask if they want an image/integer
    if file_type == 'i':
        want_image = input("Press <enter> for an integer or any key for an image")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)

    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)

    else:
        text_ans = calc_text_bits()
        print(text_ans)


