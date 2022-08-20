#Count the number of vowels of the input
def vowelCount(data):
    count = 0
    for letter in stringD:
        if letter == "a":
            count = count + 1
        if letter == "e":
            count = count + 1
        if letter == "i":
            count = count + 1
        if letter == "o":
            count = count + 1
        if letter == "u":
            count = count + 1
        if letter == "A":
            count = count + 1
        if letter == "E":
            count = count + 1
        if letter == "I":
            count = count + 1
        if letter == "O":
            count = count + 1
        if letter == "U":
            count = count + 1
    print(data + str(count))

#Reverse the case of each character of input
def reverseCase(data):
    reverseC = stringD.swapcase()
    print(data + stringD + "' is '" + reverseC + "'." )

#Reverse the word of the input
def reverseWord(data):
    reversedW = "".join(reversed(stringD))
    print(data + stringD + "' is '" + reversedW + "'.")

#Ask the user of he/she wants to try again
def tryAgain():
    while True:
        tryA = input("Do you want to try again? (y/n): ")
        if tryA == "y":
            return True
        elif tryA == "n":
            return False
        else:
            print("Wrong Input")
            continue

#Main Program
while True:
    print("-------------- Word Play --------------")
    stringD = input("Enter String Data: ")
    vowelCount("Number of Vowels: ")
    reverseCase("Reversing the case of '")
    reverseWord("Reverse of '")
    if tryAgain() == False:
        break