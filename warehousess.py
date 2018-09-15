class warehouse :
    def __init__(self):
        self.wh1row = []
        self.wh2row = []
        self.wh3row = []
        self.wh4row = []
        self.wh5row = []

        self.ID = []
        self.IDall = []

        self.wh1_productID_address = {}
        self.wh2_productID_address = {}
        self.wh3_productID_address = {}
        self.wh4_productID_address = {}
        self.wh5_R1_productID_address = {}
        self.wh5_R2_productID_address = {}
        self.wh5_R3_productID_address = {}
        self.wh5_R4_productID_address = {}
        self.wh5_R5_productID_address = {}
        self.wh5_R6_productID_address = {}
        self.wh5_R7_productID_address = {}
        self.wh5_R8_productID_address = {}

        self.Product_Type = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y' ]

    def wh1(self,row,slot):
        #print "wh1 row1-5: "
        for i in range(row):
            self.wh1row.append([])

            for j in range(slot):
                self.wh1row[i].append([])

        for k in self.wh1row:
           # print k
            self.wh1row = k
            #print self.wh1row

    def wh2(self,row,slot):
        #print "wh2 row1-5: "
        for i in range(row):
            self.wh2row.append([])

            for j in range(slot):
                self.wh2row[i].append([])

        for k in self.wh2row:
            #print k
            self.wh2row = k
            #print self.wh2row

    def wh3(self,row,slot):
        #print "wh3 row1-5: "
        for i in range(row):
            self.wh3row.append([])

            for j in range(slot):
                self.wh3row[i].append([])

        for k in self.wh3row:
            #print k
            self.wh3row = k
            #print self.wh3row

    def wh4(self,row,slot):
        #print "wh4 row1-7: "
        for i in range(row):
            self.wh4row.append([])

            for j in range(slot):
                self.wh4row[i].append([])

        for k in self.wh4row:
           # print k
           self.wh4row = k
           #print self.wh4row

    def wh5(self,row,slot):
        #print "wh5 row1-20: "
        for i in range(row):
            self.wh5row.append([])

            for j in range(slot):
                self.wh5row[i].append([])

        for k in self.wh5row:
            #print k
            self.wh5row = k
            #print self.wh5row

    def buildID(self):
        for i in self.Product_Type:
            for j in range(1,5+1):
                for k in range(0,9+1):
                    for l in range(0,9+1):
                        self.ID = i+str(j)+str(k)+str(l)
                        self.IDall.append(self.ID)
        #print self.IDall
        #print len(self.IDall)

    def appendWH1(self):
        for i in self.IDall:
            indexID = self.IDall.index(i)
            #print self.IDall.index(i)
            if 0 <= indexID <= 499 :
                self.wh1_productID_address[indexID] = [i]
        self.wh1_productID_address = self.wh1_productID_address
        print self.wh1_productID_address

    def appendWH2(self):
        for i in self.IDall:
            indexID = self.IDall.index(i)
            #print self.IDall.index(i)
            if 500 <= indexID <= 999 :
                self.wh2_productID_address[indexID - 500] = [i]
            self.wh2_productID_address = self.wh2_productID_address
        print self.wh2_productID_address

    def appendWH3(self):
        for i in self.IDall:
            indexID = self.IDall.index(i)
            #print self.IDall.index(i)
            if 1000 <= indexID <= 1499 :
                self.wh3_productID_address[indexID - 1000] = [i]
            self.wh3_productID_address = self.wh3_productID_address
        print self.wh3_productID_address

    def appendWH4(self):
        for i in self.IDall:
            indexID = self.IDall.index(i)
            #print self.IDall.index(i)
            if 1500 <= indexID <= 1674 :
                self.wh4_productID_address[indexID - 1500] = [i]
            self.wh4_productID_address = self.wh4_productID_address
        print self.wh4_productID_address

    def appendWH5_R1(self):
        for i in self.IDall:
            indexID = self.IDall.index(i)
            #print self.IDall.index(i)
            if 1675 <= indexID <= 2074 :
                self.wh5_R1_productID_address[indexID - 1675] = [i]
            self.wh5_R1_productID_address = self.wh5_R1_productID_address
        print self.wh5_R1_productID_address

    def appendWH5_R2(self):
        for i in self.IDall:
            indexID = self.IDall.index(i)
            #print self.IDall.index(i)
            if 2075 <= indexID <= 2474 :
                self.wh5_R2_productID_address[indexID - 2075] = [i]
            self.wh5_R2_productID_address = self.wh5_R2_productID_address
        print self.wh5_R2_productID_address

    def appendWH5_R3(self):
        for i in self.IDall:
            indexID = self.IDall.index(i)
            #print self.IDall.index(i)
            if 2475 <= indexID <= 2874 :
                self.wh5_R3_productID_address[indexID - 2475] = [i]
            self.wh5_R3_productID_address = self.wh5_R3_productID_address
        print self.wh5_R3_productID_address

    def appendWH5_R4(self):
        for i in self.IDall:
            indexID = self.IDall.index(i)
            #print self.IDall.index(i)
            if 2875 <= indexID <= 3274 :
                self.wh5_R4_productID_address[indexID - 2875] = [i]
            self.wh5_R4_productID_address = self.wh5_R4_productID_address
        print self.wh5_R4_productID_address

    def appendWH5_R5(self):
        for i in self.IDall:
            indexID = self.IDall.index(i)
            #print self.IDall.index(i)
            if 3275 <= indexID <= 3674 :
                self.wh5_R5_productID_address[indexID - 3275] = [i]
            self.wh5_R5_productID_address = self.wh5_R5_productID_address
        print self.wh5_R5_productID_address

    def appendWH5_R6(self):
        for i in self.IDall:
            indexID = self.IDall.index(i)
            #print self.IDall.index(i)
            if 3675 <= indexID <= 4074 :
                self.wh5_R6_productID_address[indexID - 3675] = [i]
            self.wh5_R6_productID_address = self.wh5_R6_productID_address
        print self.wh5_R6_productID_address

    def appendWH5_R7(self):
        for i in self.IDall:
            indexID = self.IDall.index(i)
            #print self.IDall.index(i)
            if 4075 <= indexID <= 4474 :
                self.wh5_R7_productID_address[indexID - 4075] = [i]
            self.wh5_R7_productID_address = self.wh5_R7_productID_address
        print self.wh5_R7_productID_address

    def appendWH5_R8(self):
        for i in self.IDall:
            indexID = self.IDall.index(i)
            #print self.IDall.index(i)
            if 4475 <= indexID <= 4874 :
                self.wh5_R8_productID_address[indexID - 4475] = [i]
            self.wh5_R8_productID_address = self.wh5_R8_productID_address
        print self.wh5_R8_productID_address

a = warehouse()
a.wh1(5,100)
a.wh2(5,100)
a.wh3(5,100)
a.wh4(7,25)
a.wh5(20,400)
a.buildID()
a.appendWH1()
a.appendWH2()
a.appendWH3()
a.appendWH4()
a.appendWH5_R1()
a.appendWH5_R2()
a.appendWH5_R3()
a.appendWH5_R4()
a.appendWH5_R5()
a.appendWH5_R6()
a.appendWH5_R7()
a.appendWH5_R8()
