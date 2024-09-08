# Toy Robot Coding Challenge

## Overview 
The Toy Robot Simulator is a Python application that simulates a toy robot moving on a square tabletop. The robot can be controlled using a set of commands to place it on the table, move it, rotate it, and report its current status. The board dimensions are 5 units by 5 units.

## Features
* PLACE X,Y,F: Place the robot on the board at coordinates (X, Y) facing the specified direction (F).
* MOVE: Move the robot one unit forward in the direction it is currently facing.
* LEFT: Rotate the robot 90 degrees to the left (counterclockwise).
* RIGHT: Rotate the robot 90 degrees to the right (clockwise).
* REPORT: Output the current position and direction of the robot. This command will print the 5x5 grid and display the robot's current location along with the corresponding direction symbol on the grid.

## Installation
To get started with the Toy Robot Simulator, follow these steps:
1. Clone this repo
2. Navigate to the project directory
```bash
cd toy_robot_coding_challenge
```
3. Install Dependencies: This project uses Python's built-in modules, so no additional packages are required.

## Usage
Run the main function to start the robot console application:
```bash
python app/main.py 
``` 
Enter commands to control the robot. Available commands include:

* **PLACE X,Y,F** – Example: PLACE 1,2,EAST
* **MOVE**
* **LEFT**
* **RIGHT**
* **REPORT**
* Type **EXIT** to quit the application.


## Running Tests 
To ensure everything is working correctly, you can run the unit tests using unittest: 
1. Navigate to the Test Directory: 
```bash
cd tests
``` 
2. Run All Tests: 
```bash
python -m unittest discover
``` 
3. Running tests per module:
* Testing for table_validator script:
```bash
python test_table_validator.py -v
``` 
* Testing for toy_robot script: 
```bash
python test_toy_robot.py -v
``` 
* Testing for main script:
```bash
python test_main.py -v
``` 

## Code Structure 
* toy_robot.py: Contains the ToyRobot class with methods for robot control.
* validation.py: Contains the TableValidator class for validating commands and robot placement.
* main.py: The entry point for running the application.
* tests/: Contains unit tests for validating functionality.


## Future Enhancements

1. **Multiple Robots**
    * Allow multiple robots on the same board, each with its own commands.
    * Implementation: Maintain a list of robot instances and switch between them with a SWITCH <robot_id> command.
2. **Advanced Movement**:
    * Add diagonal movements or allow the robot to move multiple units at once.
    * Implementation: Modify the MOVE command to accept an argument like MOVE 3.
3. **Undo Command**:
    * Implement an undo feature to revert the robot’s last action.
    * Implementation: Maintain a stack of previous states and pop them when UNDO is called.
4. **Save and Load State**:
    * Save the current board state and robot position to a file and load it later.
    * Implementation: Serialize the board and robot objects into a file and deserialize them back.
5. **Set Board Dimensions**:
    * Allow users to set the dimensions of the board through user input.
    * Implementation: Update the initialization of the ToyRobot class to accept board dimensions and adjust the commands accordingly.