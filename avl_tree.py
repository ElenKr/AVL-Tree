import random
from random import randint
import os
import time
max_visit=0
max_poso=0
max_day=0
week=6*[0]
cust_visit=[]
cust_poso=[]

def finding_max(node):
    global week
    global cust_visit
    global cust_poso
    global max_visit
    global max_poso
    temp1=0 #ποσα
    temp2=0 #επισκέψεις
    for i in range(0,6):
        temp1=temp1+node.values[i]
        temp2=temp2+node.day[i]
        week[i]+=node.day[i]    
    if temp1>max_poso:
        cust_poso=[]
        max_poso=temp1
        cust_poso.append(node.key)
    elif temp1==max_poso:
        cust_poso.append(node.key)
        
    if temp2>max_visit:
        cust_visit=[]
        max_visit=temp2
        cust_visit.append(node.key)
    elif temp2==max_visit:
        cust_visit.append(node.key)   

    
class Node():
    def __init__(self,key):
        self.key=key #card
        self.left=None #child
        self.right=None #child
        self.height=0   #height
        self.day=6*[0]     #visits
        self.values=6*[0]  #payment

    def __str__(self):
        return str(self.key)

class Avltree():
    

    def search(self,root,key): 
      
    # Base Cases: root is null or key is present at root 
        if root is None or root.key == key:
            
            return root 
  
    # Key is greater than root's key 
        if root.key < key: 
            return self.search(root.right,key) 
    
    # Key is smaller than root's key 
        return self.search(root.left,key) 
 
        
        
    def insert (self,root,key,values,day):
        if not root:
            node=Node(key)
            node.day=day
            node.values=values
            return node
        elif key < root.key:
            root.left = self.insert(root.left,key,values,day)
        elif key > root.key:
            root.right = self.insert(root.right,key,values,day)
            
        #μετα απο κάθε εισαγωγή ελέγχω την ισορροπία 
        root=self.rebalance(root)
        
        return root
    
    def getHeight(self,root):
        if not root: return -1
        return root.height
    
    def getBalance(self,root):
        if not root: return 0
        return self.getHeight(root.left)-self.getHeight(root.right)
        
    def rebalance(self,root):

        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
        balance=self.getBalance(root)

        if balance>1:

            if self.getBalance(root.left)<0:
                root.left=self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if balance<-1:
            if self.getBalance( root.right)>0:
                
                root.right=self.rightRotate(root.right)
            return self.leftRotate(root)
        return root


    def leftRotate(self,x):
        y=x.right
        B=y.left
        y.left=x
        x.right=B
        #update heights
        x.height=1+max(self.getHeight(x.left),self.getHeight(x.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
        #new root=y
        return y

    def rightRotate(self,x):
        
        y=x.left
        B=y.right
        #performrotation
        y.right=x
        x.left=B
        #updateheights
        x.height=1+max(self.getHeight(x.left),self.getHeight(x.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
        #newroot=y
        return y
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            finding_max(root)
            #print(root.key,root.values,root.day)
            self.inorder(root.right)
     
        
 

def card(root,tree):
    
    string='1234567890123456'
    random.seed(1059438)
    day=6*[0]
    values=6*[0]
    for j in range (0,1000000):
        day=6*[0]
        values=6*[0] 
        day=6*[0]
        values=6*[0]
        string='1234567890123456'
        for char in ['X','Y','Z','W']:
                        
            pos = randint(0, len(string) - 1)  # pick random position to insert char
            while string[pos].isdigit()==False:
                 pos = randint(0, len(string) - 1)
            string = "".join((string[:pos], char, string[pos+1:]))  # insert char at pos
        key=string
        
        #0->Δευτέρα
        #1->Τρίτη
        #2->Τετάρτη
        #3->Πέμπτη
        #4->Παρασκευή
        #5->Σάββατο
        
        poso=randint(10,100) #ποσό πληρωμής
        day1=randint(0,5) #ημέρα αγοράς
        day[day1]=1
        values[day1]=poso
        
       

        #ελέγχουμε εάν υπάρχει κόμβος με το ίδιο key
        node1=tree.search(root,key)
        #αν επιστρέφει none τότε δεν υπάρχει ίδιος πελάτης        
        if node1==None:
            root=tree.insert(root,key,values,day)
    
        else:
            
            for i in range(0,6):
               node1.values[i]+=values[i]
               node1.day[i]+=day[i]
      
       
    return root,tree

def hmera(i):
    if i==0:
        mera="Δευτέρα¨"
    elif i==1:
        mera="Τρίτη"
    elif i==2:
        mera="Τετάρτη"
    elif i==3:
        mera="Πέμπτη"
    elif i==4:
        mera="Παρασκευή"
    else:
        mera="Σάββατο" 
        
    return mera 


def main():
    tree=Avltree()
    root=None
    to=time.time()
    root,tree=card(root,tree)
    max_day=0
    max_d=0
    dayy=''
    #print("In Order Traversal")
    #to=time.time()   
    tree.inorder(root)
    print("ο/οι πελάτης/ες με το μεγαλύτερο ποσό πληρωμών :", cust_poso, "και πλήρωσαν:", max_poso)
    print("ο/οι πελάτης/ες με το μεγαλύτερο πλήθος επισκέψεων :", cust_visit, "και πήγαν:", max_visit)
    
    for i in range(0,6):
        if max_d<week[i]:
            max_d=week[i]
            max_day=i
            
    dayy=hmera(max_day)
    
    print("η ημέρα με τις περισσότερες επισκέψεις είναι:", dayy," με αριθμό επισκέψεων: ",max_d)    
    to=time.time()-to
    print("running time - avl tree",to)
if __name__=='__main__':    
    main()














    
        
