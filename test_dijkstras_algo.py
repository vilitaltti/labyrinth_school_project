import unittest
from labyrinth import Labyrinth

class TestDijks(unittest.TestCase):

    def test_straight_path(self):
        lab = Labyrinth(3,3,1)
        lab.init_field()
        # ---
        # ..|
        # ---
        lab.add_neighbours(0,0,0,1,0,0)
        lab.add_neighbours(1,0,0,2,0,0)
        lab.add_neighbours(2,0,0,2,1,0)
        lab.add_neighbours(2,1,0,2,2,0)
        lab.add_neighbours(2,2,0,1,2,0)
        lab.add_neighbours(1,2,0,0,2,0)
        sta = lab.dijkstras_alg(lab.get_cell(0,0,0),lab.get_cell(0,2,0))
        
        self.assertEqual(sta.pop().get_location_str(),"000")
        self.assertEqual(sta.pop().get_location_str(),"100")
        self.assertEqual(sta.pop().get_location_str(),"200")
        self.assertEqual(sta.pop().get_location_str(),"210")
        self.assertEqual(sta.pop().get_location_str(),"220")
        self.assertEqual(sta.pop().get_location_str(),"120")
        self.assertEqual(sta.pop().get_location_str(),"020")

    def test_1(self):
        # ---
        # |.|
        # ---
        lab = Labyrinth(3,3,1)
        lab.init_field()
        lab.add_neighbours(0,0,0,1,0,0)
        lab.add_neighbours(1,0,0,2,0,0)
        lab.add_neighbours(2,0,0,2,1,0)
        lab.add_neighbours(2,1,0,2,2,0)
        lab.add_neighbours(2,2,0,1,2,0)
        lab.add_neighbours(1,2,0,0,2,0)
        lab.add_neighbours(0,2,0,0,1,0)
        lab.add_neighbours(0,1,0,0,0,0)

        sta = lab.dijkstras_alg(lab.get_cell(0,0,0),lab.get_cell(2,1,0))
        
        self.assertEqual(sta.pop().get_location_str(),"000")
        self.assertEqual(sta.pop().get_location_str(),"100")
        self.assertEqual(sta.pop().get_location_str(),"200")
        self.assertEqual(sta.pop().get_location_str(),"210")

    def test_2(self):
        # ----
        # |+.|
        # ----
        lab = Labyrinth(4,3,1)
        lab.init_field()
        lab.add_neighbours(0,0,0,1,0,0)
        lab.add_neighbours(1,0,0,2,0,0)
        lab.add_neighbours(2,0,0,3,0,0)
        lab.add_neighbours(3,0,0,3,1,0)
        lab.add_neighbours(3,1,0,3,2,0)
        lab.add_neighbours(3,2,0,2,2,0)
        lab.add_neighbours(2,2,0,1,2,0)
        lab.add_neighbours(1,2,0,0,2,0)
        lab.add_neighbours(0,2,0,0,1,0)
        lab.add_neighbours(0,1,0,0,0,0)

        lab.add_neighbours(1,1,0,0,1,0)
        lab.add_neighbours(1,1,0,2,1,0)
        lab.add_neighbours(1,1,0,1,0,0)
        lab.add_neighbours(1,1,0,1,2,0)

        sta = lab.dijkstras_alg(lab.get_cell(0,0,0),lab.get_cell(3,2,0))
        
        self.assertEqual(sta.pop().get_location_str(),"000")
        sta.pop()
        sta.pop()
        sta.pop()
        self.assertEqual(sta.pop().get_location_str(),"220")
        self.assertEqual(sta.pop().get_location_str(),"320")

    def test_3(self):
        # --- x-- x--
        # |.x |.x |.|
        # --- --- ---
      
        lab = Labyrinth(3,3,3)
        lab.init_field()

        # paths to top floors
        lab.add_neighbours(2,1,0,2,1,1)
        lab.add_neighbours(0,0,1,0,0,2)

        lab.add_neighbours(0,0,0,1,0,0)
        lab.add_neighbours(1,0,0,2,0,0)
        lab.add_neighbours(2,0,0,2,1,0)
        lab.add_neighbours(2,1,0,2,2,0)
        lab.add_neighbours(2,2,0,1,2,0)
        lab.add_neighbours(1,2,0,0,2,0)
        lab.add_neighbours(0,2,0,0,1,0)
        lab.add_neighbours(0,1,0,0,0,0)

        lab.add_neighbours(0,0,1,1,0,1)
        lab.add_neighbours(1,0,1,2,0,1)
        lab.add_neighbours(2,0,1,2,1,1)
        lab.add_neighbours(2,1,1,2,2,1)
        lab.add_neighbours(2,2,1,1,2,1)
        lab.add_neighbours(1,2,1,0,2,1)
        lab.add_neighbours(0,2,1,0,1,1)
        lab.add_neighbours(0,1,1,0,0,1)

        lab.add_neighbours(0,0,2,1,0,2)
        lab.add_neighbours(1,0,2,2,0,2)
        lab.add_neighbours(2,0,2,2,1,2)
        lab.add_neighbours(2,1,2,2,2,2)
        lab.add_neighbours(2,2,2,1,2,2)
        lab.add_neighbours(1,2,2,0,2,2)
        lab.add_neighbours(0,2,2,0,1,2)
        lab.add_neighbours(0,1,2,0,0,2)

        sta = lab.dijkstras_alg(lab.get_cell(0,0,0),lab.get_cell(2,1,2))

        self.assertEqual(sta.pop().get_location_str(),"000")
        self.assertEqual(sta.pop().get_location_str(),"100")
        self.assertEqual(sta.pop().get_location_str(),"200")
        self.assertEqual(sta.pop().get_location_str(),"210")
        self.assertEqual(sta.pop().get_location_str(),"211")
        self.assertEqual(sta.pop().get_location_str(),"201")
        self.assertEqual(sta.pop().get_location_str(),"101")
        self.assertEqual(sta.pop().get_location_str(),"001")
        self.assertEqual(sta.pop().get_location_str(),"002")
        self.assertEqual(sta.pop().get_location_str(),"102")
        self.assertEqual(sta.pop().get_location_str(),"202")
        self.assertEqual(sta.pop().get_location_str(),"212")
        

if __name__ == '__main__':
    unittest.main()
        
