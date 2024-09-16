from toy_robot import ToyRobot

def test_toy_robot():
    # Initialize the toy robot
    robot = ToyRobot()

    ##### FIRST SEQUENCE
    # Test 1: PLACE command
    robot.process_command("PLACE 0,0,NORTH")
    assert robot.x == 0 and robot.y == 0 and robot.f == "NORTH", "Test 1 Failed"

    # Test 2: MOVE command
    robot.move()
    assert robot.x == 0 and robot.y == 1, "Test 2 Failed"

    # Test 3: LEFT command
    robot.left()
    assert robot.f == "WEST", "Test 3 Failed"

    # Test 4: RIGHT command
    robot.right()
    assert robot.f == "NORTH", "Test 4 Failed"

    # Test 5: REPORT command
    output = robot.process_command("REPORT")
    assert output == "0,1,NORTH", "Test 5 Failed"

    ##### SECOND SEQUENCE
    # Test 6: PLACE command
    robot.process_command("PLACE 4,4,EAST")
    assert robot.x == 4 and robot.y == 4 and robot.f == "EAST", "Test 6 Failed"

    # Test 7: REPORT command
    output = robot.process_command("REPORT")
    assert output == "4,4,EAST", "Test 7 Failed"

    ##### ERRORS
    # Test 8: MOVE out of bounds
    output = robot.process_command("MOVE")
    assert output == "MOVE command would cause the robot to fall off the table. Ignored.", "Test 8 Failed"

    # Test 9: PLACE out of bounds
    output = robot.process_command("PLACE 6,6,SOUTH")
    assert output == "Invalid PLACE command. Robot must be placed within the 5x5 grid and facing a valid direction.", "Test 9 Failed"

    # Test 10: Alpabhetic characters
    output = robot.process_command("PLACE 1,1,#")
    assert output == "Invalid PLACE command format. Directions must be alphabetic characters. Example: PLACE 1,1,NORTH", "Test 10 Failed"

    # Test 11: Numeric characters
    output = robot.process_command("PLACE a,1,NORTH")
    assert output == "Invalid PLACE command format. Coordinates must be numeric characters. Example: PLACE 1,1,NORTH", "Test 11 Failed"

    # Test 12: Incomplete position
    output = robot.process_command("PLACE 1,,NORTH")
    assert output == "Invalid PLACE command format. At least one input is missing. Example: PLACE 1,1,NORTH", "Test 12 Failed"

    # Test 13: No position at all
    output = robot.process_command("PLACE")
    assert output == "Invalid PLACE command format. Include coordinates and direction. Example: PLACE 1,1,NORTH", "Test 13 Failed"

    # Test 14: Unknown command
    output = robot.process_command("GET")
    assert output == "Unknown command: GET", "Test 14 Failed"

    ##### WHITESPACES and LOWERCASE
    # Test 15: Whitespaces in PLACE command
    robot.process_command("PLACE 3, 2,   SOUTH")
    assert robot.x == 3 and robot.y == 2 and robot.f == "SOUTH", "Test 15 Failed"

    # Test 16: Whitespaces in other commands
    robot.process_command("   RIGHT   ")
    assert robot.x == 3 and robot.y == 2 and robot.f == "WEST", "Test 16 Failed"

    # Test 17: Lowercase
    output = robot.process_command("report")
    assert output == "3,2,WEST", "Test 17 Failed"

    print("All tests passed!")

if __name__ == "__main__":
    # Each test cases could be programmed into separate functions as in real world examples, but opted to combine all in one for simplicity.
    test_toy_robot()
