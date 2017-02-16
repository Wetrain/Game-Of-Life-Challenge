import sys
sys.path.append("..")

from gameoflife.Life import Life
import unittest

class testLife(unittest.TestCase):

    def test_no_interaction(self):
        """Test that nothing occurs when initial state is dead"""
        emptyState = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        """Test that nothing occurs when initial state is dead"""
        finalState = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        testLife = Life(emptyState, 3)
        self.assertEqual(finalState, next(testLife.evolve(1)))

    def test_under_population(self):
        """Test that a cell dies due to under-population"""
        underState = [[0, 0, 0],
                      [0, 1, 0],
                      [0, 0, 0]]

        finalState = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        testLife = Life(underState, 3)
        self.assertEqual(finalState, next(testLife.evolve(1)))

    def test_over_population(self):
        """Test that a cell does die due to over-population"""
        overState = [[0, 1, 0],
                     [1, 1, 1],
                     [0, 1, 0]]

        finalState = [[1, 1, 1],
                      [1, 0, 1],
                      [1, 1, 1]]

        testLife = Life(overState, 3)
        self.assertEqual(finalState, next(testLife.evolve(1)))

    def test_survival_population(self):
        """Test that a cell survives due to not being over/under populated"""
        survivalState = [[1, 1, 0],
                         [1, 0, 0],
                         [0, 0, 0]]

        finalState = [[1, 1, 0],
                      [1, 1, 0],
                      [0, 0, 0]]

        testLife = Life(survivalState, 3)
        self.assertEqual(finalState, next(testLife.evolve(1)))

    def test_reproduction_population(self):
        """Test that a cell is born due to reproduction"""

        birthState = [[1, 1, 1],
                      [0, 0, 0],
                      [0, 0, 0]]

        finalState = [[0, 1, 0],
                      [0, 1, 0],
                      [0, 0, 0]]

        testLife = Life(birthState, 3)
        self.assertEqual(finalState, next(testLife.evolve(1)))

    def test_seeded_generation(self):
        """Tests a seeded input"""
        seedState = [ [0, 0, 0],
                      [1, 1, 1],
                      [0, 0, 0] ]

        state1 = [     [0, 1, 0],
                       [0, 1, 0],
                       [0, 1, 0] ]

        state2 = [     [0, 0, 0],
                       [1, 1, 1],
                       [0, 0, 0] ]
        
        testLife = Life(seedState, 3)

        states = testLife.evolve(2)

        self.assertEqual(state1, next(states))
        self.assertEqual(state2, next(states))



