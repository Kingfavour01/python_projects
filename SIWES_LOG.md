# SIWES Daily Activity and Progress Report

**Student:** Favour Ottache  
**Matric Number:** 24/SCI01/180  
**Institution:** Afe Babalola University (ABUAD)  
**Program Area:** Computer Science (200 Level)

---

## Week 1

---

### Day 1 (Week 1, Day 1 — Wednesday, July 8) — Foundations of Python Programming and Control Flow

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

### Day 2 (Week 1, Day 2 — Thursday, July 9) — Iteration, Data Structures, and Algorithmic Logic

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

### Day 3 (Week 1, Day 3 — Friday, July 10) — Modular Programming & Functions

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

### Day 4 (Week 2, Day 1 — Tuesday, July 14) — Advanced Iteration and Code Organization

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

### Day 5 (Week 2, Day 2 — Wednesday, July 15) — Real-World Algorithms and State Management

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

### Day 6 (Week 2, Day 3 — Thursday, July 16) — Comprehensive Software Architecture and Algorithmic Logic

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

### Day 7 (Week 2, Day 4 — Friday, July 17) — Advanced System Operations, Metaprogramming, and Performance Profiling

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

### Day 8 (Week 3, Day 1 — Monday, July 20) — WordPress CMS & LearnPress AI Integration

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

### Day 9 (Week 3, Day 2 — Tuesday, July 21) — Advanced Python Iteration, Concurrency, API Integration & GUI Development

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

### Day 10 (Week 3, Day 3 — Wednesday, July 22) — Advanced PyQt5 Widgets & Qt Style Sheets

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

---

### Day 11 (Week 3, Day 4 — Thursday, July 23) — Real-Time GUI Applications: Digital Clock & Stopwatch

**Focus:** PyQt5 QTimer, Real-Time Updates, and Time-Based GUI Applications

**Activity Description:**
Focused on building real-time, dynamically updating PyQt5 applications driven by the `QTimer` class. Engineered a live digital clock that continuously refreshes every second by polling the system time and updating a `QLabel` widget. Extended the timer concept to build a full-featured stopwatch with start, stop, and reset functionality, requiring precise state management and millisecond-level accuracy.

**Key Concepts Learned & Applied:**

**1. QTimer & Real-Time Updates:**

- **`QTimer` Initialization:** Created `QTimer` objects and configured them to emit `timeout` signals at fixed intervals (e.g., every 1000ms for a clock, every 10ms for a stopwatch).
- **Signal-Slot Connection:** Connected the `QTimer.timeout` signal to custom update methods that refresh GUI elements with current time values.
- **Polling vs. Blocking:** Understood that `QTimer` integrates with PyQt5's event loop, allowing continuous time updates without blocking the main application thread.

**2. Digital Clock Application:**

- **System Time Retrieval:** Used `datetime.now()` to fetch the current system hour, minute, and second, then formatted into a human-readable `HH:MM:SS` string.
- **Dynamic Label Updates:** Continuously updated a `QLabel` display using `setText()` every second via `QTimer`, creating a live clock feel.
- **Visual Styling:** Applied custom fonts and stylesheets to render the clock with a digital display aesthetic, including colored text, background gradients, and font sizing.

**3. Stopwatch Application:**

- **Elapsed Time Tracking:** Used `QTimer` at 10ms intervals to increment a running elapsed time counter. Stored elapsed milliseconds and converted to `minutes:seconds.milliseconds` display format.
- **State Machine Logic:** Implemented three distinct states — Stopped, Running, and Paused — managed through boolean flags and button enable/disable logic to prevent invalid operations (e.g., starting an already-running timer).
- **Start/Stop/Reset Buttons:** Created `QPushButton` widgets for Start, Stop, and Reset with conditional logic. Start began the timer, Stop paused it while preserving elapsed time, and Reset cleared all counters back to zero.
- **Elapsed Time Formatting:** Calculated elapsed time using modular arithmetic — hours = elapsed // 3600, minutes = (elapsed % 3600) // 60, seconds = elapsed % 60 — then formatted with zero-padding for consistent digit width.

**Relevant Files:** `digital clock.py`, `stopwatch.py`

---

### Day 12 (Week 3, Day 5 — Friday, July 24) — API-Powered Apps, QR Code Generation & Audio Playback

**Focus:** REST API Integration, QR Code Encoding, and Multimedia with Pygame

**Activity Description:**
Concluded Week 3 with three diverse, practical projects that integrated external services and multimedia capabilities. Built a weather application that fetches live meteorological data from a public API and renders it in a styled PyQt5 interface. Created a QR code generator that encodes arbitrary text or URLs into scannable 2D barcode images using the `qrcode` library. Finally, developed a music player application using `pygame-ce` mixer to load, play, pause, and navigate through audio files from the filesystem.

**Key Concepts Learned & Applied:**

**1. Weather App (API Integration):**

- **REST API Consumption:** Sent HTTP GET requests to the OpenWeatherMap API endpoint, passing location-based query parameters (`q=city&appid=api_key`). Parsed the JSON response into a Python dictionary to extract key fields: temperature, humidity, weather description, and wind speed.
- **Temperature Conversion:** Applied the formula `(temp - 273.15) * 9/5 + 32` to convert Kelvin (default API unit) to Fahrenheit for user-friendly display.
- **Error Handling for APIs:** Implemented `try/except` blocks and HTTP status code checks. Handled `KeyError` for invalid city names, `requests.ConnectionError` for network failures, and displayed user-friendly error messages in the GUI rather than crashing.
- **PyQt5 UI Integration:** Built a weather dashboard using `QLineEdit` for city input, `QPushButton` for triggering the API call, and multiple `QLabel` widgets styled with weather-appropriate icons and colors to display results.

**2. QR Code Generator:**

- **`qrcode` Library:** Used the `qrcode.make()` function to encode any string or URL into a QR code matrix. Saved the resulting image using the Pillow (`PIL`) backend with `.save()`.
- **QR Code Configuration:** Customized QR code parameters including `box_size` (pixel size per module), `border` (white space margin), and `error_correction` level to balance scannability with image dimensions.
- **File Output:** Generated QR code images as PNG files, displaying them in a `QLabel` with `QPixmap` after generation for immediate visual feedback.

**3. Music Player (Pygame Mixer):**

- **Pygame Mixer Initialization:** Called `pygame.mixer.init()` to set up the audio subsystem with appropriate sample rate and buffer size for MP3/WAV playback.
- **File Loading & Playback:** Used `pygame.mixer.music.load(filepath)` to load an audio file and `pygame.mixer.music.play()` to begin playback. Implemented `pause()`, `unpause()`, and `stop()` for full playback control.
- **Volume & Progress:** Adjusted playback volume using `set_volume()` (0.0 to 1.0). Queried playback position with `get_pos()` for progress tracking.
- **Playlist Management:** Dynamically listed `.mp3` files from a local directory using `os.listdir()`, allowing the user to select and switch between tracks during a session.
- **Button-Driven Interface:** Built a simple playback control panel with Play, Pause, Stop, Next, and Previous buttons connected to mixer functions via `QPushButton` clicked signals.

**Relevant Files:** `weather app.py`, `qr code.py`, `music player.py`

---

## Week 4

---

### Day 13 (Week 4, Day 1 — Monday, July 27) — Off Day

No activity scheduled.

---

### Day 14 (Week 4, Day 2 — Tuesday, July 28) — Linux Fundamentals & Fedora 44 Upgrade

**Focus:** Operating Systems, Command-Line Proficiency, and System Administration

**Activity Description:**
Transitioned into systems-level computing by exploring the Linux operating system environment. The session covered fundamental command-line operations, the Linux file system hierarchy, user and permission management, and package handling. Culminated in performing a full system upgrade from an earlier Fedora release to Fedora 44, understanding the update lifecycle and post-upgrade system verification.

**Key Concepts Learned & Applied:**

**1. Linux Terminal & Command-Line Fundamentals:**

- **Shell Navigation:** Used essential terminal commands to traverse the file system — `pwd` (print working directory), `ls` (list directory contents with flags like `-la` for detailed views), `cd` (change directory), and `mkdir`/`rmdir` for directory creation and removal.
- **File Operations:** Performed file creation (`touch`), copying (`cp`), moving/renaming (`mv`), and deletion (`rm`). Understood the difference between relative and absolute paths when referencing files.
- **File Viewing & Editing:** Used `cat`, `less`, and `head`/`tail` to view file contents. Became familiar with `nano` as a simple terminal-based text editor for configuration files.

**2. File System Structure & Permissions:**

- **Linux Directory Hierarchy:** Explored the standard Linux file system layout including `/home` (user data), `/etc` (configuration files), `/var` (logs and variable data), `/usr` (user binaries), and `/tmp` (temporary files).
- **Permission Model:** Understood the `rwx` (read, write, execute) permission structure for Owner, Group, and Others. Used `chmod` with symbolic notation (`u+x`, `g-w`) and octal values to modify access rights.
- **User Management:** Differentiated between the root superuser and standard user accounts. Used `sudo` to execute privileged commands securely.

**3. Package Management & System Updates:**

- **DNF Package Manager:** Used Fedora's native `dnf` package manager to search for packages (`dnf search`), install software (`dnf install`), remove packages (`dnf remove`), and check for available updates (`dnf check-update`).
- **Repository Configuration:** Understood how software repositories work as centralized sources for trusted, pre-compiled packages and how they are configured under `/etc/yum.repos.d/`.
- **Full System Upgrade:** Performed a `dnf system-upgrade` to migrate from an older Fedora version to Fedora 44. Followed the multi-step process: download upgrade packages, reboot into upgrade mode, and verify the new release with `cat /etc/fedora-release` and `uname -r`.

**4. Post-Upgrade Verification:**

- **System Health Check:** Verified successful upgrade by confirming the kernel version, checking that all services were running, and ensuring previously installed applications and configurations were preserved.
- **Rollback Awareness:** Learned the importance of backups and understood that `dnf history undo` can revert transactions if an upgrade introduces instability.

---

### Day 15 (Week 4, Day 3 — Wednesday, July 29) — Sick Day

Absent due to illness. No activity recorded.

---

### Day 16 (Week 4, Day 4 — Thursday, July 30) — Sick Day

Absent due to illness. No activity recorded.

---

### Day 17 (Week 4, Day 5 — Friday, July 31) — WordPress E-Commerce Store with WooCommerce & WhatsApp Integration

**Focus:** E-Commerce Platform Configuration, Product Management, and Client Communication

**Activity Description:**
Built a fully functional demo e-commerce store on WordPress using the WooCommerce plugin. Configured the core store settings including currency, tax rules, and shipping zones. Created product listings with images, pricing tiers, inventory tracking, and category organization. Set up the shopping cart and checkout flow, and integrated WhatsApp as a direct client communication channel so customers can instantly message the store owner with order inquiries.

**Key Concepts Learned & Applied:**

**1. WooCommerce Setup & Configuration:**

- **Plugin Installation:** Installed and activated WooCommerce from the WordPress plugin directory. Completed the setup wizard including store location, currency selection (NGN or USD), and industry classification.
- **Store Settings:** Configured payment gateways (Cash on Delivery, Direct Bank Transfer), shipping zones with flat rate pricing, tax rules, and email notification templates for order confirmations.
- **Pages Auto-Generation:** Allowed WooCommerce to automatically create essential store pages — Shop (product listing), Cart (review before checkout), Checkout (billing and order summary), and My Account (customer login and order history).

**2. Product Management & Inventory:**

- **Product Creation:** Created both simple and variable products with SKU numbers, regular and sale prices, product descriptions, short descriptions for listing pages, and featured images.
- **Categories & Tags:** Organized products into hierarchical categories (e.g., Electronics, Clothing, Accessories) and applied descriptive tags for improved store navigation and searchability.
- **Inventory Tracking:** Enabled stock management at the product level. Set stock quantities and configured backorder settings to prevent overselling on out-of-stock items.

**3. Shopping Cart & Checkout Flow:**

- **Cart Functionality:** Tested the end-to-end user journey — browsing the shop, adding items to cart, updating quantities, applying coupon codes, and proceeding to checkout.
- **Checkout Configuration:** Customized the checkout form fields, enabled guest checkout for faster conversions, and configured order success/error messaging.

**4. WhatsApp Integration for Client Communication:**

- **WhatsApp Click-to-Chat Plugin:** Installed a WhatsApp chat plugin that adds a floating WhatsApp button to the storefront. Configured the plugin with the client's phone number and customized the default greeting message.
- **Order Notification Workflow:** Set up the chat button on product pages so customers can inquire about specific items directly. Configured the checkout confirmation page with a WhatsApp link for customers to confirm orders or request delivery updates.
- **Direct Link Generation:** Understood the WhatsApp Click-to-Chat API URL structure (`https://wa.me/234XXXXXXXXXX?text=Message`) to manually embed WhatsApp links in product descriptions, order confirmation emails, and the contact page.

---

## Week 5

---

### Day 20 (Week 5, Day 3 — Wednesday, August 5) — Remote Access Infrastructure: Tailscale VPN, opencode Web Deployment, and Secure Mobile Connectivity

**Focus:** Virtual Private Networking, Secure Service Deployment, Reverse Proxying, and Cross-Platform Documentation

**Activity Description:**
Deployed a fully secured remote-access stack so the opencode AI coding environment can be operated from a phone anywhere, restricted to a private virtual network. Installed the Tailscale mesh VPN on Fedora 44, joined it to an existing tailnet, and enabled MagicDNS with HTTPS certificate provisioning. Ran the opencode web interface as a user-level systemd service bound strictly to `127.0.0.1:4096` with password authentication via environment variables. Exposed that service across the tailnet using Tailscale's HTTPS reverse proxy (`tailscale serve`) so the phone reaches it through the encrypted VPN rather than exposing a public port. Configured boot persistence with linger so the stack survives reboots. Verified end-to-end connectivity from Android clients (OpenRemote and MobileCode) over the tailnet. Concluded by authoring a step-by-step Windows setup runbook so the same configuration can be reproduced on another machine.

**Key Concepts Learned:**

- **Mesh VPN (Tailscale/WireGuard):** Understood how an overlay network creates encrypted point-to-point tunnels between devices without port forwarding, and how devices are addressed by stable tailnet IPs and MagicDNS hostnames (e.g., `fedora.tail6a788d.ts.net`).
- **MagicDNS & HTTPS Certificates:** Learned that enabling HTTPS in the tailnet lets Tailscale auto-provision TLS certificates for the serve URL, giving browser/phone clients a valid cert with zero manual setup.
- **Secure Service Deployment (systemd user unit):** Created and enabled a user-level systemd service (`opencode-web.service`) for the web server, managed via `systemctl --user`, with credentials supplied through an environment file rather than command-line flags.
- **Loopback Binding:** Bound the server to `127.0.0.1` so it is unreachable from the LAN directly — only reachable through the authorized reverse proxy. Direct LAN access returns connection refused by design.
- **Reverse Proxying over the VPN:** Used `tailscale serve --bg --https=443 http://127.0.0.1:4096` to terminate HTTPS at the tailnet edge and forward to the loopback service, restricting access to devices already in the tailnet.
- **Boot Persistence (`loginctl enable-linger`):** Learned how user services start automatically after reboot without a login session.
- **Mobile Client Integration:** Configured and verified third-party Android clients (OpenRemote, MobileCode) against the same authenticated endpoint, confirming the URL, username, and password flow.

**Relevant Files:** `REMOTE-PHONE-ACCESS-WINDOWS.md`, `~/.config/systemd/user/opencode-web.service`, `~/.config/systemd/user/opencode-web.env`

---

### Learning Experience — WhatsApp-to-opencode Integration (Documented, Not Re-solved)

An earlier attempt to bridge WhatsApp messaging into the opencode environment was explored and ultimately discontinued. The approach required a WhatsApp Business/Cloud API, a public tunnel (ngrok) to receive webhook callbacks, and browser automation (Chrome DevTools Protocol) to drive the agent's interface — a fragile chain of external services that did not prove practical for this use case. This is recorded here as a learning experience in API integration, webhook handling, and tunnel-based connectivity rather than a resolved feature. The experience informed the decision to favour a private, first-party remote-access path (this session's Tailscale-based setup) over a third-party messaging bridge.

---

*End of Week 5 (Days 18–19 pending) records.*
