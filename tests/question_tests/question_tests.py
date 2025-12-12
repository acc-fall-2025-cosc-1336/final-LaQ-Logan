#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_c.question_c import get_most_likely_ancestor_consensus    

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_multiple_positions(self):
        s = "GATATATGCATATACTT"
        t = "ATAT"
        expected = (2, 4, 10)

        positions = get_most_likely_ancestor_consensus(s, t) # Call the function to test
        pos1, pos2, pos3 = positions #variable for each position

        self.assertEqual(pos1, 2) #this is position 1 
        self.assertEqual(pos2, 4) #this is position 2
        self.assertEqual(pos3, 10) #this is position 3

        self.assertEqual(positions, expected) # Final assertion to check the entire tuple for expected value
