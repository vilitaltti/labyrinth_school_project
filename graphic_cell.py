from PyQt5 import QtWidgets,QtCore,QtGui
import cell
"""
TODO: ota sisään tuloksi labyrintti luokka ja fiksaa yksi kerallaan seinät
"""

class GraphicCell():

    def __init__(self,x,y,square_size,cell):

        
        brush_grey = QtGui.QBrush(1)
        brush_grey.setColor(QtGui.QColor(211,211,211))

        brush_yellow = QtGui.QBrush(1)
        brush_yellow.setColor(QtGui.QColor(255,255,0))

        gray_pen = QtGui.QPen(1)
        gray_pen.setColor(QtGui.QColor(211,211,211))

        red_pen = QtGui.QPen(1)
        red_pen.setColor(QtGui.QColor(230,0,0))

        blue_pen = QtGui.QPen(1)
        blue_pen.setColor(QtGui.QColor(25,25,250))

        purple_pen = QtGui.QPen(1)
        purple_pen.setColor(QtGui.QColor(187,51,255))

        self.background = QtWidgets.QGraphicsRectItem(x,y,square_size,square_size,None)
        self.background.setPen(gray_pen)
        if cell.is_goal:
            self.background.setBrush(brush_yellow)
        else:
            self.background.setBrush(brush_grey)

        self.pos_x_wall = QtWidgets.QGraphicsLineItem(x+square_size,y,x+square_size,y+square_size)
        self.neg_x_wall = QtWidgets.QGraphicsLineItem(x,y,x,y+square_size)
        self.pos_y_wall = QtWidgets.QGraphicsLineItem(x,y+square_size,x+square_size,y+square_size)
        self.neg_y_wall = QtWidgets.QGraphicsLineItem(x,y,x+square_size,y)
        self.z_wall = None

        loc1 = cell.get_location()


        for i in cell.neighbours:
            z_dim = False
            loc2 = i.get_location()
            diffx = loc1[0]- loc2[0]
            diffy = loc1[1]- loc2[1]
            diffz = loc1[2]- loc2[2]
            if diffx == -1:
                self.pos_x_wall = None
            if diffx == 1:
                self.neg_x_wall = None
            if diffy == -1:
                self.pos_y_wall = None
            if diffy == 1:
                self.neg_y_wall = None
            if abs(diffz) == 1 and not z_dim:
                self.z_wall = QtWidgets.QGraphicsEllipseItem(x,y,square_size-1,square_size-1,None)
                z_dim = True
                if diffz < 0:
                    self.z_wall.setPen(red_pen)
                else:
                    self.z_wall.setPen(blue_pen)
            if abs(diffz) == 1 and z_dim:
                    self.z_wall.setPen(purple_pen)





        
