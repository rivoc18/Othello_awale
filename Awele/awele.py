import sys
sys.path.append("..")
import game

def initPlateau():
    P1=[]
    for i in range (0,2):
        P2=[]
        for j in range (0,6):
            P2.append(4)
        P1.append(P2)
 
    P1[0]=[0,8,5,2,2,0]
    P1[1]=[0,0,0,0,0,0]
    
    return P1 
    
def initScores ():
    S=[0,0]
    return S
    
def adversaireAffame(jeu):
    j=game.getJoueur(jeu)
    c=0
    if j==1:
        m=jeu[0][1]
        for i in m:
            if i==0:
                c=c+1
        
    else:
        m=jeu[0][0]
        for i in m:
            if i==0:
                c=c+1
    if c==6:
        return True
    else:
        return False
    
def coups(jeu):
    c=0
    lc=[]
    j=game.getJoueur(jeu)
    if j==1:
        m=jeu[0][0]
        for i in m:
            lc2=[]
            
            if i!=0:
                lc2.append(0)
                lc2.append(c)
                lc.append(lc2)
                c=c+1
            else :
                c=c+1
                
    else:
        m=jeu[0][1]
        for i in m:
            lc2=[]
            if i!=0:
                lc2.append(0)
                lc2.append(i)
                lc.append(lc2)
            else :
                c=c+1
    return lc

def joueCoup(jeu,coup):
    
    v=game.getCaseVal(jeu,coup[0],coup[1])
    game.setCaseVal(jeu,coup[0],coup[1],0)
    distribue(jeu,coup,v)
    #game.addCoupJoue(jeu,coup)
    game.changeJoueur(jeu)
    game.razCoupValide(jeu)
    
def distribue(jeu,coup,nb):
    
    c=coup
    while(nb!=0):
        c=nextcase(jeu,c)
        if c!=coup:
            game.setCaseVal(jeu,c[0],c[1], game.getCaseVal(jeu,c[0],c[1])+1)
            nb=nb-1
    c=coup
    for i in range (0,6):
        c=i
        if game.getJoueur(jeu)==2:
            if (game.getCaseVal(jeu,0,c)==2 or game.getCaseVal(jeu,0,c)==3):
                game.setCaseVal(jeu,0,c,0)
    #mettre a jour le score 
        if game.getJoueur(jeu)==1:
            if (game.getCaseVal(jeu,1,c)==2 or game.getCaseVal(jeu,1,c)==3):
                game.setCaseVal(jeu,1,c,0)
        #mettre a jour le score        

def nextcase(jeu,coup):
    a=coup[0]
    b=coup[1]
    if coup[0]==0:
        if b!=0:
            x=[a,b-1]
            return x
        else:
            a=1
            b=0
            x=[a,b]
            return x
    if coup[0]==1:
        if b!=5:
            x=[a,b+1]
            return x
        else:
            a=0
            b=5
            x=[a,b]
            return x
    
    
    
    

def listecoupValides(jeu):
    a=adversaireAffame(jeu)
    cp=coups(jeu)
    if(not a):
        return cp
    v=[]
    for coup in cp:
        c=coup[1]          #coup[8,5,2,2]
        l=coup[0]
        g=game.getCaseVal(jeu,l,c)
        if l==0:
            if g>c:
                v.append(coup)
            else:
                if g>=(6-c):
                    v.append(coup)
    return v
