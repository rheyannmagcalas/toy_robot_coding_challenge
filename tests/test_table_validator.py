import os
import sys
import unittest

# Ensure app folder is in the path
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))

from validation import TableValidator

class TestTableValidator(unittest.TestCase):

    def setUp(self):
        """
        Set up a TableValidator instance before each test.
        """
        self.validator = TableValidator(5, 5)  

    def test_validate_place_valid(self):
        """
        Test the validate_place method with valid input.
        """
        command = "PLACE 1,2,NORTH"
        result = self.validator.validate_place(command)
        
        self.assertTrue(result['is_valid'])
        self.assertEqual(result['x'], 1)
        self.assertEqual(result['y'], 2)
        self.assertEqual(result['facing'], 'NORTH')
        self.assertEqual(result['message'], 'Place command validated successfully.')

    def test_validate_place_invalid_x(self):
        """
        Test the validate_place method with an invalid x value (non-integer).
        """
        command = "PLACE A,2,NORTH"
        result = self.validator.validate_place(command)
        
        self.assertFalse(result['is_valid'])
        self.assertEqual(result['message'], 'Invalid x value. Please provide an integer.')

    def test_validate_place_invalid_y(self):
        """
        Test the validate_place method with an invalid y value (non-integer).
        """
        command = "PLACE 1,B,NORTH"
        result = self.validator.validate_place(command)
        
        self.assertFalse(result['is_valid'])
        self.assertEqual(result['message'], 'Invalid y value. Please provide an integer.')

    def test_validate_place_invalid_facing(self):
        """
        Test the validate_place method with an invalid facing direction.
        """
        command = "PLACE 1,2,UPWARD"
        result = self.validator.validate_place(command)
        
        self.assertFalse(result['is_valid'])
        self.assertEqual(result['message'], 'Invalid facing direction. Allowed values: NORTH, EAST, SOUTH, WEST.')

    def test_validate_place_invalid_format(self):
        """
        Test the validate_place method with an invalid command format.
        """
        command = "PLACE 1,2"
        result = self.validator.validate_place(command)
        
        self.assertFalse(result['is_valid'])
        self.assertEqual(result['message'], 'Invalid number of arguments. Expected "PLACE X,Y,F".')

    def test_validate_place_out_of_range_x(self):
        """
        Test the validate_place method with x value out of range.
        """
        command = "PLACE 6,2,NORTH"  # Assuming the grid width is 5
        result = self.validator.validate_place(command)
        
        self.assertFalse(result['is_valid'])
        self.assertEqual(result['message'], 'x or y value out of bounds. Expected x: 0 to 4, y: 0 to 4.')

    def test_validate_place_out_of_range_y(self):
        """
        Test the validate_place method with y value out of range.
        """
        command = "PLACE 1,6,NORTH"  # Assuming the grid height is 5
        result = self.validator.validate_place(command)
        
        self.assertFalse(result['is_valid'])
        self.assertEqual(result['message'], 'x or y value out of bounds. Expected x: 0 to 4, y: 0 to 4.')

    def test_validate_command(self):
        """
        Test the validate_command method with valid and invalid commands.
        """
        self.assertTrue(self.validator.validate_command('MOVE'))
        self.assertTrue(self.validator.validate_command('LEFT'))
        self.assertTrue(self.validator.validate_command('RIGHT'))
        self.assertTrue(self.validator.validate_command('REPORT'))
        self.assertFalse(self.validator.validate_command('JUMP'))

    def test_validate_placement(self):
        """
        Test the validate_placement method.
        """
        class MockRobot:
            is_placed = True
        
        robot = MockRobot()
        self.assertTrue(self.validator.validate_placement(robot))
        
        robot.is_placed = False
        self.assertFalse(self.validator.validate_placement(robot))

if __name__ == '__main__':
    unittest.main()