class Warehouse:
    def __init__(self):
        self.row = []
    def addRow(self,rows=0,grid=0):
        y = grid*grid
        for i in range(rows):
            grids = []
            self.row.append(grids)
            for j in range(y):
                grids.append([])
    def summarize(self):
        x = 0
        for i in self.row:
            x+=1
            print(x,"-",i)
    def storeProduct(self,rows=0,grid=0, product=None):
        if self.row[rows-1][grid] == []:
            self.row[rows-1][grid].append(product)
        else:
            print("Cannot store the product")
    def retrieveProduct(self,rows=0,grid=0, product=None):
        if self.row[rows-1][grid] != []:
            self.row[rows-1][grid].remove(product)
        else:
            print("Cannot retrieve the product")
    def sortRow(self,rows=0):
        self.row[rows].sorted()

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
w4.summarize()

