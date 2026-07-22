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

---

## Week 3

---

### Day 8 (Week 3, Day 1 — Monday) — WordPress CMS & LearnPress AI Integration

**Focus:** Content Management Systems and E-Learning Platform Configuration

**Activity Description:**
Transitioned from Python programming into full-fledged web content management by setting up and configuring a WordPress site from the ground up. The session focused on understanding the architecture of Content Management Systems (CMS) and how they differ from static websites. Installed WordPress, navigated the admin dashboard, and customized themes and plugins. The latter half of the session was dedicated to the LearnPress plugin, a powerful Learning Management System (LMS) for WordPress. Configured its AI-powered features to automate course content generation, quiz creation, and student analytics, building a functional e-learning platform ready for course delivery.

**Key Concepts Learned & Applied:**

**1. WordPress CMS Fundamentals:**

- **Installation & Configuration:** Set up a WordPress instance, configured database connections, and completed the initial setup wizard to establish a working site.
- **Dashboard Navigation:** Explored the WordPress admin panel including posts, pages, media library, comments, appearance (themes/customizer), and plugins sections.
- **Theme Customization:** Installed and activated themes, customized site identity (titles, logos, taglines), and adjusted layout settings to match branding requirements.
- **Page/Post Management:** Created and organized static pages (About, Contact, Home) and dynamic blog posts with categories, tags, and featured images.

**2. Plugin Architecture & LearnPress LMS:**

- **Plugin Installation:** Sourced, installed, and activated plugins from the WordPress Plugin Directory, understanding how plugins extend core CMS functionality.
- **LearnPress Setup:** Installed the LearnPress LMS plugin and its required add-ons (LearnPress AI, LearnPress Course Review, LearnPress Assignments).
- **Course Creation:** Designed complete course structures including course outlines, lesson plans, curriculum sections, and lesson content with multimedia embedding.
- **Quiz & Assessment Engine:** Created quizzes with multiple question types (multiple choice, true/false, fill-in-the-blank), set passing grades, and configured retake policies.

**3. LearnPress AI Features:**

- **Automated Content Generation:** Leveraged LearnPress AI to auto-generate lesson summaries, course descriptions, and quiz questions from topic keywords, dramatically reducing manual content creation time.
- **Intelligent Recommendations:** Configured AI-driven course recommendations for students based on their browsing history, completed lessons, and quiz performance.
- **Student Analytics:** Used AI-powered dashboards to track student engagement, completion rates, and identify at-risk learners for intervention.

**4. E-Learning Structure & Workflow:**

- **Course Hierarchy:** Modeled the standard LMS hierarchy — Courses → Sections → Lessons → Quizzes — and understood how each level interacts with student progress tracking.
- **Enrollment Management:** Set up manual and automatic enrollment methods, including paid course gateways and free access links.
- **Progress Tracking:** Monitored student progress through the built-in LearnPress reporting tools, tracking lesson completion, quiz scores, and course certificates.

---

### Day 9 (Week 3, Day 2 — Tuesday) — Advanced Python Iteration, Concurrency, API Integration & GUI Development

**Focus:** Iterators, Generators, Dataclasses, Multithreading, API Requests, and PyQt5 GUI

**Activity Description:**
Covered a broad range of advanced Python topics in a single intensive session, spanning memory-efficient iteration protocols, data class optimization for cleaner code, concurrent programming for performance gains, REST API consumption for live data, and graphical user interface development with PyQt5. The practical component involved building multiple GUI applications from scratch — starting with basic labeled windows, progressing through image displays and layout managers, and culminating in interactive widgets including push buttons and checkboxes connected to real event handlers.

**Key Concepts Learned & Applied:**

**1. Advanced Iteration & Memory Optimization:**

- **Iterators:** Understood the iterator protocol (`__iter__` and `__next__` methods) and how Python's `for` loop works under the hood by calling `iter()` on any iterable object to receive an iterator, then repeatedly calling `__next__()` until `StopIteration` is raised. Built custom iterator classes to control iteration behavior manually.
- **Generators:** Built memory-efficient generator functions using the `yield` keyword. Learned that generators produce values lazily — one at a time and only when requested — meaning they never store the entire sequence in memory, making them ideal for processing large datasets or infinite streams.
- **Generator Expressions:** Wrote compact, single-line generator expressions using parenthesis syntax `(x for x in iterable)`, similar to list comprehensions but producing values on-demand rather than building a full list in memory.

**2. Data Structures & Code Simplification:**

- **Dataclasses:** Utilized the `@dataclass` decorator from the `dataclasses` module to automatically generate boilerplate methods (`__init__`, `__repr__`, `__eq__`, `__hash__`). Reduced class definitions from 10+ lines of repetitive code down to a clean, declarative annotation. Applied field ordering, default values, and type hints for self-documenting data containers.

**3. Concurrency & Performance:**

- **Multithreading:** Implemented concurrent execution using Python's `threading` module. Created and started multiple `Thread` objects to run functions in parallel, significantly improving performance for I/O-bound tasks like network requests and file operations. Used `.join()` to synchronize thread completion and understood the Global Interpreter Lock (GIL) limitations for CPU-bound tasks.

**4. API Integration:**

- **REST API Requests:** Used the `requests` library to perform HTTP GET requests against live external web APIs. Parsed JSON responses into Python dictionaries, extracted specific data fields, and handled various HTTP status codes (200 OK, 404 Not Found, 500 Server Error) with conditional logic to prevent crashes from malformed or missing data.

**5. GUI Development with PyQt5:**

- **Basic GUI Setup & Event Loop:** Created a `QMainWindow` subclass as the application shell. Initialized a `QApplication` instance with `sys.argv`, entered the event loop via `app.exec_()`, and understood the event-driven programming model where the application waits for user interactions (clicks, key presses) to trigger callbacks.
- **Window Configuration:** Set window titles with `setWindowTitle()`, positioned and sized windows with `setGeometry()`, and assigned window icons using `QIcon` with image file paths.
- **Labels & Typography:** Displayed static and dynamic text using `QLabel`. Customized font family, size, weight, and style using `QFont`, and applied inline stylesheets for text color, background color, and text decoration (underline, italic).
- **Image Display:** Loaded external image files using `QPixmap` and displayed them within `QLabel` widgets. Used `setScaledContents(True)` to control image scaling behavior within the label bounds.
- **Layout Managers:** Organized widget placement using `QVBoxLayout` (vertical stacking), `QHBoxLayout` (horizontal arrangement), and `QGridLayout` (row/column grid). Understood how layout managers automatically handle resize events and widget spacing, eliminating the need for hard-coded geometry.
- **Push Buttons & Signals:** Created `QPushButton` widgets and connected their `clicked` signal to custom slot methods using `.clicked.connect()`. Built event handlers that dynamically changed button text, disabled buttons after click, and printed output to the console on interaction.
- **Checkboxes & Toggle Input:** Implemented `QCheckBox` widgets for boolean/toggle user inputs. Connected state change signals to handler functions that read the checked state and triggered conditional logic.

**Relevant Files:** `gui.py`, `push button.py`, `how to connect to api.py`

---

### Day 10 (Week 3, Day 3 — Wednesday) — Advanced PyQt5 Widgets & Qt Style Sheets

**Focus:** Radio Buttons, Line Edits, and Qt Style Sheet (CSS) Styling

**Activity Description:**
Today's session extended PyQt5 GUI development by introducing three critical components for building interactive, professional-looking desktop applications. Implemented radio buttons for mutually exclusive selection, line edits for text input capture, and Qt Style Sheets (QSS) — PyQt5's equivalent of CSS — for complete visual customization of widget appearance, layout spacing, and hover/focus states.

**Key Concepts Learned & Applied:**

**1. Radio Buttons (`QRadioButton`):**

- **Mutually Exclusive Selection:** Implemented `QRadioButton` widgets within a `QButtonGroup` to enforce single-selection behavior, where selecting one radio button automatically deselects all others in the same group.
- **State Detection:** Connected the `toggled` signal to custom slot methods to detect which radio button is currently selected and trigger corresponding actions.
- **Use Case Mapping:** Applied radio buttons for preference selection (e.g., choosing payment methods, difficulty levels, or category filters) where only one option from a set should be active.

**2. Line Edits (`QLineEdit`):**

- **Text Input Capture:** Used `QLineEdit` widgets to accept single-line text input from the user. Connected the `textChanged` and `returnPressed` signals to capture input in real-time or on submission.
- **Input Modes & Validation:** Configured different input modes including password masking (`setEchoMode(QLineEdit.Password)`), numeric-only input, and read-only fields.
- **Placeholder & Styling:** Set placeholder text with `setPlaceholderText()` and applied stylesheet rules for focused, unfocused, and error states.
- **Data Extraction:** Retrieved entered text using `.text()` method and passed it to other parts of the application for processing or display.

**3. Qt Style Sheets (QSS / CSS):**

- **QSS Syntax:** Applied Cascading Style Sheet rules to PyQt5 widgets using `.setStyleSheet()`. Used CSS-like syntax with selectors, properties, and values — targeting specific widgets by class name, object name, or type.
- **Visual Customization:** Styled widget backgrounds (`background-color`), text colors (`color`), borders (`border`, `border-radius`), padding, and margins. Applied hover effects using `:hover` pseudo-state and focus indicators with `:focus`.
- **Nested & Combined Selectors:** Targeted specific widgets within layouts using descendant selectors (e.g., `QPushButton#myButton` for a named button, or `QWidget QLabel` for labels inside a specific container).
- **Consistent Theming:** Applied global stylesheets at the `QApplication` level to enforce a consistent theme across all widgets in the application, mimicking the separation of structure (Python) and presentation (CSS) found in web development.

**Relevant Files:** *(pending — new PyQt5 widget demos)*
