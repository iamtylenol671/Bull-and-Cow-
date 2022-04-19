import random


def numRandom():
    secret_numbers = str(random.randint(1000, 9999))
    if len(set(secret_numbers)) != len(secret_numbers):
        numRandom()
    return secret_numbers


print('Secret Number is contain 4 digit.')

bulls = 0
cows = 0
secret_number = numRandom()

while True:
    player_number = str(input('Your Number: '))

    for i in range(len(secret_number)):

        if player_number[i] == secret_number[i]:
            bulls += 1

        elif player_number[i] in secret_number:
            cows += 1

    if bulls == len(secret_number):
        print('Your win!!!')
        print(secret_number)
        print(f"{bulls} Bulls and {cows} Cows")
        break
    else:
        print(f"{bulls} Bulls and {cows} Cows")

    bulls -= bulls
    cows -= cows