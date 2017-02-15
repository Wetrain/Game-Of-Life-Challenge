from gameoflife.Life import Life
import unittest

class testLife(unittest.TestCase):
	
    def test_no_interaction(self):
        """Test that nothing occurs when initial state is dead"""
		emptyState = [  [0,0,0],
				        [0,0,0],
				        [0,0,0]  ]

        """Test that nothing occurs when initial state is dead"""
		finalState = [  [0,0,0],
				        [0,0,0],
				        [0,0,0]  ]
		
        testLife = Life(emptyState)
		self.assertEqual(finalState, testLife.evolve(1))
    
    def test_under_population(self):
        """Test that a cell dies due to under-population"""
		underState = [  [0,0,0],
				        [0,1,0],
                        [0,0,0] ]

        finalState = [  [0,0,0],
                        [0,0,0],
                        [0,0,0] ]
        
        testLife = Life(underState)
        self.assertEqual(finalState, testLife.evolve(1))

    def test_over_population(self):
        """Test that a cell does die due to over-population""" 
        overState = [   [1,1,0],
                        [1,1,0],
                        [1,1,0] ]

		finalState = [  [1,1,0],
				        [0,0,0],
                        [1,1,0] ]

        testLife = Life(overState)
        self.assertEqual(finalState, testLife.evolve(1))

    def test_survival_population(self):
        """Test that a cell survives due to nor being over/under populated"""
        survivalState = [ [1,1,0],
                          [1,0,0],
                          [0,0,0] ]

        finalState = [    [1,1,0],
                          [1,0,0],
                          [0,0,0] ]

        testLife = Life(survivalState)
        self.assertEqual(finalState, testLife.evolve(1))

    def test_creation_population(self):
        """Test that a cell is born due to reproduction"""

        birthState = [    [1,1,1],
                          [0,0,0],
                          [0,0,0] ]

        finalState = [    [1,1,1],
                          [0,1,0],
                          [0,0,0] ]

        testLife = Life(birthState)
        self.assertEqual(finalState, testLife.evolve(1))
