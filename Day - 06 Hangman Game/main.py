import random

stages = [
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    =========
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    =========
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    =========
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    =========
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    =========
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    =========
    """,
    """
     ------
     |    |
     |
     |
     |
     |
    =========
    """
]

word_list = ["apple", "banana", "grape", "orange", "mango"]
computer_choice = random.choice(word_list)

display = ["-"] * len(computer_choice)
lives = 6

print("Welcome to Hangman Game!")

while lives > 0 and "-" in display:

    print("\nWord:", " ".join(display))

    # 👇 THIS is the key line (stage depends on lives)
    print(stages[6 - lives])

    user_input = input("Enter a letter: ").lower()

    if user_input in computer_choice:

        for i in range(len(computer_choice)):
            if computer_choice[i] == user_input:
                display[i] = user_input

    else:
        lives -= 1
        print("Wrong guess! Lives left:", lives)

# RESULT
if "-" not in display:
    print("\n🎉 You Win! Word was:", computer_choice)
else:
    print(stages[0])
    print("\n💀 You Lose! Word was:", computer_choice)