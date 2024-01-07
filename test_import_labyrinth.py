import unittest
from io import StringIO
import labyrinth

input_file = "test_labyrinth_reading.labyrinth"


class Test(unittest.TestCase):

    def test_straight_line(self):
        self.input_file = StringIO()
        self.input_file.write('labyrinth:1.0\n')
        self.input_file.write('dimensions:(4,1,1)\n')
        self.input_file.write('player:(0,0,0)\n')
        self.input_file.write('goal:(3,0,0)\n')
        # @ --- G
        self.input_file.write('field:{\n')
        self.input_file.write('(0,0,0):(1,0,0)\n')
        self.input_file.write('(1,0,0):(0,0,0);(2,0,0)\n')
        self.input_file.write('(2,0,0):(1,0,0);(3,0,0)\n')
        self.input_file.write('(3,0,0):(2,0,0)\n')
        self.input_file.write('}')

        self.input_file.seek(0,0)

        a = labyrinth.Labyrinth() 

        try:
            a.import_labyrinth_from_file(self.input_file)
            self.input_file.close() 

            self.assertEqual(a.width,4)
            self.assertEqual(a.length,1)
            self.assertEqual(a.depth,1)

            self.assertEqual(a.get_player_location(),(0,0,0))
            self.assertEqual(a.get_goal_location(),(3,0,0))

            self.assertEqual(len(a.field),a.width*a.length*a.depth)
            
            self.assertEqual(len(a.get_cell(0,0,0).neighbours),1)
            self.assertEqual(a.get_cell(0,0,0).neighbours[0].get_location(),(1,0,0))

            self.assertEqual(len(a.get_cell(1,0,0).neighbours),2)
            self.assertEqual(a.get_cell(1,0,0).neighbours[1].get_location(),(2,0,0))
            self.assertEqual(a.get_cell(1,0,0).neighbours[0].get_location(),(0,0,0))

            self.assertEqual(len(a.get_cell(2,0,0).neighbours),2)
            self.assertEqual(a.get_cell(2,0,0).neighbours[0].get_location(),(1,0,0))
            self.assertEqual(a.get_cell(2,0,0).neighbours[1].get_location(),(3,0,0))

            self.assertEqual(len(a.get_cell(3,0,0).neighbours),1)
            self.assertEqual(a.get_cell(3,0,0).neighbours[0].get_location(),(2,0,0))

        except:
            self.input_file.close()
            raise

    def test_2d_case(self):
        self.input_file = StringIO()
        self.input_file.write('labyrinth:1.0\n\n\n\n\n\n\n\n')
        self.input_file.write('dimensions:(4,2,1)\n\n\n\n\n\n\n\n')
        self.input_file.write('  player:(0,0,0)\n\n\n\n\n\n\n\n\n\n')
        self.input_file.write('goal:(0,1,0)\n\n\n\n\n\n\n\n')
        # @--- 
        #    |
        # G---
        self.input_file.write('field:{\n')
        self.input_file.write('(0,0,0):(1,0,0)\n')
        self.input_file.write('(1,0,0):(0,0,0);(2,0,0)\n')
        self.input_file.write('(2,0,0):(1,0,0);(3,0,0)\n')
        self.input_file.write('(3,0,0):   (2,0,0);(3,1,0)\n')
        self.input_file.write('(3,1,0):(2,1,0);(3,0,0)\n')
        self.input_file.write('(2,1,0):(3,1,0);(1,1,0)\n')
        self.input_file.write('(1,1,0):(0,1,0);   (2,1,0)\n')
        self.input_file.write('(0,1,0):(1,1,0)\n')
        self.input_file.write('}')

        self.input_file.seek(0,0)

        a = labyrinth.Labyrinth() 

        try:
            a.import_labyrinth_from_file(self.input_file)
            self.input_file.close() 

            self.assertEqual(a.width,4)
            self.assertEqual(a.length,2)
            self.assertEqual(a.depth,1)

            self.assertEqual(a.get_player_location(),(0,0,0))
            self.assertEqual(a.get_goal_location(),(0,1,0))

            self.assertEqual(len(a.field),a.width*a.length*a.depth)
            
            self.assertEqual(len(a.get_cell(0,0,0).neighbours),1)
            self.assertEqual(a.get_cell(0,0,0).neighbours[0].get_location(),(1,0,0))

            self.assertEqual(len(a.get_cell(1,0,0).neighbours),2)
            self.assertEqual(a.get_cell(1,0,0).neighbours[1].get_location(),(2,0,0))
            self.assertEqual(a.get_cell(1,0,0).neighbours[0],a.get_cell(0,0,0))

            self.assertEqual(len(a.get_cell(2,0,0).neighbours),2)
            self.assertEqual(a.get_cell(2,0,0).neighbours[0].get_location(),(1,0,0))
            self.assertEqual(a.get_cell(2,0,0).neighbours[1].get_location(),(3,0,0))

            self.assertEqual(len(a.get_cell(3,0,0).neighbours),2)
            self.assertEqual(a.get_cell(3,0,0).neighbours[0].get_location(),(2,0,0))
            self.assertEqual(a.get_cell(3,0,0).neighbours[1].get_location(),(3,1,0))

            self.assertEqual(len(a.get_cell(3,1,0).neighbours),2)
            self.assertEqual(a.get_cell(3,1,0).neighbours[1].get_location(),(2,1,0))
            self.assertEqual(a.get_cell(3,1,0).neighbours[0].get_location(),(3,0,0))

            self.assertEqual(len(a.get_cell(2,1,0).neighbours),2)
            self.assertEqual(a.get_cell(2,1,0).neighbours[1].get_location(),(1,1,0))
            self.assertEqual(a.get_cell(2,1,0).neighbours[0].get_location(),(3,1,0))

            self.assertEqual(len(a.get_cell(0,1,0).neighbours),1)
            self.assertEqual(a.get_cell(0,1,0).neighbours[0].get_location(),(1,1,0))

            self.assertEqual(len(a.get_cell(1,1,0).neighbours),2)
            self.assertEqual(a.get_cell(1,1,0).neighbours[0].get_location(),(2,1,0))
            self.assertEqual(a.get_cell(1,1,0).neighbours[1].get_location(),(0,1,0))


        except:
            self.input_file.close()
            raise

    def test_3d_case(self):
        self.input_file = StringIO()
        self.input_file.write('labyrinth:1.0\n')
        self.input_file.write('dimensions:(4,2,2)\n')
        self.input_file.write('player:(0,0,0)\n')
        self.input_file.write('goal:(0,1,1)\n')

        # (0,0,0) - (1,0,0) - (2,0,0) - (3,0,0)
        #    @
        #                        |

        # (0,1,0) - (1,1,0) - (2,1,0) - (3,1,0)

        #    \

        # (0,0,1) - (1,0,1) - (2,0,1) - (3,0,1)

        #                                  |
        #    G
        # (0,1,1) - (1,1,1) - (2,1,1) - (3,1,1)

        self.input_file.write('field:{\n')
        self.input_file.write('(0,0,0):(1,0,0)\n')
        self.input_file.write('(1,0,0):(0,0,0);(2,0,0)\n')
        self.input_file.write('(2,0,0):(1,0,0);(3,0,0);(2,1,0)\n')
        self.input_file.write('(3,0,0):(2,0,0)\n')
        self.input_file.write('(3,1,0):(2,1,0)\n')
        self.input_file.write('(2,1,0):(2,0,0);(1,1,0);(3,1,0)\n')
        self.input_file.write('(1,1,0):(0,1,0);(2,1,0)\n')
        self.input_file.write('(0,1,0):(1,1,0);(0,0,1)\n')

        self.input_file.write('(0,0,1):(0,1,0),(1,0,1)\n')
        self.input_file.write('(1,0,1):(0,0,1);(2,0,1)\n')
        self.input_file.write('(2,0,1):(1,0,1);(3,0,1)\n')
        self.input_file.write('(3,0,1):(2,0,1);(3,1,1)\n')
        self.input_file.write('(3,1,1):(3,0,1);(2,1,1)\n')
        self.input_file.write('(2,1,1):(1,1,1);(3,1,1)\n')
        self.input_file.write('(1,1,1):(0,1,1);(2,1,1)\n')
        self.input_file.write('}')

        self.input_file.seek(0,0)

        a = labyrinth.Labyrinth() 

        try:
            a.import_labyrinth_from_file(self.input_file)
            self.input_file.close() 

            self.assertEqual(a.width,4)
            self.assertEqual(a.length,2)
            self.assertEqual(a.depth,2)

            self.assertEqual(a.get_player_location(),(0,0,0))
            self.assertEqual(a.get_goal_location(),(0,1,1))

            self.assertEqual(len(a.field),a.width*a.length*a.depth)
            
            self.assertEqual(len(a.get_cell(0,0,0).neighbours),1)
            self.assertEqual(a.get_cell(0,0,0).neighbours[0].get_location(),(1,0,0))

            self.assertEqual(len(a.get_cell(1,0,0).neighbours),2)
            self.assertEqual(a.get_cell(1,0,0).neighbours[1].get_location(),(2,0,0))
            self.assertEqual(a.get_cell(1,0,0).neighbours[0],a.get_cell(0,0,0))

            self.assertEqual(len(a.get_cell(2,0,0).neighbours),3)
            self.assertEqual(a.get_cell(2,0,0).neighbours[0].get_location(),(1,0,0))
            self.assertEqual(a.get_cell(2,0,0).neighbours[1].get_location(),(3,0,0))
            self.assertEqual(a.get_cell(2,0,0).neighbours[2].get_location(),(2,1,0))


            self.assertEqual(len(a.get_cell(3,0,0).neighbours),1)
            self.assertEqual(a.get_cell(3,0,0).neighbours[0].get_location(),(2,0,0))

            self.assertEqual(len(a.get_cell(3,1,0).neighbours),1)
            self.assertEqual(a.get_cell(3,1,0).neighbours[0].get_location(),(2,1,0))

            self.assertEqual(len(a.get_cell(2,1,0).neighbours),3)
            self.assertEqual(a.get_cell(2,1,0).neighbours[2].get_location(),(1,1,0))
            self.assertEqual(a.get_cell(2,1,0).neighbours[0].get_location(),(2,0,0))
            self.assertEqual(a.get_cell(2,1,0).neighbours[1].get_location(),(3,1,0))

            self.assertEqual(len(a.get_cell(1,1,0).neighbours),2)
            self.assertEqual(a.get_cell(1,1,0).neighbours[0].get_location(),(2,1,0))
            self.assertEqual(a.get_cell(1,1,0).neighbours[1].get_location(),(0,1,0))

            self.assertEqual(len(a.get_cell(0,1,0).neighbours),2)
            self.assertEqual(a.get_cell(0,1,0).neighbours[0].get_location(),(1,1,0))
            self.assertEqual(a.get_cell(0,1,0).neighbours[1].get_location(),(0,0,1))

            self.assertEqual(len(a.get_cell(0,0,1).neighbours),2)
            self.assertEqual(a.get_cell(0,0,1).neighbours[0].get_location(),(0,1,0))
            self.assertEqual(a.get_cell(0,0,1).neighbours[1].get_location(),(1,0,1))

            self.assertEqual(len(a.get_cell(1,0,1).neighbours),2)
            self.assertEqual(a.get_cell(1,0,1).neighbours[0].get_location(),(0,0,1))
            self.assertEqual(a.get_cell(1,0,1).neighbours[1],a.get_cell(2,0,1))

            self.assertEqual(len(a.get_cell(2,0,1).neighbours),2)
            self.assertEqual(a.get_cell(2,0,1).neighbours[0].get_location(),(1,0,1))
            self.assertEqual(a.get_cell(2,0,1).neighbours[1].get_location(),(3,0,1))

            self.assertEqual(len(a.get_cell(3,0,1).neighbours),2)
            self.assertEqual(a.get_cell(3,0,1).neighbours[0].get_location(),(2,0,1))
            self.assertEqual(a.get_cell(3,0,1).neighbours[1].get_location(),(3,1,1))

            self.assertEqual(len(a.get_cell(3,1,1).neighbours),2)
            self.assertEqual(a.get_cell(3,1,1).neighbours[1].get_location(),(2,1,1))
            self.assertEqual(a.get_cell(3,1,1).neighbours[0].get_location(),(3,0,1))

            self.assertEqual(len(a.get_cell(2,1,1).neighbours),2)
            self.assertEqual(a.get_cell(2,1,1).neighbours[1].get_location(),(1,1,1))
            self.assertEqual(a.get_cell(2,1,1).neighbours[0].get_location(),(3,1,1))

            self.assertEqual(len(a.get_cell(1,1,1).neighbours),2)
            self.assertEqual(a.get_cell(1,1,1).neighbours[0].get_location(),(2,1,1))
            self.assertEqual(a.get_cell(1,1,1).neighbours[1].get_location(),(0,1,1))

            self.assertEqual(len(a.get_cell(0,1,1).neighbours),1)
            self.assertEqual(a.get_cell(0,1,1).neighbours[0].get_location(),(1,1,1))

        except:
            self.input_file.close()
            raise

if __name__ == '__main__':
    unittest.main()
