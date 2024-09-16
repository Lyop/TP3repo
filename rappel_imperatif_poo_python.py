'''Une pile peut être vue comme une liste sur laquelle on a limité les accès : 
on ne peut insérer des éléments qu'à une seule extrémité, appelée le sommet de la pile, 
on ne peut retirer un élément que s'il est au sommet et on ne peut voir un élément de la pile 
que s'il est au sommet. Si on a besoin d'accéder à un élément qui n'est pas au sommet, 
on doit retirer un par un les éléments qui sont sur le dessus, en partant du sommet.
En anglais, ce type de structure est appelé LIFO : Last In, First Out. 
On peut faire une analogie avec une pile d'assiettes : on ne voit que l'assiette qui est au-dessus, on ajoute une nouvelle assiette par le dessus et on ne peut retirer que l'assiette du dessus. Si on a besoin d'accéder aux autres assiettes, il faut retirer une par une celles qui sont au-dessus.
La notion de pile est fondamentale en informatique et a de nombreuses applications. 
Mention-nons par exemple :
• les navigateurs Internet qui utilisent des piles pour le stockage des pages visitées 
(l'adresse de chaque nouvelle page visitée est empilée et quand on clique sur «précédente »
ou «reculer d'une page »on la dépile) ;
- la notation polonaise post-fixée ;
- la fonction «annuler la frappe» des traitements de texte :chaque nouvelle action est
empilée, puis dépilée lorsqu'on annule la frappe ;
- les fonctions récursives
============================Exercice 1:Compléter le code de la classe Pile
'''
class Pile(object):
    def __init__(self, lst):
        """
        Initialise la pile avec une liste.        
        :param lst: Liste des éléments qui seront convertis en pile.
        """
        pass        
    
    def __repr__(self):
        """
        Fournit une représentation en chaîne de la pile du sommet vers le bas.
        
        :return: Une chaîne de caractères représentant la pile avec les éléments 
        du sommet vers le bas. Par exemple pour afficher la pile 2,3,5:
        Sommet
        ||2||
        ||3||
        ||5||
         Bas        
        """
        pass
        
    
    def empiler(self, e):
        """
        Ajoute un élément au sommet de la pile.        
        :param e: Élément à empiler.
        """
        pass
       
    
    def depiler(self):
        """
        Retire l'élément au sommet de la pile et le retourne.        
        :return: L'élément qui était au sommet de la pile.
        """
        pass
       
    
    def sommet(self):
        """
        Retourne l'élément au sommet de la pile sans le retirer.        
        :return: L'élément au sommet de la pile.
        """
        pass

    def est_pile_vide(self):
        """
        Vérifie si la pile est vide.        
        :return: True si la pile est vide, False sinon.
        """
        pass
    
    def hauteur(self):
        """
        Retourne le nombre d'éléments dans la pile.        
        :return: La hauteur de la pile.
        """
        pass

'''
Exercice 2- Expressions bien parenthésées
On veut construire à l'aide d'une pile un vérificateur de parenthésage. 
Définir une fonction parenthesage, qui prend en argument une chaîne de caractères contenant
une expression parenthésée et la parcourt de gauche à droite de la façon suivante : 
lorsqu'on rencontre une parenthèse (ou accolade ou crochet) ouvrant(e) on empile la fermeture 
correspondante; lorsqu'on arrive sur une fermeture, lorsque c'est possible, on dépile et 
on compare le fermant trouvé et l'élément que l'on vient de dépiler.
La fonction renvoie True si l'expression est bien parenthésée, sinon False
Par exemple:
print('Bien Parenthésée? ', parenthage("(([{}])")) 
    affiche: False car Il y a un ouvrant de trop.
print('Bien Parenthésée? ', parenthage("(([{]}))"))
    affiche: False car Un fermant ferme un ouvrant qui ne lui correspond pas.
'''
def parenthesage(expr):
    # les fermants sont rangés dans le même ordre que les ouvrants
    ouv, fer =  ['(','[','('], [')',']', '}'] 
    pass

'''
Exrecice 3: Notation Polonaise
La notation polonaise, ou encore notation post-fixée, consiste à faire précéder les opérandes 
des opérateurs. Par exemple, au lieu d'écrire 42 + 13, en notation polonaise on écrit 42 13 +.
Un des avantages de cette notation est qu'elle rend inutile l'usage des parenthèses : 
pour 3 x (42 + 13) - 5,on note 3 42 13 + x 5 - et il n'y a aucune ambiguïté.
Dans cet exercice, on va définir une fonction polonaise qui prendra en argument une expression 
post-fixée sous la forme d'une liste de chaînes de caractères
(['3','42','13', '*', **', '5','-'] pour l'exemple précédent) et renverra le résultat de 
l'évaluation de cette expression. 
On lit les éléments de la liste un par un et on les empile sur une pile initialement vide. 
À chaque fois qu'on rencontre un opérateur, plutôt que de l'empiler, on l'applique aux deux 
derniers éléments de la pile et le résultat remplace ces deux derniers éléments.

1. Créer une fonction est_operateur qui prend une chaîne de caractères en argument et renvoie 
True si cete chaîne est '+', '*', '/' ou '-', False sinon.

2. Créer une fonction calcul qui prend en arguments des chaînes de caractères représentant 
un opérateur op et deux opérandes a et b et renvoie la valeur de a op b

3 En utilisant les deux fonctions précédentes, définir la fonction polonaise
'''
def est_operateur(c):
    '''fonction boolénne permettant de savoir si une chaîne de caractères est un opérateur'''
    pass

def calcul(op,a,b):
    pass

def polonaise(exp):
    pass

if __name__ == "__main__":
    
    pile = Pile([])
    print(pile)
    pile.empiler(-5)
    pile.empiler(-8)
    print(pile)
    print(f"Pile est vide? {pile.est_pile_vide()}")
    print(f"Hauteur de pile: {pile.hauteur()}")
    print(f"Sommet: {pile.depiler()}")
    
    print('Bien Parenthésée? ', parenthesage("(([{]}))"))
    
    exp = ['3','42','13', '+', '*', '5','-']
    print(f"{exp} = {polonaise(exp)}")
       

    
