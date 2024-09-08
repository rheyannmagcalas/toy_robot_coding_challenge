import os
import sys
import io
import unittest
from unittest.mock import patch
import logging

# Ensure app folder is in the path
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))

from toy_robot import ToyRobot
from validation import TableValidator

class TestToyRobot(unittest.TestCase):
    
    def setUp(self):
        self.robot = ToyRobot()
        self.log_stream = io.StringIO()
        logging.basicConfig(stream=self.log_stream, level=logging.INFO)
        
    def _get_log_output(self):
        self.log_stream.seek(0)
        return self.log_stream.getvalue()

    @patch.object(TableValidator, 'validate_place', return_value={'is_valid': True, 'x': 0, 'y': 0, 'facing': 'NORTH'})
    @patch.object(TableValidator, 'validate_placement', return_value=True)
    def test_scenario_a(self, mock_validate_placement, mock_validate_place):
        """
        Testing from example number one
        """
        self.robot.place({'x': 0, 'y': 0, 'facing': 'NORTH'})
        self.robot.move()
        result = self.robot.report()
        
        self.assertIn('Output: 0,1,NORTH', result)
    
    @patch.object(TableValidator, 'validate_place', return_value={'is_valid': True, 'x': 0, 'y': 0, 'facing': 'NORTH'})
    @patch.object(TableValidator, 'validate_placement', return_value=True)
    def test_scenario_b(self, mock_validate_placement, mock_validate_place):
        """
        Testing from example number two
        """
        self.robot.place({'x': 0, 'y': 0, 'facing': 'NORTH'})
        self.robot.left()
        result = self.robot.report()
        
        self.assertIn('Output: 0,0,WEST', result)
    
    @patch.object(TableValidator, 'validate_place', return_value={'is_valid': True, 'x': 1, 'y': 2, 'facing': 'EAST'})
    @patch.object(TableValidator, 'validate_placement', return_value=True)
    def test_scenario_c(self, mock_validate_placement, mock_validate_place):
        """
        Testing from example number three
        """
        self.robot.place({'x': 1, 'y': 2, 'facing': 'EAST'})
        self.robot.move()
        self.robot.move()
        self.robot.left()
        self.robot.move()
        result = self.robot.report()
        
        self.assertIn('Output: 3,3,NORTH', result)

    def test_place_valid(self):
        """
        Test the place method with valid input.
        """
        self.robot.place('PLACE 1,2,NORTH')
        self.assertTrue(self.robot.is_placed)
        self.assertEqual(self.robot.x, 1)
        self.assertEqual(self.robot.y, 2)
        self.assertEqual(self.robot.facing, 'NORTH')

    def test_place_invalid_x_command(self):
        """
        Test the place method with an x parameter.
        """
        self.robot.place('PLACE A,2,NORTH')
        self.assertEqual(self.robot.message, 'Invalid x value. Please provide an integer.')
    
    def test_place_invalid_x_command(self):
        """
        Test the place method with an y parameter.
        """
        self.robot.place('PLACE 1,B,NORTH')
        self.assertEqual(self.robot.message, 'Invalid y value. Please provide an integer.')


    def test_place_invalid_facing_command(self):
        """
        Test the place method with an y parameter.
        """
        self.robot.place('PLACE 1,1,TEST')
        self.assertEqual(self.robot.message, 'Invalid facing direction. Allowed values: NORTH, EAST, SOUTH, WEST.')


    def test_place_invalid_range_command(self):
        """
        Test the place method with an y parameter.
        """
        self.robot.place('PLACE 6,6,TEST')
        self.assertEqual(self.robot.message, 'x or y value out of bounds. Expected x: 0 to 4, y: 0 to 4.')


    def test_move(self):
        """
        Test the move method.
        """
        self.robot.place('PLACE 1,1,EAST')
        self.robot.move() 
        self.assertEqual(self.robot.x, 2)
        self.assertEqual(self.robot.y, 1)

    def test_move_falling_off_right(self):
        """
        Test moving the robot to the right edge of the board to ensure it does not fall off.
        """
        self.robot.place('PLACE 4,1,EAST')
        self.robot.move() # Should not move
        self.assertEqual(self.robot.x, 4)
        self.assertEqual(self.robot.y, 1)

    def test_move_falling_off_left(self):
        """
        Test moving the robot to the left edge of the board to ensure it does not fall off.
        """
        self.robot.place('PLACE 0,1,WEST')
        self.robot.move() # Should not move
        self.assertEqual(self.robot.x, 0)
        self.assertEqual(self.robot.y, 1)

    def test_move_falling_off_north(self):
        """
        Test moving the robot to the top edge of the board to ensure it does not fall off.
        """
        self.robot.place('PLACE 1,4,NORTH')
        self.robot.move()  # Should not move
        self.assertEqual(self.robot.x, 1)
        self.assertEqual(self.robot.y, 4)

    def test_move_falling_off_south(self):
        """
        Test moving the robot to the bottom edge of the board to ensure it does not fall off.
        """
        self.robot.place('PLACE 1,0,SOUTH')
        self.robot.move()  # Should not move
        self.assertEqual(self.robot.x, 1)
        self.assertEqual(self.robot.y, 0)

    def test_left_rotation(self):
        """
        Test the left rotation method.
        """
        self.robot.place('PLACE 1,1,NORTH')
        self.robot.left()
        self.assertEqual(self.robot.facing, 'WEST')

    def test_right_rotation(self):
        """
        Test the right rotation method.
        """
        self.robot.place('PLACE 1,1,NORTH')
        self.robot.right()
        self.assertEqual(self.robot.facing, 'EAST')

    def test_report(self):
        """
        Test the report method.
        """
        self.robot.place('PLACE 1,1,NORTH')
        output = self.robot.report()
        self.assertEqual(output, 'Output: 1,1,NORTH')

    def test_move_when_not_placed(self):
        """
        Test the move method when the robot is not placed on the board.
        """
        self.robot.move()
        self.assertEqual(self.robot.x, None)
        self.assertEqual(self.robot.y, None)
        self.assertEqual(self.robot.facing, None)

    def test_left_when_not_placed(self):
        """
        Test the left rotation method when the robot is not placed on the board.
        """
        self.robot.left()
        self.assertEqual(self.robot.facing, None)

    def test_right_when_not_placed(self):
        """
        Test the right rotation method when the robot is not placed on the board.
        """
        self.robot.right()
        self.assertEqual(self.robot.facing, None)


if __name__ == '__main__':
    unittest.main()
