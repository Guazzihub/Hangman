import random
import os
import time
import requests
from playsound import playsound

# Hangman stages
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

# Function to fetch words from an online source
def fetch_words():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=10")
        if response.status_code == 200:
            words = response.json()
            # Filter out any non-alphabetic words and convert to uppercase
            words = [word.upper() for word in words if word.isalpha()]
            if words:
                return words
            else:
                print("No valid words fetched. Falling back to default word list.")
        else:
            print("Error fetching words. Falling back to default word list.")
    except Exception as e:
        print(f"Error: {e}. Using default word list.")
    
    # Expanded default word list
    return [
        "PYTHON", "DEVELOPER", "PROGRAM", "DEBUG", "ALGORITHM",
        "FUNCTION", "VARIABLE", "CONDITION", "LOOP", "STRING",
        "INTEGER", "BOOLEAN", "LIST", "TUPLE", "DICTIONARY",
        "COMPUTER", "KEYBOARD", "SOFTWARE", "HARDWARE", "NETWORK",
        "DATABASE", "FRAMEWORK", "LIBRARY", "SYNTAX", "COMPILER"
    ]

# Victory function
def victory(word):
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"\nYOU WON! The word was: {word}\n")
    print(r'''
                 /__\
               /|    |\
              (_|    |_)
                 \  /
                  )(
                _|__|_
              _|______|_
             |__________|
    ''')
    try:
        playsound('victory.mp3')
    except Exception as e:
        print(f"Could not play victory sound: {e}")
    time.sleep(3)
    retry()

# Main game function
def start_game():
    words = fetch_words()
    word = random.choice(words).upper()
    guessed_letters = []
    attempts = len(HANGMAN_PICS) - 1  # Number of attempts based on hangman stages
    correct_guesses = set()

    print("\n---------------------------------------------------------WELCOME---------------------------------------------------------\n")
    print("Rules: Guess the word one letter at a time. You have {attempts} attempts to get it right.")

    while attempts > 0:
        os.system('clear' if os.name != 'nt' else 'cls')
        print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - attempts])
        print("\nWord: ", " ".join([letter if letter in correct_guesses else "_" for letter in word]))
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        guess = input("Enter a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabetic letter.")
            time.sleep(1.5)
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            time.sleep(1.5)
            continue

        guessed_letters.append(guess)

        if guess in word:
            correct_guesses.add(guess)
            if all(letter in correct_guesses for letter in word):
                victory(word)
                return
        else:
            try:
                playsound('error.mp3')
            except Exception as e:
                print(f"Could not play error sound: {e}")
            attempts -= 1

    # Final state after all attempts used
    os.system('clear' if os.name != 'nt' else 'cls')
    print(HANGMAN_PICS[-1])
    print("\nGAME OVER! The word was:", word)
    try:
        playsound('game_over.mp3')  # Optional: Add a game over sound
    except Exception as e:
        print(f"Could not play game over sound: {e}")
    retry()

# Retry function
def retry():
    while True:
        choice = input("\nDo you want to play again? (y/n): ").lower()
        if choice == 'y':
            start_game()
            break
        elif choice == 'n':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

# Entry point of the game
if __name__ == "__main__":
    # Check for required sound files
    required_sounds = ['victory.mp3', 'error.mp3', 'game_over.mp3']
    missing_sounds = [sound for sound in required_sounds if not os.path.isfile(sound)]
    if missing_sounds:
        print("Warning: The following sound files are missing:")
        for sound in missing_sounds:
            print(f" - {sound}")
        print("The game will continue without these sounds.")
    start_game()
