# Python Projects — Internship Portfolio

**Student:** Favour Ottache  
**Matric Number:** 24/SCI01/180  
**Institution:** Afe Babalola University (ABUAD)

This repository documents the basic Python tasks assigned during my internship programme. It serves as a practical record and defence portfolio, demonstrating my understanding of core Python concepts including variables, conditionals, loops, functions, data structures, string manipulation, user input validation, randomisation, and error handling.

---

## Projects

### Calculators

| Project | Description |
|---|---|
| `area calc.py` | Computes the area of a rectangle by multiplying user-provided length and width. |
| `3d volume calc.py` | Computes the volume of a rectangular prism using length, width, and height inputs. |
| `C.I calc 2.py` | Compound interest calculator with while-loop input validation (checks for negative values). |
| `compound intrest calculator.py` | Alternate compound interest calculator using while-loops with `<= 0` validation. |
| `python calc.py` | Basic arithmetic calculator supporting addition, subtraction, multiplication, and division. |
| `temperature converter.py` | Converts between Celsius, Fahrenheit, and Kelvin based on user-selected unit. |
| `weight converter.py` | Converts weight between pounds (lb) and kilograms (kg) using a fixed conversion factor. |

### Games

| Project | Description |
|---|---|
| `guessing number game.py` | Random number guessing game (1–20) with hints to go higher or lower. |
| `python quiz game.py` | Multiple-choice quiz with 4 questions, tracks score and shows results as a percentage. |
| `rock, paper, scissors.py` | Rock Paper Scissors (v1) — single round against the computer with nested conditionals. |
| `rock, paper, scissors v2.py` | Rock Paper Scissors (v2) — replayable with a play-again loop. |
| `dice.py` | Dice-rolling simulator that displays ASCII art dice and sums the total. |
| `fizz buzz.py` | Prints numbers 1–100, substituting "Fizz" for multiples of 3, "Buzz" for 5, and "FizzBuzz" for both. |
| `sentece gamr.py` | Mad Libs-style word game: fills user-provided nouns and adjectives into a zoo-themed story. |

### Utility Programs

| Project | Description |
|---|---|
| `2d key pad.py` | Displays a 2D keypad layout (1–9, *, 0, #) using nested lists and loops. |
| `email indexing.py` | Extracts the username and domain from an email address using the string `.index()` method. |
| `encyption device.py` | Substitution cipher using a shuffled character set — encrypts and decrypts messages. |
| `number extractor.py` | Validates a credit card number (16 digits) and checks the card carrier name (Visa/Mastercard). |
| `function to genrate phone number.py` | Formats a phone number from user-provided country code, area code, and digits. |
| `function to create full name.py` | Capitalises and combines a first and last name using a function. |
| `odd or even function.py` | Checks whether a given number is odd or even using the modulo operator. |
| `shipping function.py` | Demonstrates `*args` and `**kwargs` by printing a formatted shipping label. |
| `shopping cart.py` | Simple cart that calculates total price from item name, unit price, and quantity. |
| `shooping chart program.py` | Shopping list app — collects items and prices until the user quits, then displays the total. |
| `menu (dictioinary practice).py` | Restaurant menu system using a dictionary to look up item prices and build a cart. |
| `timer.py` | Countdown timer in HH:MM:SS format with `time.sleep()`. |
| `timer using function.py` | Countdown timer implemented as a reusable function with start/end parameters. |
| `user_input validation.py` | Validates a username for length (> 12), spaces, and non-alphabetic characters. |
| `rectangle drawing.py` | Draws a rectangle of user-specified rows, columns, and symbol using nested loops. |
| `match case.py` | Demonstrates Python structural pattern matching (`match-case`) as an alternative to `if/elif/else` chains. |
| `word_list.py` | Word bank used by the Hangman game for random word selection. |

### Stateful Applications & Algorithms

| Project | Description |
|---|---|
| `credit card validation.py` | Validates credit card numbers using the Luhn algorithm with step-based string parsing. |
| `banking function.py` | Session-based banking program with persistent balance and deposit/withdrawal transactions. |
| `slot machine.py` | Slot machine simulation with probability logic, matrix-style grid printing, and balance tracking. |
| `hangman.py` | Hangman game with real-time string masking, guessed letter tracking via sets, and input validation. |

### Object-Oriented Programs

| Project | Description |
|---|---|
| `car.py` | Demonstrates OOP fundamentals with a Car class including attributes and methods. |
| `oject oriented programming.py` | Illustrates class instantiation, inheritance, and the `self` keyword. |
| `journal.py` | Personal journal app with OOP, file I/O, `@property`, dataclass-style entries, search, and mood tracking. |

### System Operations & File I/O

| Project | Description |
|---|---|
| `alarm clock.py` | Real-time alarm clock using `datetime` and `time.sleep()` polling loop. |
| `calc execution speed.py` | Benchmarks function execution time using the `time` module. |
| `file detecton.py` | Checks file path existence using the `os` module before performing operations. |
| `file manipulation.py` | Reads, writes, and appends to external text files using context managers. |
| `python sorting.py` | Demonstrates advanced sorting with lambda functions, custom keys, and `zip()`. |
| `recusion.py` | Reinforces recursive logic with base case termination and call stack management. |

### API & Web
| Project | Description |
|---|---|
| `how to connect to api.py` | Fetches live data from REST APIs using the `requests` library and parses JSON responses. |

### GUI Applications (PyQt5)

| Project | Description |
|---|---|
| `gui.py` | PyQt5 GUI demo with QVBoxLayout, colored labels, and widget management. |
| `push button.py` | PyQt5 button demo with click events, dynamic text changes, and button disabling. |

---

## Getting Started

1. Make sure Python 3 is installed:
   ```
   python --version
   ```
2. Clone the repo:
   ```
   git clone https://github.com/Kingfavour01/python_projects.git
   ```
3. Run any project:
   ```
   python "area calc.py"
   ```

## Requirements

- Python 3.x
- `requests` — for API calls (`how to connect to api.py`)
- `PyQt5` — for GUI applications (`gui.py`, `push button.py`)
- `pygame-ce` — for game development

---

## SIWES Daily Activity Log

Detailed daily activity and progress reports for the internship programme are documented in [`SIWES_LOG.md`](SIWES_LOG.md).

---

*Built during internship programme at Afe Babalola University (ABUAD).*
