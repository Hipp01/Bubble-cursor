from PyQt5.QtWidgets import QWidget, QInputDialog

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Expérience'
        self.num = ""
        self.technique = ""
        self.densites = 0
        self.taille = 0
        self.rep = 0
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.num = self.getNum()
        self.technique = self.getTechnique()
        self.densites = self.getDensite()
        self.taille = self.getTailles()
        self.rep = self.getRep()

        
    def getNum(self):
        i, okPressed = QInputDialog.getInt(self, "Expérience","Numéro d'utilisateur", 1, 0, 1000, 1)
        if okPressed:
            return i

        
    def getTechnique(self):
        items = ("Bubble","Rope","Normal")
        item, okPressed = QInputDialog.getItem(self, "Expérience","Technique :", items, 1, False)
        if okPressed and item:
            return item


    def getDensite(self):
        i, okPressed = QInputDialog.getInt(self, "Expérience","Densité", 30, 30, 90, 30)
        if okPressed:
            return i

    def getTailles(self):
        i, okPressed = QInputDialog.getInt(self, "Expérience","Tailles de cibles", 6, 6, 18, 6)
        if okPressed:
            return i

    def getRep(self):
        i, okPressed = QInputDialog.getInt(self, "Expérience","Répétitions", 1, 1, 50, 1)
        if okPressed:
            return i

