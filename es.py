# Reads in a text file and outputs the count of "e".
# Author : Daniel Gonzalez

def getCharacter(file, n):
    with open(file, "r") as f:
        data = f.read()
        # Read function passed as an argument
        lenChar = 0
        for char in data:
            # looping through the characters in file
            if char == n:
            # if characters match
                lenChar += 1
        return "\n The number of times '{}' appears in '{}' is: {}. \n".format(n, "text-with-e.text", lenChar)


print(getCharacter("text-with-e.text", "e"))
    # Passing the file name as an argument as per Professor's comment