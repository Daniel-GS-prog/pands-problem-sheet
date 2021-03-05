# Reads in a text file and outputs the number of e's it contains.
# Author : Daniel Gonzalez


filename = "text-with-e.text"

def getCharacter(n):
    with open(filename, "r") as f:
        data = f.read()
        # Read function passed as an argument
        lenChar = 0
        for char in data:
            # looping through the characters in file
            if char == n:
            # if characters match
                lenChar += 1
        return "\n The number of times '{}' appears in '{}' is: {}. \n".format(n, filename, lenChar)

print(getCharacter("e"))
    