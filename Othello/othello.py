import sys
sys.path.append("..")
import game

def initPlateau():
    
    P1=[]
    for i in range (0,8):
        P2=[]
        for j in range (0,8):
            P2.append(0)
        P1.append(P2)
 
    P1[3][3]=2
    P1[3][4]=2
    P1[4][3]=1
    P1[4][4]=1
    P1[2][3]=2
    P1[1][4]=1
    P1[2][2]=2
    P1[1][2]=1
    
    P1[3][5]=2
    P1[3][2]=0
    P1[3][6]=1
    
    return P1
def initScores ():
    S=[0,0]
    return S

def listeCoupsValides(jeu):
    cp=coups(jeu)
    return [x for x in cp if len(encadrements(jeu,x,False))>0]
    
def coups(jeu):
    j=game.getJoueur(jeu)
    j=(j%2)+1
    s={ str(x) for l in range (0,8) for c in range (0,8) for x in entourageVide(jeu,[l,c]) if game.getCaseVal(jeu,l,c)==j }
      
    return [eval (x) for x in s]
    
def entourageVide(jeu,coup):
    ret=[]
    l=coup[0]
    c=coup[1]
    if(l>0):
        if (game.getCaseVal(jeu,l-1,c)==0):
            ret.append([l-1,c])
        if(c>0):
            if(game.getCaseVal(jeu,l-1,c-1)==0):
                ret.append([l-1,c-1])
        if(c<7):
            if (game.getCaseVal(jeu,l-1,c+1)==0):
                ret.append([l-1,c+1])
    if (l<7):
        if(game.getCaseVal(jeu,l+1,c)==0):
            ret.append([l+1,c])
        if(c>0):
            if(game.getCaseVal(jeu,l+1,c-1)==0):
                ret.append([l+1,c-1])
        if(c<7):
            if(game.getCaseVal(jeu,l+1,c+1)==0):
                ret.append([l+1,c+1])
    if (c>0):
        if(game.getCaseVal(jeu,l,c-1)==0):
            ret.append([l,c-1])
    if (c<7):
        if(game.getCaseVal(jeu,l,c+1)==0):
            ret.append([l,c+1])
    return ret
        
def encadrements(jeu,case,tous=True):
    ret=[]
    for l in [-1,0,1]:
        for c in [-1,0,1]:
            if(not((l==0)and(c==0))):
                if encadre(jeu,case[0],case[1],l,c):
                    ret.append([l,c])
                    if (not tous):
                        return ret
    return ret
    
def encadre(jeu,l,c,ml,mc):
    i=0
    j=game.getJoueur(jeu)
    while True:
        l+=ml
        c+=mc
        if(l>7)or(l<0)or(c>7)or(c<0):
            return False
        v=game.getCaseVal(jeu,l,c)
        if (v==j):
            if(i==0):
                return False
            else:
                return True
        if(v==0):
            return False
        i+=1
    return False
    
def joueCoup(jeu,coup):
    game.getCoupsJoues(jeu).append(coup)
    j=game.getJoueur(jeu)
    s=game.getScores(jeu)
    e=encadrements(jeu,coup,True)
    slv=(j%2)+1
    for d in e:
        l=coup[0]
        c=coup[1]
        while True:
            lt=d[0]
            ct=d[1]
            if (game.getCaseVal(jeu,l,c)==j):
                break
            game.setCaseVal(jeu,l,c,j)
            s[j-1]+=1
            s[slv-1]-=1
    distribue(jeu,coup,encadrements(jeu,coup,tous=True))
    game.changeJoueur(jeu)
    game.razCoupValide(jeu)
    
def distribue(jeu,coup,direction):
    j=game.getJoueur(jeu)
    for d in direction:
        l=coup[0]
        c=coup[1]
        coupss=0
        while (coupss!=j):
            
            l=l+d[0]
            c=c+d[1]
            coupss=game.getCaseVal(jeu,l,c)
            game.setCaseVal(jeu,l,c,j)
        


            

        
        
                
