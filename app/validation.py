class TableValidator:
    
    def __init__(self, board_width=5, board_height=5):
        """
        Initialize the TableValidator with the board dimensions and valid facing directions.

        Parameters:
        - board_width (int): The width of the board. Default is 5.
        - board_height (int): The height of the board. Default is 5.
        """
        self.board_width = board_width
        self.board_height = board_height
        self.valid_directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

    def _is_integer(self, value):
        """
        Check if the provided value can be converted to an integer.

        Parameters:
        - value (any): The value to check.

        Returns:
        - bool: True if value can be converted to an integer, False otherwise.
        """
        try:
            int(value)
            return True
        except ValueError:
            return False

    def _is_within_bounds(self, x, y):
        """
        Check if the given coordinates (x, y) are within the bounds of the table.

        Parameters:
        - x (int): The x-coordinate.
        - y (int): The y-coordinate.

        Returns:
        - bool: True if (x, y) is within bounds, False otherwise.
        """
        return 0 <= int(x) < self.board_width and 0 <= int(y) < self.board_height

    def _parse_command(self, command):
        """
        Parses the PLACE command into parameters.

        Parameters:
        - command (str): PLACE command.

        Returns:
        - list: Parsed parameters [x, y, facing] or None if invalid.
        """
        try:
            command = command.replace('PLACE', '').strip()
            parts = [part.strip() for part in command.split(',')] 
            return parts
        except Exception:
            return None

    def validate_place(self, command):
        """
        Validates the PLACE command parameters.

        Parameters:
        - command (str): PLACE command in the form 'PLACE X,Y,F'.

        Returns:
        - result (dict): Contains the validation status, error message (if any), and robot's position if valid.
            - is_valid (bool): True if all parameters are valid, False otherwise.
            - x (int): X-coordinate of the robot (if valid).
            - y (int): Y-coordinate of the robot (if valid).
            - facing (str): Robot's facing direction (if valid).
            - message (str): Describes the result of the validation.
        """
        params = self._parse_command(command)
        if not params:
            return {'is_valid': False, 'message': 'Invalid command format. Expected "PLACE X,Y,F".'}

        if len(params) != 3:
            return {'is_valid': False, 'message': 'Invalid number of arguments. Expected "PLACE X,Y,F".'}

        x, y, facing = params

        # Validate x and y as integers
        if not self._is_integer(x):
            return {
                'is_valid': False,
                'message': 'Invalid x value. Please provide an integer.'
            }

        if not self._is_integer(y):
            return {
                'is_valid': False,
                'message': 'Invalid y value. Please provide an integer.'
            }

        if not self._is_within_bounds(x, y):
            return {'is_valid': False, 'message': f'x or y value out of bounds. Expected x: 0 to {self.board_width - 1}, y: 0 to {self.board_height - 1}.'}

        # Validate facing direction
        if facing not in self.valid_directions:
            return {
                'is_valid': False,
                'message': 'Invalid facing direction. Allowed values: NORTH, EAST, SOUTH, WEST.'
            }

        # Return the validated result
        return {
            'x': int(x),
            'y': int(y),
            'facing': facing,
            'is_valid': True,
            'message': 'Place command validated successfully.'
        }

    def validate_command(self, command):
        """
        Validate if a command is recognized.

        Parameters:
        - command (str): Command to validate.

        Returns:
        - bool: True if the command is valid, False otherwise.
        """
        return command in ['MOVE', 'LEFT', 'RIGHT', 'REPORT'] + ['PLACE']

    def validate_placement(self, robot):
        """
        Check if the robot is placed on the board.

        Parameters:
        - robot (ToyRobot): The robot instance.

        Returns:
        - bool: True if the robot is placed on the board, False otherwise.
        """
        return robot.is_placed
