# Asks users for file type (integer/image/text/***)
def get_filetype():
    response = input("File Type: ").lower()

    # Check for 'i' or the exit code
    if response == "xxx" or response == "i":
        return response

    # Checks if it's an integer
    elif response in ['integer', 'int']:
        return "integer"

    # Checks if it's an image
    elif response in ['image', 'picture', 'img']:
        return "image"

    # Checks if it's text
    elif response in ['text', 'txt', 't']:
        return "text"

    # If the response is invalid output an error
    else:
        print("PLease enter a valid file type")


# Main routine goes here
while True:
    file_type = get_filetype()
    print(f"You chose {file_type}")
