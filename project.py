import random
n = random.randint(1,100)
a = -1
guess = 1
while(a != n):
    a = int(input("Guess a number: "))
    if(a<n):
        guess += 1
        print("Higher number please!")
    elif(a>n):
        guess += 1
        print("Lower number please!")

print(f"You have guessed the number {n} correctly in {guess} attempts")
