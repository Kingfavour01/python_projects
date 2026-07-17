# SIWES Daily Activity and Progress Report

**Student:** Favour Ottache  
**Matric Number:** 24/SCI01/180  
**Institution:** Afe Babalola University (ABUAD)  
**Program Area:** Computer Science (200 Level)

---

## Week 1

---

### Day 1 (Week 1, Day 1) — Foundations of Python Programming and Control Flow

**Focus:** Python Programming Fundamentals, Algorithmic Logic, and Modular Design

**Activity Description:**
Engaged in a comprehensive practical training module focused on Python fundamentals, environment configuration, and basic program execution. Transitioned from theoretical syntax to practical application by developing introductory utility software, including an arithmetic calculator, metric converters (weight and temperature), and a text-processing email slicer.

**Key Concepts Learned:**

- **Memory Management & Data Types:** Understanding dynamic typing, variable initialization, and explicit type casting to manage memory states effectively.
- **Standard I/O Operations:** Capturing and sanitizing standard user input, and utilizing format specifiers for clean console output.
- **Control Structures:** Implementing logical operators and branching logic using `if/elif/else` statements and conditional expressions to dictate program flow based on user constraints.
- **String Manipulation:** Utilizing built-in string methods, zero-based indexing, and string slicing to parse and process textual data.

**Relevant Files:** `python calc.py`, `weight converter.py`, `temperature converter.py`, `email indexing.py`, `area calc.py`, `3d volume calc.py`

---

### Day 2 (Week 1, Day 2) — Iteration, Data Structures, and Algorithmic Logic

**Focus:** Iteration, Data Structures, and Algorithmic Logic

**Activity Description:**
Advanced to handling complex data states, repetitive tasks, and non-deterministic logic. Designed and executed interactive console applications that required sustained data states and user interaction. Projects included a financial interest calculator, a shopping cart system, and randomized simulation models (e.g., encryption program, dice roller, and logic-based games).

**Key Concepts Learned:**

- **Iterative Processing:** Controlling execution flow and timing cycles utilizing `while` loops, `for` loops, and nested loop architectures.
- **Data Structures (Collections):** Differentiating and deploying standard Python collections — Lists (mutable arrays), Tuples (immutable arrays), Sets (unique elements), and Dictionaries (key-value pairs) — for optimized data storage. Explored 2D collections for matrix-style data mapping.
- **Stochastic Processes:** Integrating Python's standard library modules to generate pseudorandom numbers, essential for building unpredictable program logic and simulations.
- **Applied Algorithmic Logic:** Combining loops, collections, and conditionals to construct stateful applications (such as a concession stand management system) and basic security concepts (encryption algorithms).

**Relevant Files:** `C.I calc 2.py`, `compound intrest calculator.py`, `shoping cart.py`, `shooping chart program.py`, `encyption device.py`, `dice.py`, `guessing number game.py`, `rock, papper , scissors.py`, `rock , paper , scissors v2.py`, `python quiz game.py`, `fizz buzz.py`, `timer.py`, `2d key pad.py`, `menu ( dictioinary practice).py`, `user_input validation.py`, `rectangle drawing.py`, `sentece gamr.py`

---

### Day 3 (Week 1, Day 3) — Modular Programming & Functions

**Focus:** Modular Programming and Function Design

**Activity Description:**
Focused on modular software design by creating reusable Python functions. Practical exercises involved abstracting repetitive logic and utilizing advanced parameter handling — including default arguments, keyword arguments, and variable-length argument lists — to build highly scalable and dynamic code.

**Key Concepts Learned:**

- **Function Construction:** Defining and invoking reusable code blocks to improve overall script maintainability and reduce code duplication.
- **Default Arguments:** Implementing fallback parameter values using default arguments, allowing functions to be called with fewer arguments than defined.
- **Keyword Arguments:** Enhancing function call clarity and flexibility by passing arguments explicitly by parameter name, eliminating positional dependency.
- **Dynamic Data Handling (`*args` & `**kwargs`):** Utilizing `*args` (packed as tuples) and `**kwargs` (packed as dictionaries) to seamlessly process unpredictable or variable amounts of user inputs.

**Relevant Files:** `shipping function.py`, `function to create full name.py`, `function to genrate phone number.py`, `odd or even function.py`, `timer using function.py`, `number extractor.py`

---

## Week 2

---

### Day 4 (Week 2, Day 1) — Advanced Iteration and Code Organization

**Focus:** Advanced Data Filtering, Structural Pattern Matching, and Program Architecture

**Activity Description:**
Transitioned into writing more efficient, "Pythonic" code. The focus of today's practical sessions shifted from basic loops to advanced iteration techniques and cleaner control flow. Additionally, the training introduced program architecture, focusing on how to organize large codebases across multiple files and manage variable lifespans in memory.

**Key Concepts Learned:**

- **Iterables & Membership Operators:** Utilized Python's built-in membership operators (`in`, `not in`) to efficiently search for elements within iterables (lists, strings, tuples) in a single line, bypassing the need for manual loop construction.
- **List Comprehensions:** Applied functional programming concepts to generate, map, and filter lists dynamically. Replaced verbose standard `for` loop blocks with concise, single-line comprehensions to improve both script execution speed and readability.
- **Structural Pattern Matching:** Implemented Python's modern `match-case` statements as a cleaner, more readable alternative to deep `if/elif/else` conditional chains when evaluating a single variable against multiple potential states.
- **Program Architecture (Modules & Scope):**
  - **Modules:** Abstracted logic into separate `.py` files and imported them into a main execution script, establishing the foundation for building scalable, multi-file software.
  - **Scope Resolution:** Studied the LEGB (Local, Enclosing, Global, Built-in) rule to understand how the Python interpreter searches for variable names in memory, preventing namespace collisions and bugs when passing data between functions and modules.
  - **`if __name__ == '__main__'` Guard:** Learned to use the script entry-point pattern to differentiate between reusable module code and standalone execution logic, preventing unintended code from running during import.

**Relevant Files:** `match case.py`

---

### Day 5 (Week 2, Day 2) — Real-World Algorithms and State Management

**Focus:** Applied Algorithmic Logic and Stateful Application Development

**Activity Description:**
Focused on synthesizing previous knowledge of loops, collections, and functions into fully functional, interactive console applications. The session involved building software that required continuous user interaction, strict input validation, and persistent data states. Projects included a mathematically driven credit card validator, a session-based banking program, and logic-heavy simulations (Slot Machine and Hangman).

**Key Concepts Learned:**

- **Algorithmic Implementation:** Engineered a credit card validation script by translating standard mathematical protocols (like the Luhn algorithm) into Python logic. This required advanced string parsing, step-based iteration, and arithmetic tracking.
- **State Management & Session Loops:** Built continuous execution loops (`while True`) for the banking and slot machine programs. Successfully managed persistent data variables (such as a user's account balance) that dynamically updated across multiple transactions and rounds of play without resetting.
- **Input Validation & Error Prevention:** Implemented strict logical checks to sanitize user inputs. Prevented software crashes and illegal states (e.g., blocking negative monetary deposits, catching invalid menu selections, and handling repeated letter guesses in Hangman).
- **Dynamic Game Logic & String Masking:** Utilized sets and lists to track user history (guessed letters) and applied string manipulation to create dynamic visual states, rendering real-time UI updates in the terminal for the Hangman game. Applied matrix-style printing and probability logic for the slot machine grid.

**Relevant Files:** `credit card validation.py`, `banking function.py`, `slot machine.py`, `hangman.py`, `word_list.py`

---

### Day 6 (Week 2, Day 3) — Comprehensive Software Architecture and Algorithmic Logic

**Focus:** Object-Oriented Architecture, Algorithmic Thinking, and Memory Management

**Activity Description:**
Today's session was highly intensive, merging architectural software design (Object-Oriented Programming) with deep algorithmic theory and memory management. The practical exercises involved not only structuring code using class hierarchies but also optimizing execution logic, managing how data is stored in memory, and translating mathematical concepts into recursive functions.

**Key Concepts Learned & Applied:**

**1. Object-Oriented Programming (OOP) & Architectures:**

- **Classes and Object Instantiation:** Transitioned from functional scripts to object-oriented structures, utilizing the `__init__` constructor and `self` keyword to encapsulate state and behavior.
- **Class vs. Instance Variables:** Differentiated between class-level attributes (shared across all instances) and instance-level attributes (unique to each object), understanding their memory allocation and lookup precedence.
- **Inheritance & Hierarchy:** Implemented inheritance (including multiple inheritance) to share logic between parent and child classes. Utilized the `super()` function to proxy initialization logic upward through the class tree.
- **Polymorphism & Abstraction:** Enforced structural rules using Abstract Base Classes (preventing raw parent instantiation) and explored Duck Typing, where an object's suitability is determined by its available methods rather than its explicit class type.
- **Composition vs. Aggregation:** Modeled structural relationships, differentiating between strong dependencies (Composition) and weak references (Aggregation) between objects.

**2. Core Algorithmic Thinking & Control Flow:**

- **Circuit-Level Logic:** Visualized `and`/`or` boolean operators as series and parallel logical gates (short-circuiting logic) to optimize complex conditional pathways.
- **Index-Based vs. Direct Iteration:** Analyzed loop efficiencies. Used direct element iteration (`for item in list`) for read-only operations, and index-based iteration (`for i in range(...)`) for in-place memory modifications.
- **Nested Loop Dependencies:** Constructed complex nested loops where the inner loop's boundary is dynamically dependent on the outer loop's current state, directly applicable to matrix operations and combinatorial logic.

**3. Memory Management & Execution Contexts:**

- **Pass by Value vs. Pass by Reference:** Explored computer architecture fundamentals regarding how Python handles variables. Learned that lightweight primitives (integers, strings) are passed *by value* (copied), while heavyweight collections (lists, dictionaries) are passed *by reference* (pointers to the memory heap), meaning mutations inside functions affect the global state.
- **Scope Resolution (The Sandbox):** Traced variable lifespans within function execution frames (local scope vs. global scope) and analyzed how functions evaluate arguments—specifically during function composition (e.g., `f(g(x))`).

**4. Advanced Data Mapping & Recursion:**

- **Relational Data (Dictionaries):** Implemented dictionaries for highly efficient, associative `key:value` pair mapping (e.g., tracking character occurrences in a large dataset), bypassing the linear search limitations of standard lists.
- **Recursive Algorithms:** Transitioned from iterative loops to recursive function design. Engineered functions that call themselves to solve progressively smaller subsets of a problem (e.g., computing factorials or reversing strings), mastering the "base case" termination logic and the "recursive leap of faith."

**Relevant Files:** `car.py`, `oject oriented programming.py`

---

### Day 7 (Week 2, Day 4) — Advanced System Operations, Metaprogramming, and Performance Profiling

**Focus:** Advanced Object-Oriented Mechanics, System I/O Operations, and Temporal Software Utilities

**Activity Description:**
Today's training module marked a significant transition from writing isolated logic scripts to engineering robust, production-ready software that directly interacts with the host operating system. The practical session was divided into three major phases: deeply extending Object-Oriented Programming (OOP) architectures, safely handling external file streams, and mastering time-based computations. The training culminated in building a real-time terminal application — an Alarm Clock — while profiling code to ensure execution efficiency.

**Key Concepts Learned & Applied:**

**1. Advanced Object-Oriented Architecture & Metaprogramming:**

- **Composition & Nested Classes:** Moved beyond basic inheritance to model complex "Part-Of" relationships. Learned how to tightly couple objects using Composition (where the child object cannot exist without the parent object) and utilized Nested Classes to keep the global namespace clean and logically organized.
- **Method Scoping (`@staticmethod` & `@classmethod`):** Differentiated class behaviors. Implemented `@classmethod` to create alternative constructors that modify class-level states, and `@staticmethod` to attach utility functions to a class without requiring an instantiated object or altering class states.
- **Magic (Dunder) Methods:** Explored Python's internal data model by overriding double-underscore methods (e.g., `__str__`, `__eq__`, `__add__`). This allowed custom objects to interact natively with built-in Python operators, such as adding two custom objects together using the standard `+` symbol.
- **Decorators & Data Encapsulation:** Mastered the use of function decorators to dynamically alter the behavior of functions without permanently modifying their source code. Specifically, applied the `@property` decorator to enforce strict data encapsulation, allowing private variables to be accessed and modified safely via hidden getter and setter methods.

**2. Functional Utilities & Data Stream Manipulation:**

- **Lambda Functions:** Deployed anonymous, single-line lambda functions for quick, throwaway logical operations. These were particularly useful when providing custom sorting keys for complex data structures.
- **Advanced Sorting & `zip()`:** Implemented dynamic sorting algorithms to arrange complex datasets in ascending/descending order based on specific object attributes. Utilized the `zip()` function to pair and iterate through multiple independent lists simultaneously, drastically reducing the need for complex index tracking.
- **Recursion (Review):** Reinforced the principles of recursive logic, ensuring a solid understanding of base cases and the call stack memory limits.

**3. System-Level Operations: File I/O & Exception Management:**

- **Graceful Error Handling (`try`/`except`/`finally`):** Engineered crash-resistant software. Instead of allowing runtime errors to crash the entire application, implemented exception handling blocks to catch specific errors (like `ValueError` or `ZeroDivisionError`), log them, and execute fallback logic safely.
- **File Detection & Streams:** Interacted with the host OS using the `os` module to verify file path existence before attempting operations.
- **Reading & Writing Files:** Opened data streams to write (`w`), append (`a`), and read (`r`) external text files. Emphasized the use of context managers (`with open(...)`) to ensure file streams are automatically closed after execution, preventing memory leaks and file corruption.

**4. Chronometrics & Practical Application:**

- **Date & Time Manipulation:** Utilized Python's `datetime` module to fetch the current system time, format temporal data into human-readable strings, and calculate time deltas.
- **Execution Time Profiling:** Conducted software benchmarking using the `time` module. Measured the exact start and end times of functions to calculate their execution speed down to the millisecond, which is critical for optimizing slow algorithms.
- **Practical Project (Alarm Clock):** Synthesized all temporal logic into building a live Alarm Clock application. Engineered a `while True` loop combined with `time.sleep(1)` to actively poll the operating system's clock without consuming excessive CPU resources, triggering an alert event when the target time was successfully matched.

**Relevant Files:** `alarm clock.py`, `calc execution speed.py`, `file detecton.py`, `file manipulation.py`, `python sorting.py`, `recusion.py`, `output.txt`, `text.txt`
