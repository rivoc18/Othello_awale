import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain


j=game.initialiseJeu()
game.affiche(j)
print('adversaire affame:',awele.adversaireAffame(j))
print('liste coup :',awele.coups(j))
coup=[0,2]
nb=8;
print('coup:',coup,    'next case :',awele.nextcase(j,coup))
print('liste coup valide :',awele.listecoupValides(j))
awele.joueCoup(j,coup)
game.affiche(j)


