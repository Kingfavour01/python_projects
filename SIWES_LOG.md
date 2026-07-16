# SIWES Daily Activity and Progress Report

**Student:** Favour Ottache  
**Matric Number:** 24/SCI01/180  
**Institution:** Afe Babalola University (ABUAD)  
**Program Area:** Computer Science (200 Level)

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
