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

**Relevant Files:** `C.I calc 2.py`, `compound intrest calculator.py`, `shopping cart.py`, `shooping chart program.py`, `encryption device.py`, `dice.py`, `guessing number game.py`, `rock, paper, scissors.py`, `rock, paper, scissors v2.py`, `python quiz game.py`, `fizz buzz.py`, `timer.py`, `2d key pad.py`, `menu (dictioinary practice).py`, `user_input validation.py`, `rectangle drawing.py`, `sentece gamr.py`

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
