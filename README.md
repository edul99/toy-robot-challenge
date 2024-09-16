# Toy Robot Code Challenge

This is a simple python application that simulates a toy robot moving on a 5x5 square tabletop. The robot follows a series of commands to move around the table while avoiding falling off the edges.

## Features

- **PLACE X,Y,F**: Places the robot on the table at position (X, Y) facing direction F (NORTH, SOUTH, EAST, or WEST).
- **MOVE**: Moves the robot one unit forward in the direction it is currently facing.
- **LEFT**: Rotates the robot 90 degrees left without changing its position.
- **RIGHT**: Rotates the robot 90 degrees right without changing its position.
- **REPORT**: Outputs the robot's current X, Y coordinates and direction.

## Prerequisites

- **Python 3.x** installed on your machine.

## How to Set Up

1. **Clone the Repository** (if using a version control system):
   ```bash
   git clone https://github.com/edul99/toy-robot-challenge.git
   ```

2. **Alternatively**, you can download the Python script directly and place it in a folder on your machine.

## Running the Application

1. Open a terminal or command prompt.
2. Navigate to the folder where the `toy_robot.py` file is located.
3. Run the application using Python:
   ```bash
   python toy_robot.py
   ```

4. **Example of usage**:
   ```
   Enter command (type EXIT to stop): PLACE 1,2,NORTH
   Enter command (type EXIT to stop): MOVE
   Enter command (type EXIT to stop): LEFT
   Enter command (type EXIT to stop): REPORT
   Output: 1,3,WEST
   Enter command (type EXIT to stop): EXIT
   ```

### Available Commands

- **PLACE X,Y,F**: This command places the robot on the 5x5 tabletop grid, where:
  - `X` is the X-coordinate (0-4)
  - `Y` is the Y-coordinate (0-4)
  - `F` is the direction the robot faces: `NORTH`, `SOUTH`, `EAST`, or `WEST`
- **MOVE**: Moves the robot one step in the direction it is currently facing.
- **LEFT**: Rotates the robot 90 degrees to the left (counter-clockwise).
- **RIGHT**: Rotates the robot 90 degrees to the right (clockwise).
- **REPORT**: Prints the robot's current position and facing direction (e.g., `0,1,NORTH`).
- **EXIT**: Ends the application.

### Invalid Commands

- The robot will ignore any `MOVE` commands that would result in it falling off the table.
- Any command issued before a valid `PLACE` command is ignored.

## Running Unit Tests

Unit tests are included to verify the functionality of the robot simulator.

### Steps to Run the Tests

1. In the terminal, navigate to the directory where your project is located.
2. Run the `test_toy_robot.py` file:
   ```bash
   python test_toy_robot.py
   ```

3. You should see the output indicating whether all tests passed. If a test fails, the output will show which test case failed.

### Example Output for Tests

```
All tests passed!
```
