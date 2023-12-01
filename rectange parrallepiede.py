class Rectangle:
      
    def __init__(self, largeur, longueur):
        self._largeur = largeur
        self._longueur = longueur
        

    def largeur(self):
        return self._largeur

    def set_largeur(self, value):
        self._largeur = value

    def longueur(self):
        return self._longueur

    def set_longueur(self, value):
        self._longueur = value

    @classmethod
    def equals(cls,rect1, rect2):
        return rect1.largeur == rect2.largeur and rect1.longueur == rect2.longueur

    def perimetre(self):
        return 2 * (self.largeur + self.longueur)

    def surface(self):
        return self.largeur * self.longueur

    def __str__(self):
        return f"Rectangle(largeur={self.largeur}, longueur={self.longueur})"
    
    @classmethod
    def get_nbrRectangles(cls):
        return cls._nbrRectangles


class Parallelepipede(Rectangle):
     

    def __init__(self, largeur, longueur, hauteur):
        super().__init__(largeur, longueur)
        self._hauteur = hauteur
        

    def hauteur(self):
        return self._hauteur

    def hauteur(self, value):
        self._hauteur = value

    @classmethod
    def equals(cls, para1, para2):
        return super().equals(para1, para2) and para1.hauteur == para2.hauteur

    def surface(self):
        base_surface = super().surface()
        lateral_surface = 2 * (self.largeur * self.hauteur + self.longueur * self.hauteur)
        return base_surface + lateral_surface

    def volume(self):
        return super().surface() * self.hauteur

    def __str__(self):
        return f"Parallelepipede(largeur={self.largeur}, longueur={self.longueur}, hauteur={self.hauteur})"
    
    @classmethod
    def get_nbrParallelepipedes(cls):
        return cls._nbrParallelepipedes
E = Rectangle(3,5)
print(E.largeur,E.longueur.E.perimetre(),E.surface())
k = Parallelepipede(3,5,4)
print(k.longueur,k.largeur,k.hauteur,k.surface(),k.__str__())