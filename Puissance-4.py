def generDamier(dim):

    dim+=4
    L=[]
    for i in range(dim):
        dd=[]
        for j in range(dim):
            if i in [0,1,dim-2,dim-1] or j in [0,1,dim-2,dim-1]:
                dd.append("#")
            else:
                dd.append(" ")
        L.append(dd)
        
    return L

def display(L):
    for i in L:
        for j in i:
            print(j,end=" ")
        print()

def add(L, value,i,j):
    if L[i+2][j+2]==" ":
        L[i+2][j+2]=value
        print()
    else:
        print()
        print("errur case deja occup")
        print()

    #affiche(L)
        return True

    return False
if value==1 :
        L[i][j]="X"
if value==2 :
        L[i][j]="O"
L=generDamier(10)
'''add(L,"X",5,5)
add(L,"X",4,4)
add(L,"O",4,5)
add(L,"O",5,4)'''
L[4][4]=1
L[5][4]=2


for i in range (100):
    display(L)
    print(" ")
    i= int(input("En Quelle colonne  voulez vous  jouer ? "))
    j= int(input("En Quelle ligne voulez vous  jouer ? "))
    add(L,"X",i,j)


    display(L)
    print(" ")
    i= int(input("En Quelle colonne  voulez vous  jouer ? "))
    j= int(input("En Quelle ligne voulez vous  jouer ? "))
    add(L,"O",i,j)



