Title: **Flashcards learning application**

Technical implementation: **Under the hood, the app features mainly a HashMap demonstrative implementation, with a linkedlist based on the extensive class of Node.**

Description: The game/application is desgined to be accessed from within the command line (at main.py); it is supposed to touch on the following points:

1. Have a clean implementation where each component is smoothly integrated into the ensemble.
2. The actual data defintion that the hashmap and application work with/operate on is a dictionary; alternatively the data could be served from a lightweight database.
3. Compared to other games/apps that I have wrote, the error handling is not so strong here, yet the minimum is basically implemented (like, for example the user input).
4. The flashcards are displayed in a loop (a given timed sequence). The user can stop the game with a simple 'Ctrl + C' which is meant to triggered the 'KeyboardInterrupt' exception. This plays nicely on the defaults of the command line (which should work for either Windows cli or Linux/Mac OS ones). I hid the exception details upon the game termination, so the game termination is a bit more simplistic and elegant.

Disclaimer: Everything listed here is free and has the purpose of serving as a training/educational resource for the current GitHub user (the author).

