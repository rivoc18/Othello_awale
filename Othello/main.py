import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain

case=[3,2]
j=game.initialiseJeu()
game.affiche(j)
print('case',case)
print('liste entourage vide :',othello.entourageVide(j,case))
print('encadre:',othello.encadre(j,case[0],case[1],0,1))
print('liste encadrement',othello.encadrements(j,case,tous=True))
print('liste des coups valides:',game.getCoupsValides(j))
othello.joueCoup(j,case) 
game.affiche(j)
print('case',case)
print('liste entourage vide :',othello.entourageVide(j,case))
print('encadre:',othello.encadre(j,case[0],case[1],0,1))
print('liste encadrement',othello.encadrements(j,case,tous=True))
print('liste des coups valides:',game.getCoupsValides(j))




