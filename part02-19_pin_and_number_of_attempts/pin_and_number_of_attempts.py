attempts = 0
while True:
    attempts += 1
    if 4321 == int(input("PIN: ")):
        break
    print("Wrong")

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")