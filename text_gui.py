
class GraphicCell():

    def __init__(self):
        self.top = []
        self.mid = []
        self.bot = []


    def print_cell(self):
        print(''.join(self.top))
        print(''.join(self.mid))
        print(''.join(self.bot))

class GUI():

    def __init__(self,game):
        self.labyrinth = game
        self.table = []
        for k in range(self.labyrinth.depth):
            tmp2 = []
            for j in range(self.labyrinth.length):
                tmp1 = []
                for i in range(self.labyrinth.width):
                    tmp1.append(GraphicCell())
                tmp2.append(tmp1)
            self.table.append(tmp2)



    def get_graphic_cell(self,x,y,z):
        return self.table[z][y][x]
    
    def init_labyrinth_to_terminal(self):
        self.labyrinth.initialize_the_labyrinth()
        for x in range(0,self.labyrinth.width):
            for y in range(0,self.labyrinth.length):
                for z in range(0,self.labyrinth.depth):
                    cell = self.labyrinth.get_cell(x,y,z)
                    top_str = ['#','#','#']
                    mid_str = ['#','.','#']
                    bot_str = ['#','#','#']
                    for i in cell.neighbours:
                        loc = i.get_location()
                        if loc[0]-1 >= 0:
                             mid_str[0]='-' 
                        if loc[0]+1 < self.labyrinth.width:
                            mid_str[2]='-'
                        if loc[1]-1 >= 0:
                            top_str[1]='|' 
                        if loc[1]+1 < self.labyrinth.length:
                            bot_str[1]='|' 
                        if loc[2]-1 >= 0 and loc[2]+1 < self.labyrinth.depth:
                            mid_str[1]='X'
                        elif loc[2]-1 >= 0:
                            mid_str[1]='\\'
                        elif loc[2]+1 < self.labyrinth.depth:
                            mid_str[1]='/' 

                    cell = self.get_graphic_cell(x,y,z)
                    cell.top = ''.join(top_str)
                    cell.mid = ''.join(mid_str)
                    cell.bot = ''.join(bot_str)

    def print_labyrinth_to_terminal(self):
        h = 1
        for k in self.table:
            print("floor {}".format(h))
            for j in k:
                top_row = []
                mid_row = []
                bot_row = []
                for i in j:
                    top_row.append(i.top)
                    mid_row.append(i.mid)
                    bot_row.append(i.bot)
                print(''.join(top_row))
                print(''.join(mid_row))
                print(''.join(bot_row))
            h += 1
            print()
