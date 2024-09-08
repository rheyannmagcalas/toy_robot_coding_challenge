import logging 
from toy_robot import ToyRobot

def parse_command(robot, command):
    """
    Parses and executes the robot command.

    Parameters:
    :robot (object): Robot object
    :command (str): (e.g., 'PLACE 0,0,NORTH', 'MOVE', 'LEFT', 'RIGHT', 'REPORT')

    Returns:
        Bool: True / False / 'Exit'
    """
    if command.startswith('PLACE'):
        robot.place(command)
    elif command == 'MOVE':
        robot.move()
    elif command == 'LEFT':
        robot.left()
    elif command == 'RIGHT':
        robot.right()
    elif command == 'REPORT':
        robot.report()
    else:
        logging.error(f"Invalid command: {command}")
        return False

def _print_commands():
    """
    Prints the list of available commands and their descriptions.
    """
    print("\n********** AVAILABLE COMMANDS **********\n")
    print("1. PLACE X,Y,F")
    print("   - Description: Places the robot on the table at coordinates (X, Y) facing the specified direction (F).")
    print("   - Parameters:")
    print("     - X (integer): The X-coordinate of the robot's position (0 to 4).")
    print("     - Y (integer): The Y-coordinate of the robot's position (0 to 4).")
    print("     - F (string): The direction the robot is facing. Must be one of NORTH, SOUTH, EAST, or WEST.")
    print("   - Example: PLACE 1,2,EAST")
    print()
    print("2. MOVE")
    print("   - Description: Moves the robot one unit forward in the direction it is currently facing. The robot cannot move off the edge of the table.")
    print()
    print("3. LEFT")
    print("   - Description: Rotates the robot 90 degrees to the left (counterclockwise) without changing its position.")
    print()
    print("4. RIGHT")
    print("   - Description: Rotates the robot 90 degrees to the right (clockwise) without changing its position.")
    print()
    print("5. REPORT")
    print("   - Description: Outputs the current position and direction of the robot. The output includes the X-coordinate, Y-coordinate, and the direction symbol.")
    print()

def main():
    """
    Main function that runs the robot console application.
    """
    print("*****************************************")
    print("*****************************************")
    print("\n \033[1m Welcome to Toy Robot Simulator! \033[0m \n")
    print("*****************************************")
    print("*****************************************")
    print('\nOverview:')
    print('This application simulates a toy robot moving on a square tabletop of dimensions 5 units x 5 units.')
    print('The robot can be controlled using a set of commands to place it on the table, move it, rotate it, and \nreport its current status. The robot must remain on the table and cannot fall off.')

    _print_commands()
    robot = ToyRobot()
    print("Enter command (e.g., PLACE X,Y,F, MOVE, LEFT, RIGHT, REPORT), or 'EXIT' to quit:")

    while True:
        command = input("> ").upper()
        if command == 'EXIT':
            break
        parse_command(robot, command)

if __name__ == "__main__":
    main()
