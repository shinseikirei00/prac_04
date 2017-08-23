import random

MIN_PICK = 1
MAX_PICK = 45
number_of_picks = int(input("How many quick picks do you want?"))
number_of_rows = 0

while number_of_rows < number_of_picks:
    pick = []
    for n in range(5):
        number = random.randint(MIN_PICK, MAX_PICK)
        while number in pick:
            number = random.randint(MIN_PICK, MAX_PICK)

        pick.append(number)

    number_of_rows += 1

    output = " ".join(str(number) for number in pick)
    print(output)
