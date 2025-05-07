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
        response = requests.get("https://random-word-api.herokuapp.com/word?lang=pt-br&number=10")
        if response.status_code == 200:
            words = response.json()
            # Filter out any non-alphabetic words and convert to uppercase
            words = [word.upper() for word in words if word.isalpha()]
            if words:
                return words
            else:
                print("Nenhuma palavra coletada. Retornando a lista padrão de palavras.")
        else:
            print("Erro ao coletar palavras. Retornando a lista padrão de palavras.")
    except Exception as e:
        print(f"Erro: {e}. Usando lista padrão de palavras.")
    
    # Expanded default word list
    return [
        "LISTA", "DE", "PALAVRAS", "AQUI"
    ]

# Victory function
def victory(word):
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"\nVocê Venceu! A palavra era: {word}\n")
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
        print(f"Não foi possível tocar a música de vitória: {e}")
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
    print("Regras: Advinhe a palavra, uma letra por vez. Você tem {attempts} tentativas para acertar.")

    while attempts > 0:
        os.system('clear' if os.name != 'nt' else 'cls')
        print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - attempts])
        print("\nWord: ", " ".join([letter if letter in correct_guesses else "_" for letter in word]))
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        guess = input("Enter a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Entrada inválida. Por favor insira uma letra do alfabeto.")
            time.sleep(1.5)
            continue

        if guess in guessed_letters:
            print("Você já utilizou essa letra. Tente novamente.")
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
                print(f"Não foi possível tocar o som: {e}")
            attempts -= 1

    # Final state after all attempts used
    os.system('clear' if os.name != 'nt' else 'cls')
    print(HANGMAN_PICS[-1])
    print("\nGAME OVER! The word was:", word)
    try:
        playsound('game_over.mp3')  # Optional: Add a game over sound
    except Exception as e:
        print(f"Não foi possível tocar o som: {e}")
    retry()

# Retry function
def retry():
    while True:
        choice = input("\nDeseja jogar novamente?? (s/n): ").lower()
        if choice == 's':
            start_game()
            break
        elif choice == 'n':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Opção inválida. Por favor insira 's' or 'n'.")

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
