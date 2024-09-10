# Airbnb Clone

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
- [Command Interpreter](#command-interpreter)
  - [How to Use](#how-to-use)
  - [Examples](#examples)
- [Project Structure](#Project-Structure)
- [Features](#Features)
- [Testing](#Testing)
- [Implementation Journey](#implementation-journey)
- [Authors](#authors)
- [Contributing](#contributing)
- [Show Your Support](#show-your-support)



## Description

This project is a command interpreter for managing AirBnB objects. The command interpreter enables the creation, update, and manipulation of different objects (such as Users, Places, Cities, etc.) and stores them in a file (JSON format). This is part of a broader project aimed at creating a full-stack AirBnB clone application.

## Getting Started

To get started with the Airbnb Clone, follow these steps:

1. Clone this repository::

   ```bash
   git clone https://github.com/mugishasam123/alu-AirBnB_clone.git
   ```

2. Ensure you have [Python 3](https://www.python.org/downloads/) installed.
3. Navigate inside the cloned project folder

    ```bash
    cd alu-AirBnB_clone
    ```

4. Run the command interpreter using:

   ```bash
   ./console.py
   ```

   You're ready to interact with the application!

### Command Interpreter

The command interpreter manages objects like Users, Cities, Places, and more. It allows for the creation, modification, and deletion of these objects.

### How to Use

Once the interpreter is running, you can interact with it by typing commands at the prompt (hbnb)

Supported commands:

- `create <Class>`: Creates a new object and saves it to the file.
- `show <Class> <id>`:  Retrieves an object by its ID.
- `destroy <Class> <id>`:  Deletes an object by its ID.
- `all [<Class>]`:  Displays all objects, or all objects of a specific class.
- `update <Class> <id> <attribute_name> <attribute_value>`:  Updates an object's attribute.


### Examples

1. Create a new User:

```bash
(hbnb) create User
```
2. Show a User:

```bash
(hbnb) show User 1234-5678-9101
```
3. Exit the interpreter:

```bash
(hbnb) quit
```

### Project Structure

- **models/:**: Contains classes for each type of object (e.g., User, State, City, etc.) and the BaseModel class.
- **Sconsole.py:**: The entry point for the command interpreter.
- **tests/:**: Contains unit tests for each model and the storage engine.


## Features

1. **File Storage:**: Store and retrieve objects as JSON in files.

2. **UUID Generation:**:  Each object has a unique ID.

3. **Command Interpreter:**: Manage objects through a command-line interface.

4. **Serialization & Deserialization:**: Convert objects to JSON format and back to instances.

## Implementation Journey

- **BaseModel:**: A parent class that handles object creation, updates, serialization to JSON, and deserialization.
- **File Storage:**: A simple storage system that stores objects in JSON files and reloads them when needed.
- **Command Interpreter:**:  A shell-like interface that allows users to manage objects and their data.

### Testing

Unit tests are created using the `unittest` module to ensure that all components of the project work correctly.

To run all tests: `python3 -m unittest discover tests`
   

## Authors

1. **Author 1**
    - Github: [mugisha samuel](https://github.com/mugishasam123)

2. **Author 2**
    - Githib: [tuyishimejeandamour](https://github.com/tuyishimejeandamour)

## Contributing
Contributions, issues, and feature requests are welcome!

Feel free to check the issues page.

## Show your support
Give a ⭐️ if you like this project!