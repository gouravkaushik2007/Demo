import random
n = random.randint(1,100)
a = -1
guess = 1
while(a != n):
    a = int(input("Guess a number: "))
    guess += 1
    if(a<n):
        print("Higher number please!")
    elif(a>n):
        print("Lower number please!")

print(f"You have guessed the number {n} correctly in {guess} attempts")

