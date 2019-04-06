import unittest
import io, sys
from planets import *

class Test_planets(unittest.TestCase):

    def test_01(self):
        sys.stdin = io.StringIO("136")
        sys.stdout = student_output = io.StringIO()        
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 51.68 pounds.\nOn Jupiter you would weigh 318.24 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_02(self):
        sys.stdin = io.StringIO("10")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 3.8 pounds.\nOn Jupiter you would weigh 23.4 pounds."
        weight_on_planets()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_03(self): 
        sys.stdin = io.StringIO("0")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 0.0 pounds.\nOn Jupiter you would weigh 0.0 pounds."
        weight_on_planets()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_04(self):
        sys.stdin = io.StringIO("120")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 45.6 pounds.\nOn Jupiter you would weigh 280.8 pounds." 
        weight_on_planets()
        self.assertEqual(expected_out, student_output.getvalue().strip())


if __name__ == "__main__":
        unittest.main()
