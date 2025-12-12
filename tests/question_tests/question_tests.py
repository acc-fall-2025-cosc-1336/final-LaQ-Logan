#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_c.question_c import get_most_likely_ancestor_consensus    
from src.question_a.question_a import get_multiplication_table


class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_multiple_positions(self):
        s = "GATATATGCATATACTT"
        t = "ATAT"
        expected = (2, 4, 10)
class Test_Multiplication_Table(unittest.TestCase): #test class for multiplication table functions

    def test_get_multiplication_table(self):
        table = get_multiplication_table(5, 10)
        expected_table = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
            [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
            [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
            [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        ]   

        self.assertEqual(table[0], [1,2,3,4,5,6,7,8,9,10]) #check first row
        self.assertEqual(table[4], [5,10,15,20,25,30,35,40,45,50])#check last row
        self.assertEqual(table[2][3], 12) #check specific value in table at index [2][3] ( 3rd row, 4th column)

def test_config():
    return True


        positions = get_most_likely_ancestor_consensus(s, t) # Call the function to test
        pos1, pos2, pos3 = positions #variable for each position

        self.assertEqual(pos1, 2) #this is position 1 
        self.assertEqual(pos2, 4) #this is position 2
        self.assertEqual(pos3, 10) #this is position 3

        self.assertEqual(positions, expected) # Final assertion to check the entire tuple for expected value
