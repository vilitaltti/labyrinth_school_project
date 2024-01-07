from labyrinth import Labyrinth
import random
import unittest


class TestBasicFunctionsOfLabyrinth(unittest.TestCase):

    width = 5
    length = 2 
    depth = 2 

    def test_methods_init_field_add_neighbours_and_get_cell(self):
        tmp = Labyrinth(TestBasicFunctionsOfLabyrinth.width,TestBasicFunctionsOfLabyrinth.length,TestBasicFunctionsOfLabyrinth.depth)
        tmp.init_field()
        for key in tmp.field.keys():
            self.assertTrue(type(tmp.field[key]).__name__ == 'Cell')
        for x in range(TestBasicFunctionsOfLabyrinth.width):
            for y in range(TestBasicFunctionsOfLabyrinth.length):
                for z in range(TestBasicFunctionsOfLabyrinth.depth):
                    self.assertTupleEqual((x,y,z),tmp.get_cell(x,y,z).get_location())
                    self.assertFalse(tmp.get_cell(x,y,z).there_is_player)
                    self.assertFalse(tmp.get_cell(x,y,z).is_goal)
                    self.assertTupleEqual((x,y,z),tmp.get_cell((x,y,z)).get_location())
        self.assertTrue(tmp.add_neighbours(0,0,0,1,0,0))
        self.assertTrue(tmp.add_neighbours(0,0,0,0,1,0))
        self.assertTrue(tmp.add_neighbours(0,0,0,0,1,1))
        self.assertTrue(tmp.add_neighbours(0,0,0,3,0,0))
        self.assertFalse(tmp.add_neighbours(0,0,0,1,0,0))
        self.assertFalse(tmp.add_neighbours(0,0,0,0,0,0))

    def test_method_get_locations_get_goal_and_get_player(self):
        random.seed(1)
        tmp = Labyrinth(TestBasicFunctionsOfLabyrinth.width,TestBasicFunctionsOfLabyrinth.length,TestBasicFunctionsOfLabyrinth.depth)
        tmp.initialize_the_labyrinth()
        loc = tmp.get_player_location()
        goal = tmp.get_goal_location()
        self.assertTupleEqual(tmp.goal, goal)
        self.assertTupleEqual(tmp.player_location, loc)
        self.assertEqual(tmp.get_cell(loc),tmp.get_cell((1,0,1)))
        self.assertEqual(tmp.get_cell(goal),tmp.get_cell((0,0,0)))

    def test_method_update_location(self):
        random.seed(1)
        tmp = Labyrinth(TestBasicFunctionsOfLabyrinth.width,TestBasicFunctionsOfLabyrinth.length,TestBasicFunctionsOfLabyrinth.depth)
        tmp.initialize_the_labyrinth()
        loc = tmp.get_player_location() # (1,0,1)
        goal = tmp.get_goal_location() # (0,0,0)
        self.assertTrue(tmp.get_cell(goal).is_goal)

        self.assertFalse(tmp.update_player_location((4,0,1)))
        self.assertTrue(tmp.get_player().there_is_player)
        self.assertFalse(tmp.get_cell((4,0,1)).there_is_player)
        self.assertTrue(tmp.update_player_location((2,0,1)))
        self.assertFalse(tmp.get_cell(loc).there_is_player)
        self.assertTrue(tmp.get_cell((2,0,1)).there_is_player)



if __name__ == "__main__":
    unittest.main()
    
