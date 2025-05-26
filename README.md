# 🐍 Python Programming & Object-Oriented Concepts

This repository is a collection of Python programming exercises, concepts, and Object-Oriented Programming (OOP) implementations. It serves as a learning archive for fundamental and intermediate-level Python development using OOP principles.

---

## 📚 Contents

### 🧑‍💻 Python Basics
- Input/Output operations
- Variables and Data Types
- Conditional Statements (`if`, `else`, `elif`)
- Looping (`for`, `while`)
- Functions and Lambda Expressions
- List, Tuple, Set, Dictionary

### 🔁 File Handling
- Reading and writing to `.txt` files
- Working with file objects
- File modes and exception handling

### 🧱 Object-Oriented Programming (OOP)
- Classes and Objects  
- Constructors (`__init__`)  
- Instance and Class Variables  
- Inheritance and Method Overriding  
- Encapsulation and Abstraction  
- Polymorphism  
- Dunder Methods (`__str__`, `__len__`, etc.)

### 🛠️ Mini Projects
- Bank Management System  
- Student Management System  
- Simple Calculator  
- File Encryption/Decryption using OOP

---

## 🛠️ Technologies Used

- **Language:** Python 3.x  
- **IDE:** VS Code / PyCharm / Jupyter Notebook  
- **Concepts:** OOP, File Handling, Functions, Loops, Error Handling

---

## 📸 Sample Code Snapshot

```python
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")
