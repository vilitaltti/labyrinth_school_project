class Cell():

    def __init__(self):
        self.location = None # (x,y,z)
        self.is_goal = False
        self.there_is_player = False
        self.neighbours = []

    def get_location(self):
        return self.location

    def get_location_str(self):
        if self.location != None:
            return "{}{}{}".format(self.location[0],self.location[1],self.location[2])
        return ""

    def is_neighbour(self,cell):
        return cell in self.neighbours

