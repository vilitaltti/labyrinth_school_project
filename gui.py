from PyQt5 import QtWidgets,QtCore,QtGui
import labyrinth 
import graphic_cell
import random


class GUI(QtWidgets.QMainWindow):

    # I have taken example from robots exercise from week 6
    def __init__(self,labyrinth,square_size):
        super().__init__()
        # Created window ? 
        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)
        self.init_window()
        self.init_buttons()

        self.labyrinth = labyrinth
        self.square_size = square_size

        self.player_graphics_item = None
        self.init_labyrinth()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_player_randomly)
        self.timer.start(250)

    def update_player_randomly(self):
        cell = self.labyrinth.get_player()
        neigh = random.choice(cell.neighbours)
        print(neigh)
        self.labyrinth.update_player_location(neigh.get_location())
        if self.labyrinth.player_location == self.labyrinth.goal:
            print("Victory")
            self.timer.stop()
        self.player_graphics_item.setPos(self.labyrinth.player_location[0]*self.square_size,self.get_yz_point(self.labyrinth.player_location[1],self.labyrinth.player_location[2]))

    def get_yz_point(self,y=0,z=0):
        return self.square_size*(y+z*(self.labyrinth.length+1))


    def init_window(self):

        """ Sets up the window. I have taken example for the exercise robot gui"""

        self.setGeometry(300,300,800,800)
        self.setWindowTitle('Labyrinth 1.0')
        self.show()

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0,0,700,700)

        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)
        

    def init_buttons(self):

        """ init the buttons when is needed """
        self.save_button = QtWidgets.QPushButton("Save")
        self.horizontal.addWidget(self.save_button)

        self.solve_button = QtWidgets.QPushButton("Solve")
        self.horizontal.addWidget(self.solve_button)


    def init_labyrinth(self):
        for x in range(self.labyrinth.width):
            for y in range(self.labyrinth.length):
                for z in range(self.labyrinth.depth):
                    square = graphic_cell.GraphicCell(x*self.square_size,self.get_yz_point(y,z),self.square_size,self.labyrinth.get_cell(x,y,z))
                    self.scene.addItem(square.background)
                    if square.neg_x_wall != None:
                        self.scene.addItem(square.neg_x_wall)
                    if square.pos_x_wall != None:
                        self.scene.addItem(square.pos_x_wall)
                    if square.neg_y_wall != None:
                        self.scene.addItem(square.neg_y_wall)
                    if square.pos_y_wall != None:
                        self.scene.addItem(square.pos_y_wall)
                    if square.z_wall != None:
                        self.scene.addItem(square.z_wall)
        self.player_graphics_item = QtWidgets.QGraphicsEllipseItem(self.labyrinth.player_location[0]*self.square_size + self.square_size//4,self.get_yz_point(self.labyrinth.player_location[1],self.labyrinth.player_location[2])+ self.square_size//4,self.square_size/2,self.square_size/2,None) 

        brush_green = QtGui.QBrush(1)
        brush_green.setColor(QtGui.QColor(0,255,0))

        self.player_graphics_item.setBrush(brush_green)

        self.scene.addItem(self.player_graphics_item)



