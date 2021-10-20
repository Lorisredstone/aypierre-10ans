class element:
    def __init__(self, content, liste_categories):
        self.raw = content
        self.liste = content.split(",")
        self.liste_categories = liste_categories
        self.lien = self.liste[0]
        self.sujet = self.liste[1]
        self.description = self.liste[2]
        self.timestamp = self.liste[3]
        self.createur = self.liste[4]
        self.approuvé = self.liste[5]
class fichier:
    def __init__(self, nom):
        self.nom=nom
        self.contenu = open(nom, "r", encoding="UTF-8")
        self.contenu_liste = [x.split("\n")[0] for x in self.contenu.readlines()]
        self.liste_categories = self.contenu_liste[0].split(",")
        self.nombre_categories = len(self.liste_categories)
        self.classer()
    def print_liste(self):
        print(self.contenu_liste)
    def print_categories(self):
        print(self.liste_categories)
    def classer(self):
        self.classé = [element(self.contenu_liste[i], self.liste_categories) for i in range(1, len(self.contenu_liste))]

contenu = fichier("content.csv")
for element in contenu.classé:
    print(element.lien)