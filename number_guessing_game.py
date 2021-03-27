import random
lb = int(input("Enter lower bound: "))
ub = int(input("Enter upper bound: "))

n = random.randint(lb, ub)
guess_limit = (20)
count = 0
while guess_limit > 0:
    guess_limit -= 1
    count += 1
    guess = int(input("Guess the number: "))
    if guess == n:
        print("Congratulations! You won!!")
        print("You have guessed the number in " + str(count) + " times")
        break
    if guess > n:
        print("Number is lesser than this.")
    if guess < n:
        print("Number is greater than this.")
    if guess_limit == 0:
        print("You loose!")
        print("The number is ", n)
    
