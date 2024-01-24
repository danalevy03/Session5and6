import random
lives = 3

while True:
    print("you have", lives, "lives left")
    dice_roll = random.randint(1,6)
    if lives == 0:
        print("you lost all your lives, game over")
        break
    if dice_roll == 6:
        print("you rolled a 6, you win!")
        break
    print("you rolled a", dice_roll, "try again")
    lives -= 1

