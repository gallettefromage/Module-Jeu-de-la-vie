from termcolor import*
import time, random
class init:
    def __init__(self, grille_initial = False):
        
        self.génération_actuel = grille_initial
        self.mort, self.vivant = ".", "#"


    class grille_actuel:

        def afficher(self, largeur = True,bordure = 0, afficher = (colored("                                                           ", "blue", "on_green"))):
            print(afficher)
            if largeur == True:
                largeur = 1
            text = ""
            compteur = 0
            génération_à_écrire = []
            for y in self.génération_actuel:
                génération_à_écrire.append([])
                for x in y:
                    génération_à_écrire[compteur].append(colored(" " * bordure, "black", "on_cyan"))
                    génération_à_écrire[compteur].append(x.replace(".", colored(" "*largeur, "black", "on_black")).replace("#", colored(" "*largeur, "black", "on_white")))
                    génération_à_écrire[compteur].append(colored(" " * bordure, "black", "on_cyan"))
                compteur += 1

            for y in génération_à_écrire:
                for x in y:
                    text += x
                text += "\n"
            return text
        
        def avance_de_génération(self, nb_de_fois):
            for compteur in range(nb_de_fois):
                nouvelle_grille= []
                compteury = 0
                for y in self.génération_actuel:
                    nouvelle_ligne = ""
                    compteurx = 0
                    for x in y[0]:
                        mort_ou_vivant = 0
                        for i in range(-1,2):
                            try:
                                if self.génération_actuel[compteury-1][0][compteurx + i] == self.vivant:
                                    mort_ou_vivant +=1 
          
                            except:
                                pass
                        for i in range(-1,2):
                            try:
                                if self.génération_actuel[compteury+1][0][compteurx + i] == self.vivant:
                                    mort_ou_vivant +=1          
                            except:
                                pass
                        for i in range(-1, 2, 2):
                            try:
                                if y[0][compteurx+i] == self.vivant:
                                    mort_ou_vivant +=1                
                            except:
                                pass
                        if x == self.mort:
                            if mort_ou_vivant == 3:
                                nouvelle_ligne += self.vivant
                            else:
                                nouvelle_ligne += self.mort
                            
                        elif x == self.vivant:
                            if mort_ou_vivant == 2 or mort_ou_vivant == 3:
                                nouvelle_ligne += self.vivant
                            else:
                                nouvelle_ligne += self.mort
                        compteurx += 1
                    nouvelle_grille.append([nouvelle_ligne])
                    compteury += 1
                self.génération_actuel = nouvelle_grille
                        

        def timline(self, nb_de_fois, largeur = 1, bordure=0):
            print(colored("génération 0 :                                                         ", "blue", "on_red")) 
            print(self.grille_actuel.afficher(self, largeur))   
            for i in range(nb_de_fois):
                self.grille_actuel.avance_de_génération(self, 1)
                print(self.grille_actuel.afficher(self, largeur, bordure=bordure,afficher = (colored("génération "+str(i+1)+" :                                         ", "black", "on_red"))))     

        def simulation(self, nb_de_fois=1, délai = 5, largeur = 1, bordure=0, mode = 1):
            if mode == 1:
                print(self.grille_actuel.afficher(self, largeur, bordure=bordure, afficher=(colored("génération "+str(0)+" :                                         ", "black", "on_red"))))   
                time.sleep(délai*0.1)
                print("\033c")
                for i in range(nb_de_fois):
                    verif = self.génération_actuel
                    self.grille_actuel.avance_de_génération(self, 1)
                    if verif == self.génération_actuel:
                        break
                    print(self.grille_actuel.afficher(self, largeur, bordure=bordure, afficher = (colored("génération "+str(i+1)+" :                                         ", "black", "on_red"))))     
                    time.sleep(délai*0.1)
                    print("\033c")
                print(self.grille_actuel.afficher(self, largeur, bordure=bordure,afficher = (colored("génération "+str(i+1)+" :                                         ", "black", "on_red"))))     
            elif mode == 2:
                print(self.grille_actuel.afficher(self, largeur, bordure=bordure, afficher=(colored("génération "+str(0)+" :                                         ", "black", "on_red"))))   
                time.sleep(délai*0.1)
                print("\033c")
                a=1
                i=0
                stop = 0
                while a:
                    verif1 = self.génération_actuel
                    for g in range(2):
                        verif2 = self.génération_actuel
                        self.grille_actuel.avance_de_génération(self, 1)
                        if verif2 == self.génération_actuel:
                            stop = 1
                            break
                        print(self.grille_actuel.afficher(self, largeur, bordure=bordure, afficher = (colored("génération "+str(i+1)+" :                                         ", "black", "on_red"))))     
                        time.sleep(délai*0.1)
                        print("\033c")
                        i+=1
                    if stop == 1:
                        break
                    if verif1 == self.génération_actuel:
                        break
                print(self.grille_actuel.afficher(self, largeur, bordure=bordure,afficher = (colored("génération "+str(i+1)+" :                                         ", "black", "on_red"))))     
     
    class nouvelle_grille:
        def taille(self, largeur, hauteur):
            self.génération_actuel = []
            for y in range(hauteur):
                text = ""
                for x in range(largeur):
                    text += "."
                self.génération_actuel.append([text])
        
        def aléatoire(self, largeur, hauteur, aléa = 4):
            self.génération_actuel = []
            choix = []
            for i in range(aléa-1):
                choix.append(".")
            choix.append("#")
            for y in range(hauteur):
                text = ""
                for x in range(largeur):
                    text += random.choice(choix)
                self.génération_actuel.append([text])
    
    class ajouter_élément:
        def block(self, x, x2, y, y2):
            for compteury in range((y2-y)):
                for compteurx in range((x2-x)):
                    print(compteury)
                    print(compteurx)
                    self.génération_actuel[compteury][0][compteurx] = self.vivant