class ToyRobot:
    def __init__(self):
        self.x = None
        self.y = None
        self.f = None
        self.directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
        self.table_size = 5

    def place(self, x, y, f):
        if 0 <= x < self.table_size and 0 <= y < self.table_size and f in self.directions:
            self.x = x
            self.y = y
            self.f = f
        else:
            return "Invalid PLACE command. Robot must be placed within the 5x5 grid and facing a valid direction."

    def move(self):
        if self.x is None or self.y is None:
            return "MOVE command ignored. Robot has not been placed."
        else:
            if self.f == 'NORTH' and self.y + 1 < self.table_size:
                self.y += 1
            elif self.f == 'SOUTH' and self.y - 1 >= 0:
                self.y -= 1
            elif self.f == 'EAST' and self.x + 1 < self.table_size:
                self.x += 1
            elif self.f == 'WEST' and self.x - 1 >= 0:
                self.x -= 1
            else:
                return "MOVE command would cause the robot to fall off the table. Ignored."

    def left(self):
        if self.f is not None:
            self.f = self.directions[(self.directions.index(self.f) - 1) % 4]
        else:
            return "LEFT command ignored. Robot has not been placed."

    def right(self):
        if self.f is not None:
            self.f = self.directions[(self.directions.index(self.f) + 1) % 4]
        else:
            return "RIGHT command ignored. Robot has not been placed."

    def report(self):
        if self.x is not None and self.y is not None and self.f is not None:
            return f"{self.x},{self.y},{self.f}"
        else:
            return "REPORT command ignored. Robot has not been placed."

    def process_command(self, command):
        parts = command.strip().split(maxsplit=1)
        if parts[0] == 'PLACE':
            if len(parts) == 2:
                args = [arg.strip() for arg in parts[1].split(',')]
                if len(args) == 3 and all(arg != '' for arg in args):
                    x, y, f = args
                    try:
                        x = int(x)
                        y = int(y)

                        if f.isalpha():
                            # call place function
                            return self.place(x, y, f)
                        else:
                            return "Invalid PLACE command format. Directions must be alphabetic characters. Example: PLACE 1,1,NORTH"
                    except ValueError:
                        return "Invalid PLACE command format. Coordinates must be numeric characters. Example: PLACE 1,1,NORTH"
                else:
                    return "Invalid PLACE command format. At least one input is missing. Example: PLACE 1,1,NORTH"
            else:
                return "Invalid PLACE command format. Include coordinates and direction. Example: PLACE 1,1,NORTH"
        elif parts[0] == 'MOVE':
            # call move function
            return self.move()
        elif parts[0] == 'LEFT':
            # call left function
            return self.left()
        elif parts[0] == 'RIGHT':
            # call right function
            return self.right()
        elif parts[0] == 'REPORT':
            # call report function
            return self.report()
        else:
            return f"Unknown command: {command}"

def main():
    # Initialize the toy robot
    robot = ToyRobot()

    # Accept inputs until user promted to stop
    while True:
        command = input("Enter command (type EXIT to stop): ").strip()
        command = command.upper()
        if command == "EXIT":
            break

        # Outputs especially errors can be printed immediately at the command functions but opted to return instead for testability
        output = robot.process_command(command)
        if output is not None:
            print(output)

if __name__ == '__main__':
    main()
