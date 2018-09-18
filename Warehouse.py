import string
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
            return False
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

class ProductID:
    def __init__(self):
        self.pdid = []
        self.WH = []
        self.RW = []
        self.SL =[]
        self.productName = []
        self.CM = []
    def addID(self,ID = None):
        self.pdid.append(ID)
    def findWH(self):
        if self.pdid[0][1] in string.ascii_uppercase[:20]:
            self.productName.append(self.pdid[0][1:5])
            self.WH.append(5)
        elif self.pdid[0][1] in string.ascii_uppercase[20]:
            if int(self.pdid[0][2:5]) < 360:
                self.productName.append(self.pdid[0][1:5])
                self.WH.append(5)
            else:
                self.productName.append(self.pdid[0][1:5])
                self.WH.append(1)
        elif self.pdid[0][1] in string.ascii_uppercase[21]:
            if int(self.pdid[0][2:5]) < 472 or int(self.pdid[0][2:5]) > 486:
                self.productName.append(self.pdid[0][1:5])
                self.WH.append(1)
            elif int(self.pdid[0][2:5]) >= 472 and int(self.pdid[0][2:5]) < 487:
                self.productName.append(self.pdid[0][1:5])
                self.WH.append(2)
        elif self.pdid[0][1] in string.ascii_uppercase[22]:
                self.productName.append(self.pdid[0][1:5])
                self.WH.append(2)
        elif self.pdid[0][1] in string.ascii_uppercase[23]:
            if int(self.pdid[0][2:5]) < 198:
                self.productName.append(self.pdid[0][1:5])
                self.WH.append(2)
            else:
                self.productName.append(self.pdid[0][1:5])
                self.WH.append(3)
        elif self.pdid[0][1] in string.ascii_uppercase[24]:
            if int(self.pdid[0][2:5]) < 311:
                self.productName.append(self.pdid[0][1:5])
                self.WH.append(3)
            else:
                self.productName.append(self.pdid[0][1:5])
                self.WH.append(4)
    def findRW(self):
        for i in range(25):
            if i < 20:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    self.RW.append(i+1)
            elif i == 20:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) < 360:
                        for n in range(20):
                            if int(self.pdid[0][2:5]) >= 100 +(12*(n))+ n and int(self.pdid[0][2:5]) < 100 +(12*(n+1))+n+1:
                                self.RW.append(n+1)
                    if int(self.pdid[0][2:5]) >= 360 and int(self.pdid[0][2:5]) < 487:
                        for n in range(2):
                            if int(self.pdid[0][2:5]) >= 360 + (100*n)+n and int(self.pdid[0][2:5]) < 360 + (100*(n+1))+n+1:
                                self.RW.append(n+1)
                    if int(self.pdid[0][2:5]) > 486 and int(self.pdid[0][2:5]) < 600:
                        for n in range(2):
                            if int(self.pdid[0][2:5]) >= 487 + (100*n) and int(self.pdid[0][2:5]) < 487 + (100*(n+1))+n:
                                self.RW.append(n+1)
            elif i == 21:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 173:
                        for n in range(3):
                            if int(self.pdid[0][2:5]) >= 100 + (73*n)+n and int(self.pdid[0][2:5]) < 100 + (72*(n+1))+n+1:
                                self.RW.append(n+2)
                    if int(self.pdid[0][2:5]) >= 173 and int(self.pdid[0][2:5]) < 473:
                        for n in range(3):
                            if int(self.pdid[0][2:5]) >= 173 + (100*n)+n and int(self.pdid[0][2:5]) < 173 + (100*(n+1))+n+1:
                                self.RW.append(n+3)
                    if int(self.pdid[0][2:5]) >= 473 and int(self.pdid[0][2:5]) < 487:
                        self.RW.append(1)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        for n in range(2):
                            if int(self.pdid[0][2:5]) >= 487 + (72*n)+n and int(self.pdid[0][2:5]) < 487 + (72*(n+1))+n+1:
                                self.RW.append(n+2)
            elif i == 22:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 186:
                            self.RW.append(1)
                    if int(self.pdid[0][2:5]) >= 186 and int(self.pdid[0][2:5]) < 487:
                        for n in range(4):
                            if int(self.pdid[0][2:5]) >= 186 + (99*n)+n and int(self.pdid[0][2:5]) < 186 + (99*(n+1))+n+1:
                                self.RW.append(n+2)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        for n in range(2):
                            if int(self.pdid[0][2:5]) >= 487 + (85*n)+n and int(self.pdid[0][2:5]) < 487 + (85*(n+1))+n+1:
                                self.RW.append(n+1)
            elif i == 23:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 199:
                            self.RW.append(5)
                    if int(self.pdid[0][2:5]) >= 199 and int(self.pdid[0][2:5]) < 487:
                        for n in range(3):
                            if int(self.pdid[0][2:5]) >= 199 + (100*n)+n and int(self.pdid[0][2:5]) < 199 + (100*(n+1))+n+1:
                                self.RW.append(n+1)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        for n in range(2):
                            if int(self.pdid[0][2:5]) >= 487 + (99*n)+n and int(self.pdid[0][2:5]) < 487 + (99*(n+1))+n+1:
                                self.RW.append(n+1)
            elif i == 24:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 112:
                            self.RW.append(3)
                    if int(self.pdid[0][2:5]) >= 112 and int(self.pdid[0][2:5]) < 312:
                        for n in range(3):
                            if int(self.pdid[0][2:5]) >= 112 + (99*n)+n and int(self.pdid[0][2:5]) < 112 + (99*(n+1))+n+1:
                                self.RW.append(n+4)
                    if int(self.pdid[0][2:5]) >= 312 and int(self.pdid[0][2:5]) < 487:
                        for n in range(7):
                            if int(self.pdid[0][2:5]) >= 312 + (24*n)+n and int(self.pdid[0][2:5]) < 312 + (24*(n+1))+n+1:
                                self.RW.append(n+1)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        for n in range(7):
                            if int(self.pdid[0][2:5]) >= 487 + (25*n)+n and int(self.pdid[0][2:5]) < 487 + (25*(n+1))+n+1:
                                self.RW.append(n+1)
    def findSL(self):
        for i in range(25):
            if i < 20:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 487:
                        x = int(self.pdid[0][2:5])-100
                        self.SL.append(x)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        x = int(self.pdid[0][2:5])-487
                        self.SL.append(x)
            elif i == 20:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) < 113:
                        x = int(self.pdid[0][2:5])-100 +387
                        self.SL.append(x)
                    elif int(self.pdid[0][2:5]) >= 113 and int(self.pdid[0][2:5]) < 360:
                        x = int(self.pdid[0][2:5])-100
                        if x % 13 == 0:
                            y = 387
                            self.SL.append(y)
                        else:
                            x1 = int(x/13)
                            x2 = 13*x1
                            y = x - x2 + 387
                            self.SL.append(y)
                    elif int(self.pdid[0][2:5]) >= 360 and int(self.pdid[0][2:5]) < 487:
                        x = int(self.pdid[0][2:5])-360
                        if x <100:
                            self.SL.append(x)
                        else:
                            self.SL.append(x-100)
                    elif int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 587:
                        x = int(self.pdid[0][2:5])-487
                        self.SL.append(x)
                    elif int(self.pdid[0][2:5]) >= 587 and int(self.pdid[0][2:5]) < 600:
                        x = int(self.pdid[0][2:5])-587
                        self.SL.append(x)
            elif i == 21:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 473:
                        x1 = int(self.pdid[0][2:5])-100
                        if x1 + 27 <100:
                            self.SL.append(x1+27)
                        else:
                            x = x1-73
                            if x > 100:
                                x2 = int(x/100)
                                x3 = x2*100
                                x4 = x-x3
                                self.SL.append(x4)
                            else:
                                self.SL.append(x)
                    if int(self.pdid[0][2:5]) >= 473 and int(self.pdid[0][2:5]) < 487:
                        x = int(self.pdid[0][2:5])-473
                        self.SL.append(x)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        x = int(self.pdid[0][2:5])-460
                        if x < 100:
                            self.SL.append(x)
                        else:
                            self.SL.append(x-100)
            elif i == 22:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 487:
                        x = int(self.pdid[0][2:5])-100
                        if x <100:
                            self.SL.append(x+14)
                        else:
                            x1 = int(x/100)
                            x2 = x1*100
                            x3 = x-x2
                            if x3 +14 <100:
                                self.SL.append(x3+14)
                            if x3 +14>99:
                                self.SL.append(x3+14-100)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        x = int(self.pdid[0][2:5])-487+14
                        if x <100:
                            self.SL.append(x)
                        else:
                            self.SL.append(x-100)
            elif i == 23:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 199:
                        x = int(self.pdid[0][2:5])-100+1
                        self.SL.append(x)
                    if int(self.pdid[0][2:5]) >= 199 and int(self.pdid[0][2:5]) < 487:
                        x = int(self.pdid[0][2:5])-199
                        if x<100:
                            self.SL.append(x)
                        else:
                            x1 = int(x/100)
                            x2 = x1*100
                            x3 = x-x2
                            self.SL.append(x3)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        x = int(self.pdid[0][2:5])-487
                        if x<100:
                            self.SL.append(x)
                        else:
                            x1 = int(x/100)
                            x2 = x1*100
                            x3 = x-x2
                            self.SL.append(x3)
            elif i == 24:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 312:
                        x = int(self.pdid[0][2:5])-100+88
                        if x<100:
                            self.SL.append(x)
                        else:
                            x1 = int(x/100)
                            x2 = x1*100
                            x3 = x-x2
                            self.SL.append(x3)
                    if int(self.pdid[0][2:5]) >= 312 and int(self.pdid[0][2:5]) < 486:
                        x = int(self.pdid[0][2:5])-312
                        if x<25:
                            self.SL.append(x)
                        else:
                            x1 = int(x/25)
                            x2 = x1*25
                            x3 = x-x2
                            self.SL.append(x3)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        x = int(self.pdid[0][2:5])-487
                        if x<25:
                            self.SL.append(x)
                        else:
                            x1 = int(x/25)
                            x2 = x1*25
                            x3 = x-x2
                            self.SL.append(x3)
p = ProductID()
class Warehouse:
    def __init__(self):
        self.row = []
        self.manuallyY = []
        self.manuallyX = []
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
            print("Moving from Belt to Warehouse 1")
        else:
            print("Slot is occupied. Cannot store the product.")
    def retrieveProduct(self,rows=0,grid=0, product=None):
        if self.row[rows-1][grid] != []:
            self.row[rows-1][grid].remove(product)
            Inbelt(product)
            if Inbelt(product) == False:
                self.row[rows-1][grid].append(product)
            return True
        else:
            print("Slot is empty. Cannot retrieve the product.")
    #def sort(self,rows=0):
        #self.remove(product)
        #if self.row[rows-1][grid] == []:
            #self.row[rows-1][grid].append(product)
            #return True
        #else:
            #print("Cannot sort the product")
            #return False
    #def search(self,rows=0,grid=0, product=None):
        #self.sort(product)
        #if self.sort(product) == True:
            #print("Found the product at Warehouse",self," rows",rows," slot",grid)
        #else:
            #print("Product not found")
    def manually_put(self):
        i = enter.command
        self.manuallyX.append(i[1:5])
        self.manuallyY.append(i[5:9])
        print(self.manuallyY)
        print(self.manuallyX)
    def summarize(self):
        x = 0
        for i in self.row:
            x+=1
            print(x,"-",i)
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
class Userinput:
    def __init__(self):
        self.command = ""
    def userCommand(self):
        i = input("Enter Your Command :")
        self.command = i
    def checkid(self):
        i = self.command
        if len(i) ==5:
            if i[0].isdigit() == True:
                if int(i[0]) <= 1 or int(i[0]) == 5:
                    if i[1].isupper() == True and i[1] != "Z":
                        if i[2].isdigit() == True and int(i[2])<=5 and int(i[2]) != 0:
                            if i[3:5].isdigit() == True and int(i[3:5]) <= 99:
                                return True
                elif int(i[0]) == 2:
                    if int(i[1]) <= 5:
                        if i[2].isdigit() == True and int(i[2]) <=9 and int(i[2]) != 0:
                            if i[3:5].isdigit() == True and int(i[3:5]) == 0:
                                return True
                elif int(i[0]) == 3 or int(i[0]) == 4:
                    if int(i[1:5]) == 0:
                        return True
        elif len(i) ==6:
            if i[0].isdigit() == True:
                if int(i[0]) == 2:
                    if int(i[1]) <= 5 and int(i[1]) != 0:
                        if i[2:3].isdigit() == True and int(i[2:3]) <=20 and int(i[2:3]) != 0:
                            if i[4:5].isdigit() == True and int(i[3:5]) == 0:
                                return True
        elif len(i) ==9:
            if i[0].isdigit() == True:
                if int(i[0]) == 9:
                    if i[1].isupper() == True and i[1] != "Z":
                        if i[2].isdigit() == True and int(i[2])<=5 and int(i[2]) != 0:
                            if i[3:5].isdigit() == True and int(i[3:5]) <= 99:
                                if i[5].isupper() == True and i[5] != "Z":
                                    if i[6].isdigit() == True and int(i[6])<=5 and int(i[6]) != 0:
                                        if i[6:8].isdigit() == True and int(i[6:8]) <= 99:
                                            return True

        return False
    def outputcheckid(self):
        opc = self.checkid()
        if opc == False:
            print("Product ID ERROR")
        if opc == True:
            self.readcommand()
            self.readid()
            r.run()
            if p.CM[0] == "Retrieve belt" or p.CM[0] == "Output":
                p.pdid.pop()
                p.CM.pop()
            elif p.CM[0] == "Sort":
                p.pdid.pop()
                p.CM.pop()
                #p.WH.pop()
                #p.RW.pop()
            else:
                p.pdid.pop()
                p.productName.pop()
                p.WH.pop()
                p.RW.pop()
                p.SL.pop()
                p.CM.pop()
    def readcommand(self):
        i = self.command
        if i[0] == "0":
            p.CM.append("Retrieve")
        if i[0] == "1":
            p.CM.append("Store")
        if i[0] == "2":
            p.CM.append("Sort")
        if i[0] == "3":
            p.CM.append("Retrieve belt")
        if i[0] == "4":
            p.CM.append("Output")
        if i[0] == "5":
            p.CM.append("Search")
        if i[0] == "9":
            p.CM.append("Manually Put")
    def readid(self):
        i = self.command
        p.addID(i)
        p.findWH()
        p.findRW()
        p.findSL()
class RunSoftware:
    def run(self):
        a = p.CM
        c = p.WH
        All = [w1,w2,w3,w4,w5]
        if a[0] == "Retrieve":
            for i in range(len(All)):
                if i == c[0]-1:
                    if bool(All[i].retrieveProduct(p.RW[0],p.SL[0],p.productName[0])) == True:
                        x = [1,2,1]
                        y4 = [2,4,2]
                        y5 = [2,5,2]
                        if i+1 == 1:
                            print("Getting a product id",p.productName[0],"in warehouse",i+1,": row",p.RW[0],"slot",p.SL[0])
                            print("Moving from Warehouse 1 to Start")
                            print("Place product id",p.productName[0],"on the belt","\nRetrieving Successfully!")
                        elif i+1 == 2:
                            print("Moving from Warehouse %d to Warehouse %d" % (x[0], y4[0]))
                            print("Getting a product id",p.productName[0],"in warehouse",i+1,": row",p.RW[0],"slot",p.SL[0])
                            print("Moving from Warehouse %d to Warehouse %d" % (y4[0], x[0]))
                            print("Moving from Warehouse 1 to Start")
                            print("Place product id",p.productName[0],"on the belt","\nRetrieving Successfully!")
                        elif i+1 == 3:
                            print("Moving from Warehouse 1 to Warehouse 3")
                            print("Getting a product id",p.productName[0],"in warehouse",i+1,": row",p.RW[0],"slot",p.SL[0])
                            print("Moving from Warehouse 3 to Warehouse 1")
                            print("Moving from Warehouse 1 to Start")
                            print("Place product id",p.productName[0],"on the belt","\nRetrieving Successfully!")
                        elif i+1 == 5 or i+1 == 4:
                            for j in range(2):
                                if i+1 == 5:
                                    print("Moving from Warehouse %d to Warehouse %d" % (x[j], y5[j]))
                                elif i+1 == 4:
                                    print("Moving from Warehouse %d to Warehouse %d" % (x[j], y4[j]))
                                    print("Getting a product id",p.productName[0],"in warehouse",i+1,": row",p.RW[0],"slot",p.SL[0])
                            for j in range(2):
                                if i+1 == 5:
                                    print("Moving from Warehouse %d to Warehouse %d" % (y5[j+1], x[j+1]))
                                elif i+1 == 4:
                                    print("Moving from Warehouse %d to Warehouse %d" % (y4[j+1], x[j+1]))
                            print("Moving from Warehouse 1 to Start")
                            print("Place product id",p.productName[0],"on the belt","\nRetrieving Successfully!")
        elif a[0] == "Store":
            for i in range(len(All)):
                if i == c[0]-1:
                    All[i].storeProduct(p.RW[0],p.SL[0],p.productName[0])
                    x = [1,2,1]
                    y4 = [2,4,2]
                    y5 = [2,5,2]
                    if i+1 == 1:
                        print("Storing a product id",p.productName[0],"in warehouse",i+1,": row",p.RW[0],"slot",p.SL[0])
                        print("Moving from Warehouse 1 to Start","\nStoring Successfully!")
                    elif i+1 == 2:
                        print("Moving from Warehouse %d to Warehouse %d" % (x[0], y4[0]))
                        print("Storing a product id",p.productName[0],"in warehouse",i+1,": row",p.RW[0],"slot",p.SL[0])
                        print("Moving from Warehouse %d to Warehouse %d" % (y4[0], x[0]))
                        print("Moving from Warehouse 1 to Start","\nStoring Successfully!")
                    elif i+1 == 3:
                        print("Moving from Warehouse 1 to Warehouse 3")
                        print("Storing a product id",p.productName[0],"in warehouse",i+1,": row",p.RW[0],"slot",p.SL[0])
                        print("Moving from Warehouse 3 to Warehouse 1")
                        print("Moving from Warehouse 1 to Start","\nStoring Successfully!")
                    elif i+1 == 5 or i+1 == 4:
                        for j in range(2):
                            if i+1 == 5:
                                print("Moving from Warehouse %d to Warehouse %d" % (x[j], y5[j]))
                            elif i+1 == 4:
                                print("Moving from Warehouse %d to Warehouse %d" % (x[j], y4[j]))
                                print("Storing a product id",p.productName[0],"in warehouse",i+1,": row",p.RW[0],"slot",p.SL[0])
                        for j in range(2):
                            if i+1 == 5:
                                print("Moving from Warehouse %d to Warehouse %d" % (y5[j+1], x[j+1]))
                            elif i+1 == 4:
                                print("Moving from Warehouse %d to Warehouse %d" % (y4[j+1], x[j+1]))
                        print("Moving from Warehouse 1 to Start","\nStoring Successfully!")
        elif a[0] == "Retrieve belt":
            Outbelt()
        elif a[0] == "Output":
            OP.show()
        elif a[0] == "Manually Put":
            w1.manually_put()
        #elif a[0] == "Sort":
            #for i in range(len(All)):
                #if i == c[0]-1:
                    #All[i].sort(p.RW[0])
        #elif a[0] == "Search":
            #for i in range(len(All)):
                #if i == c[0]-1:
                    #All[i].sort(p.RW[0])


r = RunSoftware()
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
OP = output()

enter = Userinput()
while 1<2:
    enter.userCommand()
    enter.outputcheckid()
