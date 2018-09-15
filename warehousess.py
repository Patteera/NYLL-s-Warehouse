class warehouse :
    def __init__(self):
        self.wh1row = []
        self.wh2row = []
        self.wh3row = []
        self.wh4row = []
        self.wh5row = []

        self.ID = []
        self.IDall =[]

        self.Product_Type = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y' ]

    def wh1(self,row,slot):
        print "wh1 row1-5: "
        for i in range(row):
            self.wh1row.append([])

            for j in range(slot):
                self.wh1row[i].append([])

        for k in self.wh1row:
            print k

    def wh2(self,row,slot):
        print "wh2 row1-5: "
        for i in range(row):
            self.wh2row.append([])

            for j in range(slot):
                self.wh2row[i].append([])

        for k in self.wh2row:
            print k

    def wh3(self,row,slot):
        print "wh3 row1-5: "
        for i in range(row):
            self.wh3row.append([])

            for j in range(slot):
                self.wh3row[i].append([])

        for k in self.wh3row:
            print k

    def wh4(self,row,slot):
        print "wh4 row1-7: "
        for i in range(row):
            self.wh4row.append([])

            for j in range(slot):
                self.wh4row[i].append([])

        for k in self.wh4row:
            print k

    def wh5(self,row,slot):
        print "wh5 row1-20: "
        for i in range(row):
            self.wh5row.append([])

            for j in range(slot):
                self.wh5row[i].append([])

        for k in self.wh5row:
            print k

    def buildID(self):
        for i in self.Product_Type:
            for j in range(1,5+1):
                for k in range(0,9+1):
                    for l in range(0,9+1):
                        self.ID = i+str(j)+str(k)+str(l)
                        self.IDall.append(self.ID)
        print self.IDall
        print len(self.IDall)

    def appendWH1(self):




a = warehouse()
a.wh1(5,100)
a.wh2(5,100)
a.wh3(5,100)
a.wh4(7,25)
a.wh5(20,400)
a.buildID()



