def Belt():
    b = []
    for i in range(10):
        b.append([])
    return b
belt = Belt()
def Inbelt(product = None):
        x = []
        if x == []:
            for i in range(11):
                if i == 0 and belt[0] == []:
                    belt[i].append(product)
                elif i != 0 and i < 10 and belt[i-1] != []and belt[i] == [] and belt[i-1] != [product]:
                    belt[i].append(product)
                elif i == 10 and belt[9] != []:
                    x.append(product)
        if x != []:
            print("Belt is full.Cannot Retrieve the product.")
def Outbelt():
    x = 0
    popproduct = []
    popproduct.append(belt[0])
    if belt[0] != []:
        belt.remove(belt[0])
        belt.append([])
        print("Retrieve a product with id",popproduct[0][0],"from the belt.")
        for i in belt:
            if i!=[]:
                x+=1
        print("The belt now has",x,"on the line.")
    elif belt[0] == []:
        print("The belt is empty.Cannot retrieve the product from the belt.")
class Warehouse:
    def __init__(self):
        self.row = []
    def WHname(self):
        return str(self)
    def addRow(self,rows=0,grid=0):
        y = grid*grid
        for i in range(rows):
            grids = []
            self.row.append(grids)
            for j in range(y):
                grids.append([])
    def storeProduct(self,rows=0,grid=0, product=None):
        if self.row[rows-1][grid] == []:
            self.row[rows-1][grid].append(product)
        else:
            print("Storing Successfully!")
    def retrieveProduct(self,rows=0,grid=0, product=None):
        if self.row[rows-1][grid] != []:
            self.row[rows-1][grid].remove(product)
        else:
            print("Slot is occupied. Cannot store the product.")
    def sort(self,rows=0,grid=0, product=None):
        self.remove(product)
        if self.row[rows-1][grid] == []:
            self.row[rows-1][grid].append(product)
            return True
        else:
            print("Slot is occupied. Cannot store the product.")
            return False
    def search(self,rows=0,grid=0, product=None):
        self.sort(product)
        if self.sort(product) == True:
            print("Found the product at Warehouse",self," rows",rows," slot",grid)
        else:
            print("Slot is occupied. Cannot store the product.")
    def summarize(self):
        x = 0
        for i in self.row:
            x+=1
            print(x,"-",i)
w1 = Warehouse()
w2 = Warehouse()
w3 = Warehouse()
w4 = Warehouse()
w5 = Warehouse()
w1.addRow(5,10)
w2.addRow(5,10)
w3.addRow(5,10)
w4.addRow(7,5)
w5.addRow(20,20)

class output:
    def show(self):
        WH = []
        for k in range(5):
            WH.append(k+1)
            x = 0
            y = 0
            wx = [w1.row,w2.row,w3.row,w4.row,w5.row]
            print("Warehouse ",WH[k])
            for i in wx[k]:
                x+=1
                for j in i:
                    if j == []:
                        y+=0
                    else:
                        y+=1
            print("Numbers of Rows: ",x)
            print("Numbers of total product: ",y)
            u = 0
            for i in wx[k]:
                u+=1
                v = ""
                for j in i:
                    if j == []:
                        y+=0
                    else:
                        y+=1
                        v += j[0] + " "
                if v == "":
                    v = "-"
                print("Product in row ",u,": id",v,)
            print("")


Eninput = ''
Atoy = []
for ic in range(ord('a'), ord('b')+1):
    Atoy.append(chr(ic).upper())

xtest = 0
for test in Atoy:
    for test2 in range(1, 21):
        for itest in range(00, 100):
            if itest in [0,1, 2, 3, 4, 5, 6, 7, 8, 9]:
                itest = str(xtest) + str(itest) 
            # Eninput = str(1) + str(test) + str(test2) + str(itest) #1A100
            Eninput =  test2, int(itest), str(1)+str(test)+str(test2)+str(itest)
            # w5.storeProduct(Eninput)
            # print 'sucsess'
            print Eninput
                

OP = output()
# w1.storeProduct(1,01,'1A100')
w1.summarize()
w2.summarize()
w3.summarize()
w4.summarize()
w5.summarize()







