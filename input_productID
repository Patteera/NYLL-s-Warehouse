import string
class ProductID:
    def __init__(self):
        self.pdid = []
    def addID(self,ID = None):
        self.pdid.append(ID)
    def findWH(self):
        if self.pdid[0][1] in string.ascii_uppercase[:20]:
            print(self.pdid)
            print("Belong to w5")
        elif self.pdid[0][1] in string.ascii_uppercase[20]:
            if int(self.pdid[0][2:5]) < 360:
                print(self.pdid)
                print("Belong to w5")
            else:
                print(self.pdid)
                print("Belong to w1")
        elif self.pdid[0][1] in string.ascii_uppercase[21]:
            if int(self.pdid[0][2:5]) < 472 or int(self.pdid[0][2:5]) > 486:
                print(self.pdid)
                print("Belong to w1")
            elif int(self.pdid[0][2:5]) >= 472 and int(self.pdid[0][2:5]) < 487:
                print(self.pdid)
                print("Belong to w2")
        elif self.pdid[0][1] in string.ascii_uppercase[22]:
                print(self.pdid)
                print("Belong to w2")
        elif self.pdid[0][1] in string.ascii_uppercase[23]:
            if int(self.pdid[0][2:5]) < 198:
                print(self.pdid)
                print("Belong to w2")
            else:
                print(self.pdid)
                print("Belong to w3")
        elif self.pdid[0][1] in string.ascii_uppercase[24]:
            if int(self.pdid[0][2:5]) < 311:
                print(self.pdid)
                print("Belong to w3")
            else:
                print(self.pdid)
                print("Belong to w4")
    def findRW(self):
        for i in range(25):
            if i < 20:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    print("Belong to row",i+1)
            elif i == 20:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) < 360:
                        for n in range(20):
                            if int(self.pdid[0][2:5]) >= 100 +(12*(n))+ n and int(self.pdid[0][2:5]) < 100 +(12*(n+1))+n+1:
                                print("Belong to row",n+1)
                    if int(self.pdid[0][2:5]) >= 360 and int(self.pdid[0][2:5]) < 487:
                        for n in range(2):
                            if int(self.pdid[0][2:5]) >= 360 + (100*n)+n and int(self.pdid[0][2:5]) < 360 + (100*(n+1))+n+1:
                                print("Belong to row",n+1)
                    if int(self.pdid[0][2:5]) > 486 and int(self.pdid[0][2:5]) < 600:
                        for n in range(2):
                            if int(self.pdid[0][2:5]) >= 487 + (100*n) and int(self.pdid[0][2:5]) < 487 + (100*(n+1))+n:
                                print("Belong to row",n+1)
            elif i == 21:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 173:
                        for n in range(3):
                            if int(self.pdid[0][2:5]) >= 100 + (73*n)+n and int(self.pdid[0][2:5]) < 100 + (72*(n+1))+n+1:
                                print("Belong to row",n+2)
                    if int(self.pdid[0][2:5]) >= 173 and int(self.pdid[0][2:5]) < 473:
                        for n in range(3):
                            if int(self.pdid[0][2:5]) >= 173 + (100*n)+n and int(self.pdid[0][2:5]) < 173 + (100*(n+1))+n+1:
                                print("Belong to row",n+3)
                    if int(self.pdid[0][2:5]) >= 473 and int(self.pdid[0][2:5]) < 487:
                        print("Belong to row",1)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        for n in range(2):
                            if int(self.pdid[0][2:5]) >= 487 + (72*n)+n and int(self.pdid[0][2:5]) < 487 + (72*(n+1))+n+1:
                                print("Belong to row",n+2)
            elif i == 22:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 186:
                            print("Belong to row",1)
                    if int(self.pdid[0][2:5]) >= 186 and int(self.pdid[0][2:5]) < 487:
                        for n in range(4):
                            if int(self.pdid[0][2:5]) >= 186 + (99*n)+n and int(self.pdid[0][2:5]) < 186 + (99*(n+1))+n+1:
                                print("Belong to row",n+2)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        for n in range(2):
                            if int(self.pdid[0][2:5]) >= 487 + (85*n)+n and int(self.pdid[0][2:5]) < 487 + (85*(n+1))+n+1:
                                print("Belong to row",n+1)
            elif i == 23:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 199:
                            print("Belong to row",5)
                    if int(self.pdid[0][2:5]) >= 199 and int(self.pdid[0][2:5]) < 487:
                        for n in range(3):
                            if int(self.pdid[0][2:5]) >= 199 + (100*n)+n and int(self.pdid[0][2:5]) < 199 + (100*(n+1))+n+1:
                                print("Belong to row",n+1)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        for n in range(2):
                            if int(self.pdid[0][2:5]) >= 487 + (99*n)+n and int(self.pdid[0][2:5]) < 487 + (99*(n+1))+n+1:
                                print("Belong to row",n+1)
            elif i == 24:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 112:
                            print("Belong to row",3)
                    if int(self.pdid[0][2:5]) >= 112 and int(self.pdid[0][2:5]) < 312:
                        for n in range(3):
                            if int(self.pdid[0][2:5]) >= 112 + (99*n)+n and int(self.pdid[0][2:5]) < 112 + (99*(n+1))+n+1:
                                print("Belong to row",n+4)
                    if int(self.pdid[0][2:5]) >= 312 and int(self.pdid[0][2:5]) < 487:
                        for n in range(7):
                            if int(self.pdid[0][2:5]) >= 312 + (24*n)+n and int(self.pdid[0][2:5]) < 312 + (24*(n+1))+n+1:
                                print("Belong to row",n+1)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        for n in range(7):
                            if int(self.pdid[0][2:5]) >= 487 + (25*n)+n and int(self.pdid[0][2:5]) < 487 + (25*(n+1))+n+1:
                                print("Belong to row",n+1)
    def findSL(self):
         for i in range(25):
            if i < 20:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 487:
                        x = int(self.pdid[0][2:5])-100
                        print("Belong to slot",x)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        x = int(self.pdid[0][2:5])-487
                        print("Belong to slot",x)
            elif i == 20:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) < 113:
                        x = int(self.pdid[0][2:5])-100 +387
                        print("Belong to slot",x)
                    elif int(self.pdid[0][2:5]) >= 113 and int(self.pdid[0][2:5]) < 360:
                        x = int(self.pdid[0][2:5])-100
                        if x % 13 == 0:
                            y = 387
                            print("Belong to slot",y)
                        else:
                            x1 = int(x/13)
                            x2 = 13*x1
                            y = x - x2 + 387
                            print("Belong to slot",y)
                    elif int(self.pdid[0][2:5]) >= 360 and int(self.pdid[0][2:5]) < 487:
                        x = int(self.pdid[0][2:5])-360
                        if x <100:
                            print("Belong to slot",x)
                        else:
                            print("Belong to slot",x-100)
                    elif int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 587:
                        x = int(self.pdid[0][2:5])-487
                        print("Belong to slot",x)
                    elif int(self.pdid[0][2:5]) >= 587 and int(self.pdid[0][2:5]) < 600:
                        x = int(self.pdid[0][2:5])-587
                        print("Belong to slot",x)
            elif i == 21:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 473:
                        x1 = int(self.pdid[0][2:5])-100
                        if x1 + 27 <100:
                            print("Belong to slot",x1+27)
                        else:
                            x = x1-73
                            if x > 100:
                                x2 = int(x/100)
                                x3 = x2*100
                                x4 = x-x3
                                print("Belong to slot",x4)
                            else:
                                print("Belong to slot",x)
                    if int(self.pdid[0][2:5]) >= 473 and int(self.pdid[0][2:5]) < 487:
                        x = int(self.pdid[0][2:5])-473
                        print("Belong to slot",x)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        x = int(self.pdid[0][2:5])-460
                        if x < 100:
                            print("Belong to slot",x)
                        else:
                            print("Belong to slot",x-100)
            elif i == 22:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 487:
                        x = int(self.pdid[0][2:5])-100
                        if x <100:
                            print("Belong to slot",x+14)
                        else:
                            x1 = int(x/100)
                            x2 = x1*100
                            x3 = x-x2
                            if x3 +14 <100:
                                print("Belong to slot",x3+14)
                            if x3 +14>99:
                                print("Belong to slot",x3+14-100)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        x = int(self.pdid[0][2:5])-487+14
                        if x <100:
                            print("Belong to slot",x)
                        else:
                            print("Belong to slot",x-100)
            elif i == 23:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 199:
                        x = int(self.pdid[0][2:5])-100+1
                        print("Belong to slot",x)
                    if int(self.pdid[0][2:5]) >= 199 and int(self.pdid[0][2:5]) < 487:
                        x = int(self.pdid[0][2:5])-199
                        if x<100:
                            print("Belong to slot",x)
                        else:
                            x1 = int(x/100)
                            x2 = x1*100
                            x3 = x-x2
                            print("Belong to slot",x3)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        x = int(self.pdid[0][2:5])-487
                        if x<100:
                            print("Belong to slot",x)
                        else:
                            x1 = int(x/100)
                            x2 = x1*100
                            x3 = x-x2
                            print("Belong to slot",x3)
            elif i == 24:
                if self.pdid[0][1] in string.ascii_uppercase[i]:
                    if int(self.pdid[0][2:5]) >= 100 and int(self.pdid[0][2:5]) < 312:
                        x = int(self.pdid[0][2:5])-100+88
                        if x<100:
                            print("Belong to slot",x)
                        else:
                            x1 = int(x/100)
                            x2 = x1*100
                            x3 = x-x2
                            print("Belong to slot",x3)
                    if int(self.pdid[0][2:5]) >= 312 and int(self.pdid[0][2:5]) < 486:
                        x = int(self.pdid[0][2:5])-312
                        if x<25:
                            print("Belong to slot",x)
                        else:
                            x1 = int(x/25)
                            x2 = x1*25
                            x3 = x-x2
                            print("Belong to slot",x3)
                    if int(self.pdid[0][2:5]) >= 487 and int(self.pdid[0][2:5]) < 600:
                        x = int(self.pdid[0][2:5])-487
                        if x<25:
                            print("Belong to slot",x)
                        else:
                            x1 = int(x/25)
                            x2 = x1*25
                            x3 = x-x2
                            print("Belong to slot",x3)
p = ProductID()
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
                if int(i[0]) <= 5 or int(i[0]) == 9:
                    if i[1].isupper() == True and i[1] != "Z":
                        if i[2].isdigit() == True and int(i[2])<=5 and int(i[2]) != 0:
                            if i[3:5].isdigit() == True and int(i[3:5]) <= 99:
                                return True
        return False
    def outputcheckid(self):
        opc = self.checkid()
        if opc == False:
            print("Product ID ERROR")
        if opc == True:
            self.readcommand()
            self.readid()
    def readcommand(self):
        i = self.command
        if i[0] == "0":
            print("Retrieve")
        if i[0] == "1":
            print("Store")
        if i[0] == "2":
            print("Sort")
        if i[0] == "3":
            print("Retrieve belt")
        if i[0] == "4":
            print("Output")
        if i[0] == "5":
            print("Search")
        if i[0] == "9":
            print("Manually Put")
    def readid(self):
        i = self.command
        p.addID(i)
        p.findWH()
        p.findRW()
        p.findSL()


enter = Userinput()
while 1<2:
    enter.userCommand()
    enter.outputcheckid()
