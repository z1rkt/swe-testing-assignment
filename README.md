# Quick-Calc

Quick-Calc is a simple calculator application that performs basic arithmetic operations including addition, subtraction, multiplication, division, and clearing results.

The project demonstrates software testing principles including unit testing and integration testing while using GitHub for version control.

## Setup Instructions

1. Clone the repository

git clone https://github.com/yourusername/swe-testing-assignment

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python interface.py

## Running Tests

pytest

## Testing Framework Research

Two popular Python testing frameworks are **Unittest** and **PyTest**.

Unittest is Python's built-in testing framework inspired by Java's JUnit. It provides structured test cases, setup and teardown functions, and strong integration with Python's standard library. However, its syntax can be verbose and requires more boilerplate code.

PyTest is a more modern and flexible testing framework. It allows writing tests with simple functions and minimal code. PyTest also supports powerful features such as fixtures, parameterization, and detailed failure reports.

For this project, PyTest was chosen because it is easier to write and read tests, making development faster and the test suite more maintainable.
