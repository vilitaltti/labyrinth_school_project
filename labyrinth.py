import cell
import sys
import stack 
import random

class Labyrinth():

    def __init__(self,width=1,length=1,depth=1):
        self.width = width
        self.length = length
        self.depth = depth
        self.field = dict()
        self.player_location = (0,0,0)
        self.goal = (0,0,0)

    def init_field(self):
        """ intializes unique cell object in field"""
        for x in range(self.width):
            for y in range(self.length):
                for z in range(self.depth):
                    tmp = cell.Cell()
                    tmp.location = (x,y,z)
                    self.field[tmp.get_location_str()] = tmp

    def get_player_location(self):
        """Returns palyer's location 3x1 tuple"""
        return self.player_location

    def get_goal_location(self):
        """Returns goal's location 3x1 tuple"""
        return self.goal

    def get_cell(self,x,y=None,z=None):
        """Returns cell according to x,y,z or with maching tuple (x,y,z)"""
        if type(x) is not tuple:
            return self.field["{}{}{}".format(x,y,z)]
        else:
            return self.field["{}{}{}".format(x[0],x[1],x[2])]

    def get_goal(self):
        """Return goal's cell"""
        return self.get_cell(self.goal[0],self.goal[1],self.goal[2])

    def get_player(self):
        """Return player's cell"""
        return self.get_cell(self.player_location[0],self.player_location[1],self.player_location[2])

    def add_neighbours(self,x1,y1,z1,x2,y2,z2):
        """ makes locations cells become neighbours"""
        cell1 = self.get_cell(x1,y1,z1)
        cell2 = self.get_cell(x2,y2,z2)
        if cell1 not in cell2.neighbours and cell1.location != cell2.location:
            cell2.neighbours.append(cell1)
            cell1.neighbours.append(cell2)
            return True
        return False


    def update_player_location(self,new_location):
        """ updates player's location, new_location is  3x1 tuple"""
        new_cell = self.get_cell(new_location)
        curr_cell = self.get_cell(self.player_location)
        if new_cell in curr_cell.neighbours:
            self.player_location = new_location 
            new_cell.there_is_player = True
            curr_cell.there_is_player = False 
            return True
        else:
            return False
        
    def dijkstras_alg(self,start,end):
        """ start and end types are Cells. The pseudocode has been got from the wikipedia page: https://en.wikipedia.org/wiki/Dijkstra's_algorithm """
        dist = dict()
        prev = dict()
        vertexs = set()

        for i in self.field.keys():
            dist[i] = sys.maxsize # works like inf
            prev[i] = None # works like undefined
            vertexs.add(self.field[i])

        dist[start.get_location_str()] = 0

        while len(vertexs) > 0:

            lst = list(dist.keys())
            smallest = lst[0]
            for key in lst:
                if dist[key] < dist[smallest]:
                    smallest = key

            cell1 = self.field[smallest]
            vertexs.remove(cell1)

            if cell1 == end:
                break 

            alt = dist[cell1.get_location_str()] + 1 # since the distace is constant between vertexes
            for neighbour in cell1.neighbours:
                if neighbour in vertexs and alt < dist[neighbour.get_location_str()]:
                   dist[neighbour.get_location_str()] = alt 
                   prev[neighbour.get_location_str()] = cell1
            dist.pop(smallest)

        stack1 = stack.Stack()
        tmp = end
        if prev[tmp.get_location_str()]!= None or tmp == start:
            while tmp != None:
                stack1.push(tmp)
                tmp = prev[tmp.get_location_str()]
        return stack1

    def initialize_the_labyrinth(self):
        """The following pseudo algorithim has been got from wikipedia"""
        self.init_field()
        init_cell = self.get_cell(random.randint(0,self.width-1),random.randint(0,self.length-1),random.randint(0,self.depth-1))
        self.player_location = init_cell.get_location()
        init_cell.there_is_player = True
        visited = set({init_cell})
        sta = stack.Stack()
        sta.push(init_cell)
        

        while not sta.is_empty():
            curr = sta.pop()

            x_plus= curr.location[0]+1
            x_minus= curr.location[0]-1
            y_plus= curr.location[1]+1 
            y_minus= curr.location[1]-1
            z_plus= curr.location[2]+1 
            z_minus= curr.location[2]-1 

            possible_neighbours = []

            if x_minus >= 0:
                possible_neighbours.append(self.get_cell(x_minus,curr.location[1],curr.location[2]))
            if x_plus < self.width:
                possible_neighbours.append(self.get_cell(x_plus,curr.location[1],curr.location[2]))
            if y_minus >= 0:
                possible_neighbours.append(self.get_cell(curr.location[0],y_minus,curr.location[2]))
            if y_plus < self.length:
                possible_neighbours.append(self.get_cell(curr.location[0],y_plus,curr.location[2]))
            if z_minus >= 0:
                possible_neighbours.append(self.get_cell(curr.location[0],curr.location[1],z_minus))
            if z_plus < self.depth:
                possible_neighbours.append(self.get_cell(curr.location[0],curr.location[1],z_plus))

            while len(possible_neighbours) > 0:
                i = possible_neighbours[random.randint(0,len(possible_neighbours)-1)]
                possible_neighbours.remove(i)
                if i not in visited:
                    sta.push(curr)
                    self.add_neighbours(i.location[0],i.location[1],i.location[2],curr.location[0],curr.location[1],curr.location[2])
                    sta.push(i)
                    visited.add(i)

        cpy = list(self.field.values())
        cpy.remove(self.get_player())
        tmp1 = random.choice(cpy) 
        ret =  self.dijkstras_alg(self.get_player(),tmp1)
        while ret.is_empty():
            cpy.remove(tmp1)
            tmp1 = random.choice(cpy)
            ret =  self.dijkstras_alg(self.get_player(),tmp1)
        tmp1.is_goal = True
        self.goal = tmp1.get_location()
        return True 


    def import_labyrinth(self,input_file_name):
        """ imports labyrinth object from file name input_file_name,which is string object """
        if input_file_name[-10:] !=".labyrinth":
            raise LabyrinthError("Unknown file type")

        try:
            the_file = open(input_file_name,'r')
            return self.import_labyrinth_from_file(the_file)
        except:
            raise


    def import_labyrinth_from_file(self,input_file):
        """ imports labyrinth object from file name input_file,which is file object """
        try:

            def read_one_line_input(file1):
                read_line = file1.readline()
                parsed = []
                if ':' in read_line:
                    parsed = read_line.strip().split(':')
                else:
                    parsed = read_line.strip().split()
                return read_line,parsed

            def read_coordinates_from_str(string):
                list1 = string.strip().split(',')
                a = int(list1[0][1:])
                b = int(list1[1])
                c = int(list1[2][:-1])
                return (a,b,c)

            plyr_read = False
            field_read = False
            dims_read = False
            goal_read = False

            read_line,parsed = read_one_line_input(input_file)
            prev_line = None
            
            if len(parsed) != 2 or parsed[0].lower() != 'labyrinth':
                raise LabyrinthError("Unknown file")

            while read_line != prev_line or not (plyr_read and field_read and dims_read and goal_read):
                if len(parsed) > 0:
                    if parsed[0] == "pelaaja" or parsed[0] == "player":
                        self.player_location = read_coordinates_from_str(parsed[1])
                        plyr_read = True
                    elif parsed[0]== "dimenssiot" or parsed[0] == "dimensions":
                        cord = read_coordinates_from_str(parsed[1])
                        self.width = cord[0]
                        self.length = cord[1]
                        self.depth = cord[2]
                        dims_read = True
                    elif parsed[0] == "maali" or parsed[0] == "goal":
                        self.goal = read_coordinates_from_str(parsed[1])
                        goal_read = True
                    elif parsed[0] == "field" and parsed[1] == '{':
                        if dims_read:
                            self.init_field()
                        else:
                            raise LabyrinthError("Field is read before dimensions")
                        # if there are spaces in between the cells it does not work
                        while True:
                            read_line,parsed = read_one_line_input(input_file)
                            if '}' in parsed:
                                break
                            neigh = []
                            curr_cord = read_coordinates_from_str(parsed[0])
                            curr = self.get_cell(curr_cord[0],curr_cord[1],curr_cord[2])
                            if ',' in parsed[1]:
                                neigh = parsed[1].split(';')
                            for i in neigh:
                                cord = read_coordinates_from_str(i)
                                cell =  self.get_cell(cord[0],cord[1],cord[2]) 
                                if cell not in curr.neighbours:
                                    self.add_neighbours(curr_cord[0],curr_cord[1],curr_cord[2],cord[0],cord[1],cord[2])
                        # not working in general case but this is a quick fix
                        field_read = True
                prev_line = read_line
                read_line,parsed = read_one_line_input(input_file)


            if not dims_read:
                raise LabyrinthError("Missing the dimmensions part") 
            if not goal_read:
                raise LabyrinthError("Missing the goal location part") 
            if not plyr_read:
                raise LabyrinthError("Missing the palyer location part") 
            if not field_read:
                raise LabyrinthError("Missing the field part") 

            goal_cell = self.get_cell(self.goal[0],self.goal[1],self.goal[2])
            player_cell = self.get_cell(self.player_location[0],self.player_location[1],self.player_location[2])

            if self.dijkstras_alg(player_cell,goal_cell).is_empty():
                raise LabyrinthError("No path between goal and player")

            goal_cell.is_goal = True
            player_cell.there_is_player = True

            return True

        except:
            input_file.close()
            raise

    def export_labyrinth(self,output_file_name):
        """ writes labyrinth object to a file named as output_file_name which is string object """
        try:
            ofile = open("{}.labyrinth".format(output_file_name),"w")
            ofile.write("labyrinth:1.0\n")
            ofile.write("dimensions:({},{},{})\n".format(self.width,self.length,self.depth))
            ofile.write("player:{}\n".format(self.get_player_location()))
            ofile.write("goal:{}\n".format(self.get_goal_location()))
            ofile.write("field:{\n")
            for i in self.field.keys():
                ofile.write("{}:".format(self.field[i].location))
                for j in range(len(self.field[i].neighbours)):
                    if j == len(self.field[i].neighbours)-1:
                        ofile.write("{}\n".format(self.field[i].neighbours[j].get_location()))
                    else:
                        ofile.write("{};".format(self.field[i].neighbours[j].get_location()))
            ofile.write("}\n")
            ofile.close()
        except:
            raise
        

class LabyrinthError(Exception):
    # Same as definition as in exercise humanreadable week 6
    def __init__(self,message):    
        super(LabyrinthError,self).__init__(message)
