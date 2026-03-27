import random

# Word list
words = ["apple", "mango", "grape", "peach", "lemon"]

# Random word selection
word = random.choice(words)

# Blank display
display = ["_"] * len(word)

# Chances
chances = 6

print("🎮 Welcome to Hangman Game!")

# Game loop
while chances > 0:
    print("\nWord:", " ".join(display))
    print("Remaining chances:", chances)

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Enter only ONE letter!")
        continue

    # Check correct guess
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        chances -= 1
        print("❌ Wrong guess!")

    # Win condition
    if "_" not in display:
        print("\n🎉 You Win! The word was:", word)
        break

# Lose condition
if chances == 0:
    print("\n💀 Game Over! The correct word was:", word)