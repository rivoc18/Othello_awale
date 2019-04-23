# plateau: List[List[nat]]
# liste de listes (lignes du plateau) d'entiers correspondant aux contenus des cases du plateau de jeu

# coup: Pair[nat nat]
# Numero de ligne et numero de colonne de la case correspondante a un coup d'un joueur

# Jeu
# jeu:N-UPLET[plateau nat List[coup] List[coup] Pair[nat nat]]
# Structure de jeu comportant :
#           - le plateau de jeu
#           - Le joueur a qui c'est le tour de jouer (1 ou 2)
#           - La liste des coups possibles pour le joueur a qui c'est le tour de jouer
#           - La liste des coups joues jusqu'a present dans le jeu
#           - Une paire de scores correspondant au score du joueur 1 et du score du joueur 2

game=None #Contient le module du jeu specifique: awele ou othello
joueur1=None #Contient le module du joueur 1
joueur2=None #Contient le module du joueur 2


#Fonctions minimales 

def razCoupValide(jeu):
    jeu[2]=None

    

def getCopieJeu(jeu):
    """ jeu->jeu
        Retourne une copie du jeu passe en parametre
        Quand on copie un jeu on en calcule forcement les coups valides avant
    """
    ret=[]
    for i in range(0,len(jeu[0])):
        ret.append(jeu[0][i])
    return [ret,jeu[1],jeu[2],jeu[3],jeu[4]]
            
            

def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
        
    """
    if len(getCoupsJoues(jeu))>100:
        return True
    elif (getCoupsValides(jeu)==0):
        return True
    else:
        return False
def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
        On suppose que la fonction n'est appelee que si il y a au moins un coup valide possible
        et qu'elle retourne obligatoirement un coup valide
    """
    j=getJoueur(jeu)
    if j==1:
        j=joeueur1
    else:
        j=joueur2
    c=j.saisieCoup(getCopieJeu(jeu))
    while (not CoupValide(jeu,c)):
        print ('rejoué, votre coup n est pas valide')
        c=j.saisiecoup(getCopieJeu(jeu))
    return c

def joueCoup(jeu,coup):
    """jeu*coup->void
        Joue un coup a l'aide de la fonction joueCoup defini dans le module game
        Hypothese:le coup est valide
        Met tous les champs de jeu à jour (sauf coups valides qui est fixée à None)
    """
    
def initialiseJeu():
    """ void -> jeu
        Initialise le jeu (nouveau plateau, liste des coups joues vide, liste des coups valides None, et joueur = 1)
    """
    p=game.initPlateau()
    s=game.initScores()
    return [p,1,None,[],s]

def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    g=getScore(jeu)
    if (g[0]>g[1]):
        return 1
    elif (g[0]<g[1]):
        return 2
    else:
        return 0
    
   
    
def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer
                    
         Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """
    m=jeu[0]
    s=getCoupsJoues(jeu)
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    
    if (s==[]):
        print('aucun coup joué')
    else :
        p=len(s)-1
        print ('coup joue ='+str(s[p]))
        
    print('Scores='+str(getScores(jeu)))
    print('Plateau:')
    print('')
    k=0
    p=0
    c=0
    c2=0
    c3=0
    w=jeu[0][0]
    print('        |', end='')
    for o in w:
        print('   '+str(c3)+'    |', end='')
        c3=c3+1
    print('')
   
    for v in range (0,len(w)+2):
    
        print('--------', end='')
    print('')
        
    for i in m :
        for j in i:
            
            if p==0:
                print('   '+str(c2)+'    |', end='')
                p=p+1
                c2=c2+1
         
            print('   '+str(j)+'    |', end='')
            c=c+1	
        print('    ')
        k=1
        p=0
        w=0
        for r in range (0,len(i)+1):	
            print('---------', end='')
        print('')
    print('joueur',getJoueur(jeu),'a vous de jouer')

# Fonctions utiles

def getPlateau(jeu):
    """ jeu  -> plateau
        Retourne le plateau du jeu passe en parametre
        
    """
    return jeu[0]
def getCoupsJoues(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups joues dans le jeu passe en parametre
    """
    return jeu[3]
def getCoupsValides(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups valides dans le jeu passe en parametre
        Si None, alors on met à jour la liste des coups valides
    """
    if(jeu[2]==None):
        jeu[2]=game.listeCoupsValides(jeu)
    return jeu[2]
    
def getScores(jeu):
    """ jeu  -> Pair[nat nat]
        Retourne les scores du jeu passe en parametre
    """
    return jeu[4]
    
def getJoueur(jeu):
    """ jeu  -> nat
        Retourne le joueur a qui c'est le tour de jouer dans le jeu passe en parametre
    """
    return jeu[1]
    


def changeJoueur(jeu):
    """ jeu  -> void
        Change le joueur a qui c'est le tour de jouer dans le jeu passe en parametre (1 ou 2)
    """
    if (jeu[1]==1):
        jeu[1]=2
    else:
        jeu[1]=1
def getScore(jeu,joueur):
    """ jeu*nat->int
        Retourne le score du joueur
        Hypothese: le joueur est 1 ou 2
    """ 
    if(joueur==1):
        return jeu[4][0]
    else:
        return jeu[4][1]

def getCaseVal(jeu, ligne, colonne):
    """ jeu*nat*nat -> nat
        Retourne le contenu de la case ligne,colonne du jeu
        Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
    """
    
    return jeu[0][ligne][colonne]
    
def setCaseVal(jeu, ligne, colonne,nb):
    jeu[0][ligne][colonne]=nb




