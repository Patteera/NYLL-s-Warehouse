
class Warehouse:
    def __init__(self):
        self.row = []

    def addRow(self, rows=0, grid=0):
        t1 = grid*grid
        for i in range(rows):
            grid = []
            for y in range(1, t1):
                # self.row.append(y)
                grid.append(y)
            self.row.append(grid)

    def sumtable(self):
        x = 0
        for x1 in self.row:
            x += 1
            print(x, x1)
            print('\n')

    def addProduct(self, rows=0, grid=0, product=None):
        self.row[rows-1].pop(grid-1)
        self.row[rows-1].insert(grid-1, product)

    def deleteProduct(self, rows=0, grid=0, product=None):
        self.row[rows-1].remove(product)
        self.row[rows-1].insert(grid-1, grid)  # (index, element)


wh1 = Warehouse()
wh1.addRow(5, 10)
# test123
# while(1):
#     Eninput = raw_input('Enter Input Command  : ')
#     if (int(Eninput[0]) == 1):
#         # rows , grid , product
#         # wh1.addProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])
#         print(1)
#         addProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])
        
#     elif (int(Eninput[0]) == 0):
#         print(2)
#         break


Eninput = raw_input('Enter Input Command  : ')

# wh1.addProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])
# print('---Warehouse 1---')
# wh1.addProduct(1, 100, "A125")  #ff
# wh1.addProduct(int(Eninput[1]), int(Eninput[2:]), Eninput)
# wh1.deleteProduct(int(Eninput[1]), int(Eninput[2:]), Eninput)
wh1.sumtable()

# wh2 = Warehouse()
# wh2.addRow(5 ,10)
# print('---Warehouse 2---')
# wh2.sumtable()

# wh3 = Warehouse()
# wh3.addRow(5, 10)
# print('---Warehouse 3---')
# wh3.sumtable()

# wh4 = Warehouse()
# wh4.addRow(7, 5)
# print('---Warehouse 4---')
# wh4.sumtable()

# wh5 = Warehouse()
# wh5.addRow(20, 20)
# print('---Warehouse 5---')
# wh5.sumtable()
