import random
secret_number = random.randint(1, 100)

attempts = 0
while True:
    guss_number = int(input("Guss the number: "))
    attempts += 1

    if secret_number < guss_number :
        print("Too High")

    elif secret_number > guss_number:
        print("Too Low")

    else:
        print("Congratulation")
        print(f"Your gussed it in {attempts} attempts! ")
        break
