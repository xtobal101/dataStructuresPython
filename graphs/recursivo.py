class Node:
    def __init__(self, payload):
        self.payload =  payload
        self.child = None

    def __str__(self):
        return str(self.payload)

def recursivo(root):
    

    if root == None:

        #print("last recursive") 
        return -5  #This is the exit condition"
    else:
        #print("cycle")
        #print(root)
        return 10 + (recursivo(root.child))


a = Node("Hola")
ab = Node("Tio")
b = Node("Cris")
c = Node("???")
d = Node("ha")
e = Node("llovido")

a.child = ab
ab.child = b
b.child = c
c.child = d
d.child = e


print(recursivo(a))


                    
