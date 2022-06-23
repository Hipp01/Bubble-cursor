import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import BubbleWidget
import NormalWidget
from ExpSetup import App
import random
from os.path import exists


class XPManager() : 
    
    def __init__(self):
        app = QApplication(sys.argv)
        ex = App()

        self.numero = ex.num
        self.technique = ex.technique
        self.densite = ex.densites
        self.taille = ex.taille
        self.repetition = ex.rep
        self.app = app

        self.ordre = self.ordre_densite_taille()
        self.techniques = self.differentes_techniques()
        
        for j in range(len(self.techniques)+1):
            self.moyenne_technique = 0
            
            for i in range(len(self.ordre)+1):
                moyenne = self.experience()
                self.moyenne_technique += moyenne
                self.analyse_moyenne(moyenne)
                
                if i != len(self.ordre):
                    self.taille = self.ordre[i][1]
                    self.densite = self.ordre[i][0]
            
            self.score_total()

            if j != len(self.techniques):
                self.technique = self.techniques[j]



    def ordre_densite_taille(self):

        liste_td = [[30,6],[30,12],[30,18],[60,6],[60,12],[60,18],[90,6],[90,12],[90,18]]
        random.shuffle(liste_td)
        liste_td.remove([self.densite,self.taille])
        
        return liste_td


    def differentes_techniques(self):

        techniques = ["Bubble", "Rope", "Normal"]
        techniques.remove(self.technique)
        return techniques 

    
    def experience(self):

        name_file = "../cibles/"+ str(self.densite)+ "_cibles_de_taille_" + str(self.taille) + ".csv"

        if self.technique == 'Bubble' :
            cibles = BubbleWidget.BubbleWidget('bubble', name_file, self.repetition + 1)
        
        elif self.technique == 'Rope':
            cibles = BubbleWidget.BubbleWidget('rope', name_file, self.repetition + 1)

        else :
            cibles = NormalWidget.NormalWidget(name_file, self.repetition + 1)

        cibles.resize(1034,800)

        
        cibles.show()
        self.app.exec_()

        div = self.repetition
        res = 0
        for i in cibles.list_temps :
            res += float(i)

        moyenne = res/div

        return moyenne
        
    
    def analyse_moyenne(self, moyenne):
        name = "user_"+str(self.numero)+".txt"
        file = "../resultat/"+name
        

        if exists(file) :
            with open(file) as f:
                lines = f.read()
        else :
            lines = ""


        f = open(file, "a")
        if not(str(self.technique) in lines) :
            f.write(str(self.technique)+'\n\n')

        f.write(str(self.densite)+" cibles , "+str(self.taille)+" pixels :\n")
        f.write("   - "+str(moyenne)+" secondes\n\n")

        f.close()


    def score_total(self):
        name = "user_"+str(self.numero)+".txt"
        file = "../resultat/"+name
        f = open(file, "a")
        f.write('\n\n')
        f.write('Temps total pour '+str(self.technique)+' : '+str(self.moyenne_technique)+' secondes'+'\n\n\n')
        f.close()




if __name__ == "__main__":
	XPManager()
