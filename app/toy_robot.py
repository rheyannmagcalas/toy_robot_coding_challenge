import logging
from validation import TableValidator

class ToyRobot:
    def __init__(self, board_width=5, board_height=5):
        """
        Initialize the ToyRobot with a board of the specified dimensions.
        
        Parameters:
        - board_width (int): Width of the board.
        - board_height (int): Height of the board.
        """
        self.board_width = board_width
        self.board_height = board_height
        self.x = None
        self.y = None
        self.facing = None
        self.is_placed = False
        self.message = ''
        self.direction_symbols = {
            'NORTH': '^',  
            'EAST': '>',   
            'SOUTH': 'v',  
            'WEST': '<'    
        }
        self.validator = TableValidator(board_width, board_height)
        self.logger = logging.getLogger(self.__class__.__name__)
        logging.basicConfig(
            level=logging.INFO,  
            format='%(levelname)s: %(message)s'
        )

    def place(self, command):
        """
        Place the robot on the board at the specified coordinates and facing direction.
        
        Parameters:
        - command (dict): Dictionary with 'x', 'y', and 'facing' keys.
        """
        result = self.validator.validate_place(command)
        if result['is_valid']:
            self.x = result['x']
            self.y = result['y']
            self.facing = result['facing']
            self.is_placed = True
            self.logger.info('Robot placed at (%d, %d) facing %s', self.x, self.y, self.facing)

        else:
            self.message = result['message']
            self.logger.error(result['message'])

    def move(self):
        """
        Move the robot one unit forward in the direction it is currently facing.
        """
        if self.validator.validate_placement(self):
            old_x, old_y = self.x, self.y
            if self.facing == "NORTH" and self.y < self.board_height - 1:
                self.y += 1
            elif self.facing == "SOUTH" and self.y > 0:
                self.y -= 1
            elif self.facing == "EAST" and self.x < self.board_width - 1:
                self.x += 1
            elif self.facing == "WEST" and self.x > 0:
                self.x -= 1
            else:
                self.logger.warning('Move ignored to prevent falling off the table from (%d, %d) facing %s', old_x, old_y, self.facing)
                return
            self.logger.info('Moved from (%d, %d) to (%d, %d), facing %s', old_x, old_y, self.x, self.y, self.facing)
        else:
            self.logger.error('MOVE command ignored: Robot is not placed on the table.')

    def left(self):
        """
        Rotate the robot 90 degrees to the left (counterclockwise) without changing its position.
        """
        if self.validator.validate_placement(self):
            directions = ["NORTH", "WEST", "SOUTH", "EAST"]
            old_direction = self.facing
            self.facing = directions[(directions.index(self.facing) + 1) % 4]
            self.logger.info('Successfully rotated from %s to %s', old_direction, self.facing)
        else:
            self.logger.error('LEFT command ignored: Robot is not placed on the table.')

    def right(self):
        """
        Rotate the robot 90 degrees to the right (clockwise) without changing its position.
        """
        if self.validator.validate_placement(self):
            directions = ["NORTH", "EAST", "SOUTH", "WEST"]
            old_direction = self.facing
            self.facing = directions[(directions.index(self.facing) + 1) % 4]
            self.logger.info('Robot successfully rotated from %s to %s', old_direction, self.facing)

        else:
            self.logger.error('RIGHT command ignored: Robot is not placed on the table.')

    def _print_board(self):
        """
        Print the board with the robot's current position and facing direction.
        """
        self.logger.info('Current robot location: (%d, %d) %s', self.x, self.y, self.facing)
        board = [[' ' for _ in range(self.board_width)] for _ in range(self.board_height)]
        if self.is_placed:
            board[self.board_height - 1 - self.y][self.x] = self.direction_symbols[self.facing]
        for row in board:
            self.logger.info(' '.join(f"[{cell}]" for cell in row))
        

    def report(self):
        """
        Output the current position and direction of the robot.
        """
        if self.is_placed:
            symbol = self.direction_symbols.get(self.facing, '?')
            output = f"Output: {self.x},{self.y},{self.facing}"
            self._print_board()
            self.logger.info(output)
            return output
        else:
            self.logger.error('REPORT command ignored: Robot is not placed on the table.')
