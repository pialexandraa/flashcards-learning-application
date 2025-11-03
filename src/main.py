from hash_map import HashMap
from definitions import flashcards_data
import time
import os
import sys
import random

#clear the screen
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  return

#dynamic function for updating text with delay/'a print with delay'
def timed_print(message, type_delay=0.03, message_delay=6):
  for character in message:
    print(character, end='', flush=True)
    time.sleep(type_delay)
  time.sleep(message_delay)
  return

def main():
  timed_print("Welcome to the mini game for learning new concepts!\nWe use flashcards to help you learn new things.\n")
  
  while True:
    user_input = input("Press Enter to start the game!\n")
    if user_input == "":
      break
    timed_print("Invalid input!\nStopping the game.")
    clear_screen()
  timed_print("Starting the game...\n")
  instance_1 = HashMap(len(flashcards_data))
  timed_print("Next, you will be shown a series of concepts to learn. First, you will see the term, and after 6 seconds, you will see its definition.\nTo stop the game at any time, press Ctrl + C!")
  clear_screen()

  try:
    all_definitions = list(flashcards_data.items())
    random.shuffle(all_definitions)
    for concept, definition in all_definitions:
      instance_1.assign(concept, definition)
      timed_print(f"Concept: {concept}\n")
      timed_print(f"Definition: {definition}")
      clear_screen()
  except KeyboardInterrupt: #the 'Ctrl + C' signal should raise the KeyboardInterrupt exception
    print("\nGame stopped by user. Exiting...")
    sys.exit(0)
  return

if __name__ == "__main__":
  main()