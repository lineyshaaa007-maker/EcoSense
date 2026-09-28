# EcoSense – Smart Waste Classification & Recycling Assistant

EcoSense is a Python-based waste classification and recycling assistant developed as a first-year B.Tech CSE project.

The application allows users to enter information about a waste item, classify the waste, receive a recycling or disposal recommendation, save the record, search previous records, and view basic statistics.

---

## 1. About the Project

EcoSense is a Python-based project designed to help users classify common waste items and understand how they can be handled.

The user enters basic information about a waste item, such as:

- Item name
- Material
- Condition
- Quantity

Based on this information, EcoSense identifies the type of waste and provides a suitable recycling or disposal suggestion.

The entered record is also stored in a CSV file. This allows users to:

- View previous waste records
- Search for a particular item or material
- View basic statistics
- Maintain a history of waste entries

The project was developed as a first-year B.Tech CSE project to apply Python programming concepts to a practical real-world problem.

---

## 2. Problem Statement

Waste is often not sorted correctly because people may not always know which category a particular item belongs to or how it should be handled.

Different types of waste require different methods of handling.

For example:

- Plastic may be recyclable.
- Paper can generally be recycled when it is clean and dry.
- Glass requires appropriate collection and recycling.
- Organic waste can be handled through composting or suitable organic-waste systems.
- Electronic waste should be sent to an appropriate e-waste collection facility.

Keeping track of waste records manually can also become difficult.

EcoSense provides a simple way to enter waste information, classify it, receive a basic recommendation, and store the information for later use.

---

## 3. Objectives

The main objectives of EcoSense are:

- To classify common types of waste.
- To provide basic recycling or disposal suggestions.
- To validate important user inputs.
- To save waste records for future reference.
- To allow users to view previously saved records.
- To provide a search facility.
- To calculate basic statistics from stored waste data.
- To demonstrate the use of Python programming concepts in a practical project.
- To organize the project using multiple Python modules.
- To include basic automated testing.

---

## 4. Features

EcoSense currently provides the following features:

- Waste classification based on material.
- Input validation.
- Recycling and disposal recommendations.
- CSV-based data storage.
- Waste history.
- Search by item name or material.
- Basic waste statistics.
- Error handling for invalid input.
- Object-Oriented Programming using a `WasteItem` class.
- NumPy-based statistical calculations.
- Basic automated testing.
- Modular Python project structure.

---

## 5. Supported Waste Categories

EcoSense currently works with six main types of waste:

| Material | Waste Category |
|---|---|
| Plastic | Plastic Waste |
| Paper | Paper Waste |
| Glass | Glass Waste |
| Metal | Metal Waste |
| Organic | Organic Waste |
| E-Waste | Electronic Waste |

The classification module maps the material entered by the user to the corresponding waste category.

---

## 6. Main Modules

The project is divided into multiple Python files instead of placing the complete program into one large file.

This makes the project easier to understand, maintain, test, and modify.

### 6.1 Classification

The classification module checks the material entered by the user and assigns the appropriate waste category.

For example:

```text
Input:
plastic

Output:
Plastic Waste
```

### 6.2 Input Validation

The validation module checks information entered by the user.

It validates inputs such as:

- Item name
- Material
- Condition
- Quantity

It helps prevent invalid information from entering the system.

### 6.3 Recommendations

The recommendation module provides recycling or disposal suggestions based on the waste material and condition.

For example, clean and dry paper may receive a recycling recommendation, while electronic waste may receive a recommendation to use an appropriate e-waste collection facility.

### 6.4 Waste History

The history module manages waste records stored in the CSV file.

It allows the program to:

- Save records.
- Read records.
- Display waste history.
- Search stored records.

### 6.5 Search

The search functionality allows users to find stored waste records.

Users can search using information such as:

- Item name
- Material

### 6.6 Statistics

The statistics module reads the stored records and calculates basic values such as:

- Total number of records
- Total quantity
- Average quantity
- Minimum quantity
- Maximum quantity
- Number of different waste categories

NumPy is used for some of the statistical calculations.

---

## 7. Non-Functional Requirements

### 7.1 Usability

The program should be simple enough for a user to understand and operate through the menu.

### 7.2 Reliability

The program should handle incorrect inputs properly instead of stopping unexpectedly.

### 7.3 Maintainability

The project is divided into separate modules so individual parts can be modified without changing the entire program.

### 7.4 Performance

The program should provide results quickly when working with a normal number of waste records.

### 7.5 Error Handling

The program should display understandable error messages when the user enters invalid information.

---

## 8. Project Structure

The project is organized into different files and folders. Each file has a specific purpose.

```text
Ecosense/
│
├── .gitignore
├── main.py
├── classifier.py
├── validation.py
├── recommendation.py
├── models.py
├── history.py
├── statistics.py
├── utilities.py
├── requirements.txt
├── README.md
├── statement.md
│
├── data/
│   └── waste_records.csv
│
├── design/
│   ├── architecture_diagram.graphml
│   ├── workflow_diagram.graphml
│   ├── use_case_diagram.graphml
│   ├── class_diagram.graphml
│   ├── sequence_diagram.graphml
│   ├── component_diagram.graphml
│   └── storage_diagram.graphml
│
├── screenshots/
│   ├── 01_waste_history.png
│   ├── 01_waste_history_2.png
│   ├── 02_search.png
│   ├── 03_statistics.png
│   ├── 04_recommendations.png
│   ├── 05_error_handling.png
│   ├── 05_error_handling_quantity.png
│   ├── 05_error_handling_condition.png
│   ├── 05_error_handling_material.png
│   ├── 06_csv_storage.png
│   ├── 07_tests_passed.png
│   ├── architecture_diagram.png
│   ├── workflow_diagram.png
│   ├── use_case_diagram.png
│   ├── class_diagram.png
│   ├── sequence_diagram.png
│   ├── component_diagram.png
│   └── storage_diagram.png
│
└── tests/
    ├── __init__.py
    └── test_project.py
```

---

## 9. Python Files and Their Responsibilities

This section explains what each Python file does.

### 9.1 main.py

This is the main entry point of the application.

It:

- Displays the main menu.
- Accepts the user's choice.
- Connects the different modules.
- Controls the overall program flow.

The project is started using:

```bash
python main.py
```

### 9.2 classifier.py

This file contains the functions used to classify waste.

It checks the material entered by the user and maps it to the appropriate waste category.

### 9.3 validation.py

This file is responsible for validating user input.

It checks values such as:

- Item name
- Material
- Quantity
- Condition

### 9.4 recommendation.py

This file contains recycling and disposal recommendations for the supported waste materials.

The recommendation can depend on the type and condition of the waste.

### 9.5 models.py

This file contains the `WasteItem` class.

The class is used to keep information about one waste item together in the form of an object.

Typical information includes:

- Item name
- Material
- Condition
- Quantity
- Category
- Status
- Recommendation

### 9.6 history.py

This file manages waste records stored in the CSV file.

It handles tasks such as:

- Saving records.
- Reading records.
- Displaying history.
- Searching records.

### 9.7 statistics.py

This file reads the stored waste records and performs basic statistical calculations.

NumPy is used for calculations such as:

- Average
- Minimum
- Maximum
- Total quantity

### 9.8 utilities.py

This file contains common utility functions used throughout the project.

Examples include:

- Displaying headings.
- Getting the waste condition.
- Determining waste status.
- Other commonly used helper functions.

---

## 10. Technologies Used

The project was developed using the following technologies and concepts:

- Python
- Visual Studio Code
- NumPy
- CSV file handling
- Object-Oriented Programming
- Python modules
- Exception handling
- File handling
- Basic automated testing

---

## 11. Python Concepts Used

While developing EcoSense, several Python concepts were used:

- Variables and data types
- Input and output
- Conditional statements
- Loops
- Functions
- Modules
- Lists
- Dictionaries
- Sets
- File handling
- Exception handling
- NumPy
- Classes and objects
- Constructors
- Methods
- Object-Oriented Programming
- Basic software testing

Using these concepts together helped demonstrate how different Python topics can be combined to create a complete working application.

---

## 12. Data Storage

EcoSense uses a CSV file to store waste records.

The file is located at:

```text
data/waste_records.csv
```

Each record contains information such as:

- Item Name
- Material
- Condition
- Quantity
- Category
- Status
- Recommendation

Example CSV Record:

```csv
item_name,material,condition,quantity,category,status,recommendation
Water bottle,plastic,clean,2,Plastic Waste,Recyclable,Recycle the plastic through an appropriate recycling system.
```

Using a CSV file makes the data easy to store and read without requiring a separate database.

---

## 13. Installation

### 13.1 Check Python Installation

Make sure Python is installed on your computer.

You can check it using:

```bash
python --version
```

or:

```bash
python3 --version
```

### 13.2 Open the Project

Open the Ecosense folder in Visual Studio Code.

### 13.3 Install Required Packages

Open the VS Code terminal inside the project folder.

Run:

```bash
python -m pip install -r requirements.txt
```

This installs the packages required by the project.

---

## 14. How to Run the Project

Open the VS Code terminal inside the main Ecosense folder.

Run:

```bash
python main.py
```

The main menu will appear similar to:

```text
=======================================================
       ECOSENSE - SMART WASTE CLASSIFICATION SYSTEM
=======================================================

1. Classify Waste
2. View Waste History
3. Search Waste Records
4. View Waste Statistics
5. View Recycling Recommendations
6. Exit
```

The user can enter the number of the option they want to use.

---

## 15. How EcoSense Works

### 15.1 Classify Waste

The user selects:

```text
1. Classify Waste
```

The program asks for:

- Waste item name
- Material
- Condition
- Quantity

The entered information is validated first.

If the information is valid:

- The material is classified.
- The waste status is determined.
- A recommendation is generated.
- The complete record is saved in the CSV file.

### 15.2 View Waste History

The user selects:

```text
2. View Waste History
```

EcoSense reads the saved records from the CSV file and displays them.

### 15.3 Search Waste Records

The user selects:

```text
3. Search Waste Records
```

The user can enter an item name or material.

EcoSense searches the saved records and displays matching entries.

### 15.4 View Waste Statistics

The user selects:

```text
4. View Waste Statistics
```

The program reads the stored quantities and displays basic statistics such as:

- Total quantity
- Average quantity
- Minimum quantity
- Maximum quantity
- Number of categories

### 15.5 View Recycling Recommendations

The user selects:

```text
5. View Recycling Recommendations
```

EcoSense displays the available recommendations for supported materials.

### 15.6 Exit

The user selects:

```text
6. Exit
```

The program ends and displays a thank-you message.

---

## 16. Input Validation and Error Handling

Input validation is included to make the program more reliable and user-friendly.

### 16.1 Invalid Material

If the user enters a material that is not supported, EcoSense displays an error message and shows the materials that can be selected.

Supported materials include:

- plastic
- paper
- glass
- metal
- organic
- e-waste

### 16.2 Invalid Quantity

The quantity must be a positive whole number.

If the user enters:

- Text
- Zero
- A negative number
- An invalid value

the program displays an appropriate error message and asks for a valid quantity.

### 16.3 Invalid Condition

The program currently accepts three conditions:

- clean
- dirty
- damaged

If the user enters another value, an error message is displayed.

### 16.4 Empty Item Name

The item name cannot be left empty.

If the user does not enter an item name, the program displays an error message.

---

## 17. Testing

Basic automated testing has been included to check important parts of the project.

The test file is:

```text
tests/test_project.py
```

To run the tests, open the terminal in the main Ecosense folder and run:

```bash
python -m tests.test_project
```

If all tests work correctly, the output is:

```text
All tests passed successfully!
```

Current Tests

The current tests check:

- Waste classification
- Material validation
- Quantity validation
- Recycling recommendations

---

## 18. Basic Project Workflow

The overall workflow of EcoSense can be represented as:

```text
User
  ↓
Main Menu
  ↓
Enter Waste Information
  ↓
Validate Input
  ↓
Classify Waste
  ↓
Determine Status
  ↓
Give Recommendation
  ↓
Save Record
  ↓
View / Search / Calculate Statistics
```

The different tasks are handled by separate modules.

This keeps the program organized and easier to understand.

---

## 19. System Design and Diagrams

The project includes several diagrams to explain its structure and working.

### 19.1 Architecture Diagram

The architecture diagram gives an overall view of the main components of EcoSense and how they communicate with each other.

![Architecture Diagram](screenshots/architecture_diagram.png)

### 19.2 Workflow Diagram

The workflow diagram shows the main steps followed by the program while processing a waste item.

![Workflow Diagram](screenshots/workflow_diagram.png)

### 19.3 Use Case Diagram

The use case diagram shows the main actions that a user can perform in EcoSense.

![Use Case Diagram](screenshots/use_case_diagram.png)

### 19.4 Class Diagram

The class diagram shows the WasteItem class, its attributes, and its methods.

![Class Diagram](screenshots/class_diagram.png)

### 19.5 Sequence Diagram

The sequence diagram shows the order in which the user and different parts of the program interact while a waste item is being classified.

![Sequence Diagram](screenshots/sequence_diagram.png)

### 19.6 Component Diagram

The component diagram shows the main software components of EcoSense and their connections.

![Component Diagram](screenshots/component_diagram.png)

### 19.7 Data Storage Diagram

The data storage diagram shows how waste records are stored in the CSV file and used by the program.

![Data Storage Diagram](screenshots/storage_diagram.png)

---

## 20. Screenshots

The following screenshots demonstrate the main features of EcoSense and some of the testing performed during development.

Note: The screenshots are stored inside the `screenshots` folder of this repository.

### 20.1 Waste History

The waste history screen displays previously stored waste records.

![Waste History](screenshots/01_waste_history.png)

Additional Waste History View

![Additional Waste History View](screenshots/01_waste_history_2.png)

### 20.2 Search

The search feature allows the user to find stored waste records.

![Search](screenshots/02_search.png)

### 20.3 Waste Statistics

The statistics feature displays basic information calculated from stored waste records.

![Waste Statistics](screenshots/03_statistics.png)

### 20.4 Recycling Recommendations

The recommendation feature displays recycling or disposal suggestions for supported waste materials.

![Recycling Recommendations](screenshots/04_recommendations.png)

### 20.5 Error Handling

EcoSense checks invalid inputs and displays appropriate error messages.

General Error Handling

![General Error Handling](screenshots/05_error_handling.png)

Quantity Validation

![Quantity Validation](screenshots/05_error_handling_quantity.png)

Condition Validation

![Condition Validation](screenshots/05_error_handling_condition.png)

Material Validation

![Material Validation](screenshots/05_error_handling_material.png)

### 20.6 CSV Storage

The CSV file stores the waste records entered by the user.

![CSV Storage](screenshots/06_csv_storage.png)

### 20.7 Automated Testing

The test output demonstrates that the implemented tests completed successfully.

![Automated Testing](screenshots/07_tests_passed.png)

---

## 21. Future Improvements

The current version of EcoSense is a rule-based system.

There are several ways in which the project could be improved in the future.

Possible improvements include:

- Adding image-based waste recognition.
- Using a camera to identify waste items.
- Using machine learning for automatic classification.
- Creating a graphical user interface.
- Developing a mobile application.
- Adding multilingual support.
- Showing nearby recycling centres.
- Adding charts and more detailed waste analysis.
- Connecting the application to a database.
- Adding user accounts.
- Adding cloud-based storage.

These are future ideas and are not part of the current version of the project.

---

## 22. What I Learned From This Project

Working on EcoSense helped me understand how different Python concepts can be used together in one project.

Through this project, I learned:

- How to divide a program into different modules.
- How functions can be used to handle specific tasks.
- How lists, dictionaries, and sets can be used to organize information.
- How to read and write data using CSV files.
- How to validate user input.
- How to handle errors using exceptions.
- How classes and objects can be used in Python.
- How NumPy can be used for calculations.
- How basic testing can be added to a project.
- How to organize a complete project using files and folders.
- How different modules can communicate with each other.
- How to build a complete Python application from smaller components.

I also gained a better understanding of how a simple idea can be divided into smaller tasks and then connected together to create a working application.

---

## 23. Conclusion

EcoSense is a simple Python project that combines waste classification, recycling recommendations, data storage, searching, and basic statistics in one application.

The project helped me apply different concepts from the Python course, including:

- Functions
- Modules
- Data structures
- File handling
- Exception handling
- NumPy
- Object-Oriented Programming
- Testing

The current version focuses on common waste materials and provides basic recommendations based on the information entered by the user.

It also stores the records so they can be viewed and searched later.

Although the current system is simple, it provides a foundation for adding more advanced features such as image recognition, machine learning, graphical interfaces, databases, and mobile applications in the future.

---

## 24. Project Author

EcoSense – Smart Waste Classification & Recycling Assistant

Developed as a first-year B.Tech CSE project using Python.

---

## 25. Repository Overview

The repository contains:

```text
Python Source Code
        │
        ├── Classification
        ├── Validation
        ├── Recommendations
        ├── History Management
        ├── Statistics
        └── Utilities
                │
                ↓
        CSV Data Storage
                │
                ↓
        Testing
                │
                ↓
        Screenshots & Diagrams
```
