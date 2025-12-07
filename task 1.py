import random
pool = ["apple", "robot", "magic", "india", "light"]
secret = random.choice(pool)
used = []
lives = 6
print("=== Hangman ===")
while lives > 0:
  
    show = ""
    for ch in secret:
        if ch in used:
            show += ch + " "
        else:
            show += "_ "
    print("\nWord:", show)

    if "_" not in show:
        print("\nYou guessed it! Word was:", secret)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one alphabet letter.")
        continue

    if guess in used:
        print("Already tried that letter.")
        continue

    used.append(guess)

    if guess in secret:
        print("Nice! Correct letter.")
    else:
        lives -= 1
        print("Wrong! Lives left:", lives)

if lives == 0:
    print("\nOut of chances! The word was:", secret)
