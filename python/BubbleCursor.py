from PyQt5.QtGui import *
from math import sqrt

class BubbleCursor :

    defaultCol = QColor("purple")

    def __init__(self,liste):
        self.x = 0
        self.y = 0
        self.size = 20
        self.targets = liste
        self.closest = self.targets[0]


    def paint(self, qpaint):
        qpaint.setBrush(BubbleCursor.defaultCol)
        distance = sqrt((self.closest.x-self.x)**2 + (self.closest.y-self.y)**2)-self.closest.size
        qpaint.drawEllipse(self.x-distance-5,self.y-distance-5,distance*2+self.closest.size+10,distance*2+self.closest.size+10)
        


    def move(self,a,b):
        self.x = a
        self.y = b
        d2 = 1000
        
        for i in self.targets :
            distance = sqrt((i.x-self.x)**2 + (i.y-self.y)**2)-i.size
            
            if distance < d2 :
                
                d2 = distance
                #self.closest.toSelect = False
                self.closest = i
                #self.closest.toSelect = True 