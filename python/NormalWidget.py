from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from NormalCursor import NormalCursor
import random
import time


class NormalWidget(QWidget):

    def __init__(self, file, rep):
        super().__init__()
        self.targets = []
        self.file = file
        self.list_temps = []
        self.rep = rep
        with open(self.file) as f:
            lines = f.readlines()

        for i in lines :
            
            x = int(i.split(',')[0])
            y = int(i.split(',')[1])
            size = int(i.split(',')[2])
            t = Target(x,y,size)

            self.targets.append(t)

        # self.aleatoire = random.choice(self.targets)
        # self.aleatoire.toSelect = True

        self.cpt = 0
        self.aleatoire = self.targets[self.cpt]
        self.aleatoire.toSelect = True


        self.rect = QRect(self.aleatoire.x,self.aleatoire.y,self.aleatoire.size,self.aleatoire.size)
        self.ellipse = QRegion(self.rect,QRegion.Ellipse)
        self.start = time.time()


        self.cursor = NormalCursor(self.targets)
        self.setMouseTracking(True)


    def paintEvent(self,qpaint):
        qpaint = QPainter(self)
        for i in self.targets:
            i.paint(qpaint)


        self.update()


    def mouseMoveEvent(self,event):
        cursorpos = event.pos()
        a = cursorpos.x()
        b = cursorpos.y()
        self.cursor.move(a,b)
        self.cursor.closest.toselect = False
        self.update()


    def mousePressEvent(self, event):
        
        
        if self.ellipse.contains(event.pos()):

            self.aleatoire.toSelect = False
            stop = time.time()
            temps_select = str(stop - self.start)[:4]
            self.list_temps.append(temps_select)
            
            # print("Temps de sélection : " + str(stop - self.start)[:4] + 's')
            
            # self.aleatoire = random.choice(self.targets)
            # self.aleatoire.toSelect = True

            self.aleatoire = self.targets[self.cpt]
            self.aleatoire.toSelect = True
            self.cpt += 1

            self.rect = QRect(self.aleatoire.x,self.aleatoire.y,self.aleatoire.size,self.aleatoire.size)
            self.ellipse = QRegion(self.rect,QRegion.Ellipse)
            self.start = time.time()

            self.rep -= 1
        
        if self.rep == 0 :
            self.close()


class Target :

    defaultCol = QColor("blue")
    highlightCol = QColor("red")
    toSelectCol = QColor("green")


    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.toSelect = False
        self.highlighted = False


    def paint(self, qpaint):
        
        if self.toSelect :
            qpaint.setBrush(Target.toSelectCol)

        elif self.highlighted :
            qpaint.setBrush(Target.highlightCol)

        else :
            qpaint.setBrush(Target.defaultCol)
            
        qpaint.drawEllipse(self.x,self.y,self.size,self.size)