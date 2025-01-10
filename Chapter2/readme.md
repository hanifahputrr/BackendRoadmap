**Python Programming Specificities.**
--
 This chapter introduces Python's unique features, especially those critical for efficient programming and relevant to FastAPI development. 

**Basics of Python Programming**:
--


**Lists**

1. Mutable (can be modified).
2. Defined using square brackets [].
3. Elements are separated by commas.
4. Can store various data types (strings, integers, floats, etc.).
5. Elements can be added, removed, or modified.
    '''
    Example: [1, 2, 3], ["a", "b", "c"].
    '''

**Tuples**

1. Immutable (cannot be modified).
2. Defined using parentheses ().
3. Elements are separated by commas.
4. Can store various data types.
5. Elements cannot be added, removed, or modified.
'''
Example: (1, 2, 3), ("a", "b", "c").
'''

**Dictionaries**

1. Mutable (can be modified).
2. Defined using curly brackets {}.
3. Consist of key-value pairs.
4. Keys must be unique and immutable.
5. Values can be various data types.
6. Elements can be added, removed, or modified.
'''
Example: {"name": "John", "age": 30}.
'''

**Usage**

1. Lists: for frequently changing data collections.
2. Tuples: for static data collections.
3. Dictionaries: for data with unique keys.
--


**Boolean Operation**

use 'is None' for checking the null availability, unless you're certain the class doesn't override the '==' operator

**For Loop**

for loop is a method for repeatedly executing a block of code for each element in an iterable (such as lists, tuples, dictionaries, sets, or strings).

example
'''
for i in [1, 2, 3]:
    print(i)
'''

**When to Use a For Loop? A for loop is utilized when:**

1. Iterating over elements in collections (lists, tuples, dictionaries, etc.).
2. Applying specific operations to each element of an iterable.
3. Performing tasks such as:
    - Calculating totals
    - Filtering data
    - Printing iterable contents

**Common Use Cases**

1. Processing data arrays
2. Iterating over files or directories
3. Handling database query results
4. Manipulating strings or characters
5. Looping through function arguments

**Notes**
*range output is not a list*
*A common misconception is to think range returns a list. It’s actually a Sequence object that only stores the start, end, and step arguments. That’s why you could write range(1000000000) without blowing up your system’s memory: the billions of elements are not assigned to memory all at once.*
--

**While Loop**
A while loop in programming is used to repeatedly execute a block of code as long as a given condition is true. It's a fundamental control flow structure used to perform repetitive tasks where the number of iterations isn't known beforehand and depends on a condition.

**Structure and Usage of Packages in Python**
1. A package in Python is a way to organize modules into a hierarchical structure, allowing for better code management and namespace organization. 
2. A module is a single Python file containing code, while a package is a collection of modules organized in directories.
3. Packages help structure complex projects by grouping related modules.

**Example Structure:**
'''
project/
└── package/
    └── subpackage/
        └── module.py
'''

Importing a Module:
'''
import package.subpackage.module
'''

1. The __init__.py file makes a directory recognizable as a package.
2. In older Python versions, it was required. In newer versions, it’s optional but recommended.
3. Helps differentiate a package from a namespace package.
4. Can include initialization logic that executes when the package or submodules are imported.
--

**List Comprehension**
list comprehension is used to:

1. Create a new list by:
    -Transforming elements (e.g., calculating squares, changing data formats).
    -Filtering elements based on specific conditions (e.g., keeping only even numbers).
2. Simplify and shorten code compared to traditional for loops, making it more concise, elegant, and readable.
--

**Object-Oriented Programming**
--
OOP (Object-Oriented Programming) adalah paradigma pemrograman yang berfokus pada konsep objek. Dalam OOP, program dibangun menggunakan objek yang mewakili entitas dalam sistem yang sedang dibangun. Setiap objek dapat memiliki atribut (data) dan metode (fungsi) yang dapat mengoperasikan data tersebut

**Benefits of OOP**
1. developing complex software
2. efficiency
3. easily upgraded
4. easy work segregation
5. effective communication
6. maintenance
7. reusability
8. security and privacy

**Class, Object, Attribute, Method**
1. A class is a blueprint for creating objects. A class defines the attributes and methods that will be possessed by the objects created from that class.

2. An object is an instance of a class. It is a concrete representation of the class that contains the attributes and methods defined by the class.

3. Methods are used to perform specific operations or actions on an object, or to access and manipulate the data associated with that object.

4. Each object in a class can have the same or different methods, which are used to manipulate attributes or implement specific functionalities.

**Notes**
Class and method naming, By convention, classes should be named using camel case: MyWonderfulClass but not
my_wonderful_class. Methods should use snake case, like regular functions.

**Principles of OOP**
1. Encapsulation ensures restricted access to internal states.
2. Inheritance allows reuse of existing code.
3. Polymorphism enables different implementations for a shared interface.
4. Abstraction simplifies the use of complex systems by hiding unnecessary details.