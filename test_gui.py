from gui import GUI
import sys 
import time
import random
from labyrinth import Labyrinth
from PyQt5.QtWidgets import QApplication

random.seed(2)
global app
lab = Labyrinth(20,3,3)
lab.initialize_the_labyrinth()
#lab.import_labyrinth("testi.labyrinth")
print("goal:",lab.get_goal_location())
print("player:",lab.get_player_location())
app = QApplication(sys.argv)
a = GUI(lab,30)
sys.exit(app.exec_())
