from random import *

class CreateCibles():

    def __init__(self, nb_cibles, taille_cibles, espacement):

        self.nb_cibles = int(nb_cibles)
        self.taille_cibles = int(taille_cibles)
        self.espacement = int(espacement)
        self.name = "cibles/"+str(self.nb_cibles) + "_cibles_de_taille_" + str(self.taille_cibles) + ".csv"

        self.main()

        
    def main(self):
        good = False
        while good == False :

            list_cibles = []
            xs = sample(range(0+self.taille_cibles+self.espacement,1000-self.taille_cibles-self.espacement), self.nb_cibles)
            ys = sample(range(0+self.taille_cibles+self.espacement,800-self.taille_cibles-self.espacement), self.nb_cibles)

            for i in range(self.nb_cibles):
                taille = self.taille_cibles
                list_cibles.append([xs[i],ys[i],taille])

            list_good = []
            for i in list_cibles :
                for j in list_cibles:
                    if i != j :
                        boucle = False
                        while boucle == False :

                            xi_plus = i[0] + i[2] + self.espacement//2
                            xi_moins = i[0] - i[2] + self.espacement//2
                            range_xi = range(xi_moins, xi_plus - 50 )
                            yi_plus = i[1] + i[2] + self.espacement//2
                            yi_moins = i[1] - i[2] + self.espacement//2
                            range_yi = range(yi_moins, yi_plus - 50 )


                            xj_plus = j[0] + j[2] + self.espacement//2
                            xj_moins = j[0] - j[2]+ self.espacement//2
                            range_xj = range(xj_moins, xj_plus - 50 )
                            yj_plus = j[1] + j[2] + self.espacement//2
                            yj_moins = j[1] - j[2] + self.espacement//2
                            range_yj = range(yj_moins, yj_plus - 50 )
                            

                            if ((xi_moins or xi_plus) in range_xj) or ((xj_moins or xj_plus) in range_xi) or ((yi_moins or yi_plus) in range_yj) or ((yj_moins or yj_plus) in range_yi) :
                                
                                i[0] = randint(self.taille_cibles+self.espacement,1000-self.taille_cibles-self.espacement)
                                i[1] = randint(self.taille_cibles+self.espacement,1000-self.taille_cibles-self.espacement)
                                list_good.append(False)

                            else :
                                boucle = True    
                                list_good.append(True)


            if not(False in list_good):
                good = True

        f = open(self.name, "w")
        for i in list_cibles:
            f.write(str(i[0])+','+str(+i[1])+','+str(i[2])+'\n')
        f.close()
            

class ordre_cible() :
    
    def __init__(self, name_file_cibles):

        self.name_file_cibles = name_file_cibles
        self.name = "ordre_pour_" + str(self.nb_cibles) + "_cibles_de_taille_" + str(self.taille_cibles) + ".csv"

        self.main()

    def main(self):
        with open(self.name_file_cibles) as f:
            lines = f.readlines()

        list_targets = []
        for i in lines :
            
            x = int(i.split(',')[0])
            y = int(i.split(',')[1])
            size = int(i.split(',')[2])
            t = [x,y,size]
            list_targets.append(t)

        ordre = []
        for i in range(len(list_targets)):
            choice = random.choice(list_targets)
            
            ordre.append(choice)

            list_targets.remove(choice)

        f = open(self.name, 'w')
        for i in ordre :
            f.write(str(i[0])+','+str(+i[1])+','+str(i[2])+'\n')
        
        f.close()



CreateCibles(30,6,15)
CreateCibles(60,6,10)
CreateCibles(90,6,5)

CreateCibles(30,12,15)
CreateCibles(60,12,5)
CreateCibles(90,12,0)

CreateCibles(30,18,10)
CreateCibles(60,18,0)
CreateCibles(90,18,0)