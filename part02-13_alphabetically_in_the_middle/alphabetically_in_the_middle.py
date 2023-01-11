letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")
middle = letter1

if (letter2 < letter1 and letter2 > letter3) or (letter2 > letter1 and letter2 < letter3):
    middle = letter2
elif (letter3 < letter1 and letter3 > letter2) or (letter3 > letter1 and letter3 < letter2):
    middle = letter3

print(f"The letter in the middle is {middle}")