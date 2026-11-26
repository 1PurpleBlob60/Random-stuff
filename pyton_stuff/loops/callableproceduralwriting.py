import time

def procedural_print(word, delay=0.5):
    for letter in word:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print()  # Moves to the next line when finished

# --- How to call it anywhere ---
'''procedural_print("Hello, world!")
procedural_print("Loading system...", delay=0.1)

# You can also still use it with user input:
user_word = input("Enter a word: ")
procedural_print(user_word)'''
