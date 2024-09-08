import os
import sys 
import unittest
from unittest.mock import MagicMock

# Ensure app folder is in the path
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))

from toy_robot import ToyRobot
from main import parse_command 

class TestParseCommand(unittest.TestCase):
    
    def setUp(self):
        """
        Set up a ToyRobot instance before each test.
        """
        self.robot = ToyRobot()
        self.robot.place = MagicMock()
        self.robot.move = MagicMock()
        self.robot.left = MagicMock()
        self.robot.right = MagicMock()
        self.robot.report = MagicMock()

    def test_parse_command_place(self):
        """
        Test the parse_command function with a valid PLACE command.
        """
        command = 'PLACE 1,2,NORTH'
        parse_command(self.robot, command)
        
        self.robot.place.assert_called_once_with(command)
        self.robot.move.assert_not_called()
        self.robot.left.assert_not_called()
        self.robot.right.assert_not_called()
        self.robot.report.assert_not_called()

    def test_parse_command_move(self):
        """
        Test the parse_command function with a valid MOVE command.
        """
        command = 'MOVE'
        parse_command(self.robot, command)
        
        self.robot.move.assert_called_once()
        self.robot.place.assert_not_called()
        self.robot.left.assert_not_called()
        self.robot.right.assert_not_called()
        self.robot.report.assert_not_called()

    def test_parse_command_left(self):
        """
        Test the parse_command function with a valid LEFT command.
        """
        command = 'LEFT'
        parse_command(self.robot, command)
        
        self.robot.left.assert_called_once()
        self.robot.place.assert_not_called()
        self.robot.move.assert_not_called()
        self.robot.right.assert_not_called()
        self.robot.report.assert_not_called()

    def test_parse_command_right(self):
        """
        Test the parse_command function with a valid RIGHT command.
        """
        command = 'RIGHT'
        parse_command(self.robot, command)
        
        self.robot.right.assert_called_once()
        self.robot.place.assert_not_called()
        self.robot.move.assert_not_called()
        self.robot.left.assert_not_called()
        self.robot.report.assert_not_called()

    def test_parse_command_report(self):
        """
        Test the parse_command function with a valid REPORT command.
        """
        command = 'REPORT'
        parse_command(self.robot, command)
        
        self.robot.report.assert_called_once()
        self.robot.place.assert_not_called()
        self.robot.move.assert_not_called()
        self.robot.left.assert_not_called()
        self.robot.right.assert_not_called()

    def test_parse_command_invalid(self):
        """
        Test the parse_command function with an invalid command.
        """
        command = 'JUMP'
        with self.assertLogs(level='INFO') as log:
            result = parse_command(self.robot, command)
            self.assertFalse(result)
            self.assertIn("Invalid command: JUMP", log.output[0])

if __name__ == '__main__':
    unittest.main()
