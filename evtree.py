from visual import *
import random

def treemaker(): #User interractive version of below
    L=[]
    n = int(input("How many animals do you want: "))
    for g in range(n):
        x=str(input("Name of Organism #"+str(g+1)+": "))
        if g==0:
            y=0
        else: y=int(input("Evolutionary Distance from " + L[0][0]+": "))
        if g==0:
            z=0
        else:
            z=int(input("Paralogs with " + L[g-1][0]+": "))
        L=L+[[x,y,z]]
        print ("Current List: " +str(L))
    return treeraw(L)

def treeraw(ListOfOrganismValues):
    #List is a list of lists [x,y,z]: [name, evolutionary distance from first,paralogs with last animal]
    L=ListOfOrganismValues #to make my life easier
    for x in L:
        if x[2]!=0:
            g= (5/x[2])
            x[2]=g        #for scaling
    for x in range(len(L)): #number or organisms
        if x>0:
            (oldname,oldy,oldz) = L[x-1]
        (name,y,z)=L[x] #extracting values
        (a,b,c)=(random.random(),random.random(),random.random()) #Random color generator
        organism = box(pos=(x,y,z), length=.5, height=.5, width=.5, color=(a,b,c), opacity=1) #creating the organism
        text(text=name,align='center', depth=-0.3, color=color.green, pos=(x,y+.6,z), height=.5, width=.5) #Adding name
        if x>0: #checking if it's the first
            (oldname,oldy,oldz) = L[x-1] 
            curve(pos=[(x-1,oldy,oldz), (x,y,z)], radius=0.05) #making the lines between the animals

#tree([["Horse",0,0],["Donkey",1,8],["Chicken",11,10],["Penguin",13, 15],["Snake",21,16]]) #our example
