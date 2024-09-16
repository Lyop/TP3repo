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

'''A pile can be seen as a list on which access is restricted: 
elements can only be inserted at one end, called the top of the pile, 
you can only remove an element if it is at the top, and you can only see an element in the pile 
only if it's at the top. If you need to access an element that is not at the top, 
you have to remove the elements on top one by one, starting from the top.
In English, this type of structure is called LIFO: Last In, First Out. 
An analogy can be made with a pile of plates: you can only see the plate on top, you add a new plate from above, and you can only remove the plate on top. If you need to access the other plates, you have to remove the ones on top one by one.
The notion of pile is fundamental to computing and has many applications. 
For example
- Internet browsers, which use piles to store visited pages 
(the address of each new page visited is pileed, and when you click on “previous
or “back one page” to unpile it);
- post-fixed Polish notation;
- the “undo typing” function in word-processing programs: each new action is
then unpileed when the keystroke is cancelled;
- recursive functions
============================Exercise 1:Complete the code for the pile class
'''

class Pile(object):
    def __init__(self, lst):
        """
        Initialise la pile avec une liste.        
        :param lst: Liste des éléments qui seront convertis en pile.
        """
        self.pile = lst      
    
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
        retext = "Sommet\n"
        for val in range(len(self.pile)):
            retext = retext + "||" + str(self.pile[val]) + "||\n"
        retext = retext + "Bas"
        return retext
        
    
    def empiler(self, e):
        """
        Ajoute un élément au sommet de la pile.        
        :param e: Élément à empiler.
        """
        self.pile.insert(0, e)
       
    
    def depiler(self):
        """
        Retire l'élément au sommet de la pile et le retourne.        
        :return: L'élément qui était au sommet de la pile.
        """
        old = self.pile[0]

        del self.pile[0]
        return old
       
    
    def sommet(self):
        """
        Retourne l'élément au sommet de la pile sans le retirer.        
        :return: L'élément au sommet de la pile.
        """
        return self.pile[0]
        # pass

    def est_pile_vide(self):
        """
        Vérifie si la pile est vide.        
        :return: True si la pile est vide, False sinon.
        """
        if len(self.pile) == 0:
            return True
        else:
            return False
        # pass
    
    def hauteur(self):
        """
        Retourne le nombre d'éléments dans la pile.        
        :return: La hauteur de la pile.
        """
        hauteur = len(self.pile)
        return hauteur
        # pass
# __________________________________________________________________ STOP and Test the above 🛑 _______________________________________________
# ✔ Done

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

'''
Exercise 2- expressions
Using pile One approach to check balanced parentheses is to use pile. 
Each time, when an open parentheses is encountered push it in the pile, and when closed parenthesis is encountered, match it with the top of pile and pop it. 
If pile is empty at the end, return Balanced otherwise, Unbalanced. 
'''

def parenthesage(expr):
    # les fermants sont rangés dans le même ordre que les ouvrants
    ouv, fer =  ['(','[','('], [')',']', '}'] 
    pile = Pile([]) 

    for string in expr:
        if string in ouv:
            position = ouv.index(string)
            pile.empiler(fer[position])
        
        elif string in fer:
            if pile.est_pile_vide():
                print("There's an extra closing bracket")
                return False

            elif pile.sommet() == string:
                pile.depiler()

            else: 
                print("There's an open bracket without a closing one :(")
                return False
            
    if pile.est_pile_vide():
        print("The stack is empty: it's all good")
        return True
    else:
        print("There's an extra bracket/parenthesis")
        return True


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
    print('Bien Parenthésée? ', parenthesage("(())"))
    
    exp = ['3','42','13', '+', '*', '5','-']
    print(f"{exp} = {polonaise(exp)}")
       

    