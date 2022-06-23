from PyQt5.QtGui import *
from math import sqrt

class RopeCursor :

    defaultCol = QColor("purple")

    def __init__(self,liste):
        self.x = 0
        self.y = 0
        self.size = 20
        self.targets = liste
        self.closest = self.targets[0]


    def paint(self, qpaint):
        qpaint.setBrush(RopeCursor.defaultCol)
        qpaint.drawLine(self.x,self.y,self.closest.x+self.closest.size/2,self.closest.y+self.closest.size/2)
        


    def move(self,a,b):
        self.x = a
        self.y = b
        d2 = 1000
        
        for i in self.targets :
            distance = sqrt((i.x-self.x)**2 + (i.y-self.y)**2)-i.size
            
            if distance < d2 :
                
                d2 = distance
                self.closest = i
