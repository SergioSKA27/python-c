import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="Python",
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

r"""
Indice:

    1. Introducción
       1.1. algoritmos
        1.2. El lenguaje de programación Python
        1.3. Más sobre los programas
            1.3.1. Vista previa de estructuras de control
        1.4. Lenguajes formales y naturales
        1.5. Un primer programa típico
        1.6. Comentarios
        1.7. Glosario



    2. Variables, declaraciones y expresiones

    Variables, sentencias y expresiones

        2.2. Valores y tipos de datos
        2.3. Operadores y operandos
        2.4. Llamadas de función
            2.4.1. Llamadas a funciones como parte de expresiones complejas
            2.4.2. Las funciones son objetos; los paréntesis invocan funciones
        2.5. Tipos de datos
        2.6. Funciones de conversión de tipos
        2.7. Variables
        2.8. Nombres de variables y palabras clave
        2.9. 👩‍💻 Elegir el nombre de variable correcto
        2.10. Declaraciones y Expresiones
        2.11. Orden de operaciones
        2.12. reasignación
            2.12.1. Desarrollando tu modelo mental de cómo evalúa Python
        2.13. Actualización de variables
        2.14. 👩‍💻 Codificación dura

    3. Debugging
        3.1. Introduction to Debugging
            3.1.1. Learning Goals
            3.1.2. Objectives
        3.2. 👩‍💻 Programming in the Real World
        3.3. 👩‍💻 Debugging
            3.3.1. How to Avoid Debugging
        3.4. 👩‍💻 Beginning tips for Debugging
        3.5. Syntax errors
        3.6. Runtime Errors
        3.7. Semantic Errors
            3.7.1. Test Cases
        3.8. 👩‍💻 Know Your Error Messages
            3.8.1. SyntaxError
            3.8.2. TypeError
            3.8.3. NameError
            3.8.4. ValueError
        3.9. Exercises
            3.9.1. Contributed Exercises
    4. Python Modules
        4.1. Introduction to Python Modules
            4.1.1. Learning Goals
            4.1.2. Objectives
        4.2. Modules
            4.2.1. Importing Modules
            4.2.2. Syntax for Importing Modules and Functionality
        4.3. The random module
        4.4. Glossary
        4.5. Exercises
            4.5.1. Contributed Exercises
    5. Python Turtle
        5.1. Hello Little Turtles!
            5.1.1. Learning Goals
            5.1.2. Objectives
        5.2. Our First Turtle Program
        5.3. Instances: A Herd of Turtles
        5.4. Object Oriented Concepts
            5.4.1. User-defined Classes
            5.4.2. Instances
            5.4.3. Attributes
            5.4.4. Methods
        5.5. Repetition with a For Loop
        5.6. A Few More turtle Methods and Observations
        5.7. Summary of Turtle Methods
        5.8. 👩‍💻 Incremental Programming
        5.9. 👩‍💻 Common turtle Errors
        5.10. Exercises
            5.10.1. Contributed Exercises
        5.11. Chapter Assessment - Turtle and Object Mechanics
        5.12. Chapter Assessment - Drawing with Turtle
    6. Sequences
        6.1. Introduction: Sequences
            6.1.1. Learning Goals
            6.1.2. Objectives
        6.2. Strings and Lists
            6.2.1. Strings
            6.2.2. Lists
            6.2.3. Tuples
        6.3. Index Operator: Working with the Characters of a String
            6.3.1. Index Operator: Accessing Elements of a List or Tuple
        6.4. Disambiguating []: creation vs indexing
        6.5. Length
        6.6. The Slice Operator
            6.6.1. List Slices
            6.6.2. Tuple Slices
        6.7. Concatenation and Repetition
        6.8. Count and Index
            6.8.1. Count
            6.8.2. Index
        6.9. Splitting and Joining Strings
        6.10. Exercises
            6.10.1. Contributed Exercises
        6.11. Chapter Assessment
    7. Iteration
        7.1. Introduction: Iteration
        7.2. The for Loop
        7.3. Flow of Execution of the for Loop
        7.4. Strings and for loops
        7.5. Lists and for loops
            7.5.1. Using the range Function to Generate a Sequence to Iterate Over
            7.5.2. Iteration Simplifies our Turtle Program
        7.6. The Accumulator Pattern
        7.7. Traversal and the for Loop: By Index
        7.8. Nested Iteration: Image Processing
            7.8.1. The RGB Color Model
            7.8.2. Image Objects
            7.8.3. Image Processing and Nested Iteration
        7.9. 👩‍💻 Printing Intermediate Results
        7.10. 👩‍💻 Naming Variables in For Loops
        7.11. The Gory Details: Iterables
        7.12. 👩‍💻 Keeping Track of Your Iterator Variable and Your Iterable
        7.13. Glossary
        7.14. Exercises
            7.14.1. Contributed Exercises
        7.15. Chapter Assessment
    8. Conditionals
        8.1. Intro: What we can do with Turtles and Conditionals
            8.1.1. Learning Goals
            8.1.2. Objectives
        8.2. Boolean Values and Boolean Expressions
        8.3. Logical operators
            8.3.1. Smart Evaluation
        8.4. The in and not in operators
        8.5. Precedence of Operators
        8.6. Conditional Execution: Binary Selection
        8.7. Omitting the else Clause: Unary Selection
        8.8. Nested conditionals
        8.9. Chained conditionals
        8.10. The Accumulator Pattern with Conditionals
            8.10.1. Accumulating the Max Value
        8.11. 👩‍💻 Setting Up Conditionals
            8.11.1. Choosing your type of Conditional
        8.12. Glossary
        8.13. Exercises
            8.13.1. Contributed Exercises
        8.14. Chapter Assessment
    9. Transforming Sequences
        9.1. Introduction: Transforming Sequences
            9.1.1. Learning Goals
            9.1.2. Objectives
        9.2. Mutability
            9.2.1. Lists are Mutable
            9.2.2. Strings are Immutable
            9.2.3. Tuples are Immutable
        9.3. List Element Deletion
        9.4. Objects and References
        9.5. Aliasing
        9.6. Cloning Lists
        9.7. Mutating Methods
            9.7.1. List Methods
        9.8. Append versus Concatenate
        9.9. Non-mutating Methods on Strings
            9.9.1. String Format Method
        9.10. The Accumulator Pattern with Lists
        9.11. The Accumulator Pattern with Strings
        9.12. 👩‍💻 Accumulator Pattern Strategies
            9.12.1. When to Use it
            9.12.2. Before Writing it
            9.12.3. Choosing Good Accumulator and Iterator Variable Names
        9.13. 👩‍💻 Don’t Mutate A List That You Are Iterating Through
        9.14. Summary
        9.15. Exercises
            9.15.1. Contributed Exercises
        9.16. Chapter Assessment - List Methods
            9.16.1. Chapter Assessment - Aliases and References
            9.16.2. Chapter Assessment - Split and Join
            9.16.3. Chapter Assessment - For Loop Mechanics
            9.16.4. Chapter Assessment - Accumulator Pattern
            9.16.5. Chapter Assessment - Problem Solving
    10. Files
        10.1. Introduction: Working with Data Files
            10.1.1. Learning Goals
            10.1.2. Objectives
        10.2. Reading a File
        10.3. Alternative File Reading Methods
        10.4. Iterating over lines in a file
        10.5. Finding a File in your Filesystem
        10.6. Using with for Files
        10.7. Recipe for Reading and Processing a File
        10.8. Writing Text Files
        10.9. CSV Format
        10.10. Reading in data from a CSV File
        10.11. Writing data to a CSV File
        10.12. 👩‍💻 Tips on Handling Files
        10.13. Glossary
        10.14. Exercises
            10.14.1. Contributed Exercises
        10.15. Chapter Assessment
    11. Dictionaries
        11.1. Introduction: Dictionaries
            11.1.1. Learning Goals
            11.1.2. Objectives
        11.2. Getting Started with Dictionaries
        11.3. Dictionary operations
        11.4. Dictionary methods
            11.4.1. Iterating over Dictionaries
            11.4.2. Safely Retrieving Values
        11.5. Aliasing and copying
        11.6. Introduction: Accumulating Multiple Results In a Dictionary
        11.7. Accumulating Results From a Dictionary
        11.8. Accumulating the Best Key
        11.9. 👩‍💻 When to use a dictionary
        11.10. Glossary
        11.11. Exercises
            11.11.1. Contributed Exercises
        11.12. Chapter Assessment
            11.12.1. Assessment - Dictionaries
            11.12.2. Assessment - Dictionary Accumulation
    12. Functions
        12.1. Introduction to Functions
            12.1.1. Topics
            12.1.2. Learning Objectives
        12.2. Function Definition
        12.3. Function Invocation
        12.4. Function Parameters
        12.5. Returning a value from a function
        12.6. 👩‍💻 Decoding a Function
        12.7. Type Annotations
        12.8. A function that accumulates
        12.9. Variables and parameters are local
        12.10. Global Variables
        12.11. Functions can call other functions (Composition)
        12.12. Flow of Execution Summary
        12.13. 👩‍💻 Print vs. return
        12.14. Passing Mutable Objects
        12.15. Side Effects
        12.16. Glossary
        12.17. Exercises
            12.17.1. Contributed Exercises
        12.18. Chapter Assessment
    13. Tuple Packing and Unpacking
        13.1. Introduction
            13.1.1. Learning Objectives
        13.2. Tuple Packing
        13.3. Tuple Assignment with Unpacking
            13.3.1. Swapping Values between Variables
            13.3.2. Unpacking Into Iterator Variables
            13.3.3. The Pythonic Way to Enumerate Items in a Sequence
        13.4. Tuples as Return Values
        13.5. Unpacking Tuples as Arguments to Function Calls
        13.6. Glossary
        13.7. Exercises
            13.7.1. Contributed Exercises
        13.8. Chapter Assessment
    14. More About Iteration
        14.1. Introduction
            14.1.1. Learning Goals
            14.1.2. Objectives
        14.2. The while Statement
        14.3. The Listener Loop
            14.3.1. Other uses of while
                14.3.1.1. Sentinel Values
                14.3.1.2. Validating Input
        14.4. Randomly Walking Turtles
        14.5. Break and Continue
        14.6. 👩‍💻 Infinite Loops
        14.7. Exercises
            14.7.1. Contributed Exercises
        14.8. Chapter Assessment
    15. Advanced Functions
        15.1. Introduction: Optional Parameters
        15.2. Keyword Parameters
            15.2.1. Keyword Parameters with .format
        15.3. Anonymous functions with lambda expressions
        15.4. 👩‍💻 Programming With Style
        15.5. Method Invocations
        15.6. Exercises
            15.6.1. Contributed Exercises
        15.7. Chapter Assessment
    16. Sorting
        16.1. Introduction: Sorting with Sort and Sorted
        16.2. Optional reverse parameter
        16.3. Optional key parameter
        16.4. Sorting a Dictionary
        16.5. Breaking Ties: Second Sorting
        16.6. 👩‍💻 When to use a Lambda Expression
        16.7. Glossary
        16.8. Exercises
            16.8.1. Contributed Exercises
        16.9. Chapter Assessment
        16.10. Project - Sentiment Classifier
    17. Nested Data and Nested Iteration
        17.1. Introduction: Nested Data and Nested Iteration
            17.1.1. Lists with Complex Items
        17.2. Nested Dictionaries
        17.3. Processing JSON results
        17.4. Nested Iteration
        17.5. 👩‍💻 Structuring Nested Data
        17.6. Deep and Shallow Copies
        17.7. 👩‍💻 Extracting from Nested Data
            17.7.1. Understand
            17.7.2. Extract
            17.7.3. Repeat
                17.7.3.1. Level 2
                17.7.3.2. Level 3
                17.7.3.3. Level 4
                17.7.3.4. Reflections
        17.8. Exercises
            17.8.1. Contributed Exercises
        17.9. Chapter Assessment
    18. Test Cases
        18.1. Introduction: Test Cases
        18.2. Checking Assumptions About Data Types
        18.3. Checking Other Assumptions
        18.4. Testing Conditionals
        18.5. Testing Loops
        18.6. Writing Test Cases for Functions
            18.6.1. Return Value Tests
            18.6.2. Side Effect Tests
        18.7. Testing Optional Parameters
        18.8. 👩‍💻 Program Development
        18.9. Glossary
        18.10. Chapter Assessment
        18.11. Exercises
            18.11.1. Contributed Exercises
    19. Exceptions
        19.1. What is an exception?
        19.2. Exception Handling Flow-of-control
            19.2.1. Raising and Catching Errors
        19.3. 👩‍💻 When to use try/except
        19.4. Standard Exceptions
        19.5. Exercises
            19.5.1. Contributed Exercises
        19.6. Chapter Assessment
    20. Defining your own Classes
        20.1. Introduction: Classes and Objects - the Basics
            20.1.1. Object-oriented programming
        20.2. Objects Revisited
        20.3. User Defined Classes
        20.4. Adding Parameters to the Constructor
        20.5. Adding Other Methods to a Class
        20.6. Objects as Arguments and Parameters
        20.7. Converting an Object to a String
        20.8. Instances as Return Values
        20.9. Sorting Lists of Instances
        20.10. Class Variables and Instance Variables
        20.11. Thinking About Classes and Instances
        20.12. Testing classes
        20.13. A Tamagotchi Game
        20.14. Glossary
        20.15. Exercises
            20.15.1. Contributed Exercises
        20.16. Chapter Assessment
    21. Building Programs
        21.1. Building A Program: A Strategy
            21.1.1. Sketch an Outline
            21.1.2. Code One Section at a Time
            21.1.3. Clean Up
        21.2. 👩‍💻 Sketch an Outline
        21.3. 👩‍💻 Code one section at a time
        21.4. 👩‍💻 Clean Up
        21.5. Exercises
            21.5.1. Contributed Exercises
    22. Inheritance
        22.1. Introduction: Class Inheritance
        22.2. Inheriting Variables and Methods
            22.2.1. Mechanics of Defining a Subclass
            22.2.2. How the interpreter looks up attributes
        22.3. Overriding Methods
        22.4. Invoking the Parent Class’s Method
        22.5. Tamagotchi Revisited
        22.6. Exercises
            22.6.1. Contributed Exercises
        22.7. Chapter Assessment
        22.8. Project - Wheel of Python
    23. More on Accumulation: Map, Filter, List Comprehension, and Zip
        23.1. Introduction: Map, Filter, List Comprehensions, and Zip
        23.2. Map
        23.3. Filter
        23.4. List Comprehensions
        23.5. Zip
        23.6. Exercises
            23.6.1. Contributed Exercises
        23.7. Chapter Assessment
    24. Internet APIs
        24.1. Requesting data from the Internet
        24.2. The Internet: Behind the Scenes
        24.3. Anatomy of URLs
        24.4. The HTTP protocol
        24.5. Using REST APIs
            24.5.1. URL Structure for REST APIs
            24.5.2. Encoding URL Parameters
        24.6. Fetching a page
            24.6.1. Fetching in python with requests.get
            24.6.2. More Details of Response objects
            24.6.3. Using requests.get to encode URL parameters
        24.7. Caching Response Content
            24.7.1. The requests_with_caching module
            24.7.2. Implementation of the requests_with_caching module
        24.8. Figuring Out How to Use a REST API
            24.8.1. Example: the datamuse API
            24.8.2. Defining a function to make repeated invocations
        24.9. Debugging calls to requests.get()
            24.9.1. In the Runestone environment
            24.9.2. In a full python environment
        24.10. Requests Cookbook
        24.11. Searching for Media on iTunes
        24.12. Searching for tags on flickr
        24.13. Unicode for non-English characters
        24.14. Project - OMDB and TasteDive


    Apandices
        A.1 Numpy
        A.2 Pandas
        A.3 Regex


"""
