import random
from termcolor import colored


words = list(open("words.txt", "r"))
word = random.choice(words).strip()
display = ["_", "_", "_", "_", "_"]
win = False


for i in range(6):
    print("".join(display))
    display = ["_", "_", "_", "_", "_"]
    answer = ""
    while answer + "\n" not in words:
        answer = input("Input your guess: ")
    if answer == word:
        win = True
        break
    else:
        for letter in range(5):
            if answer[letter] == word[letter]:
                display = list(display)
                display[letter] = colored(word[letter], "green")
            else:
                if answer[letter] in word:
                    display[letter] = colored(answer[letter], "yellow")
                    


print("You win!") if win == True else print("You lose, The word was: " + word)