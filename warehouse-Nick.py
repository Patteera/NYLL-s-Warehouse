
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
            print(' \n')

    def addProduct(self, rows=0, grid=0, product=None):
        self.row[rows-1].pop(grid-1)
        self.row[rows-1].insert(grid-1, product)

    def deleteProduct(self, rows=0, grid=0, product=None):
        self.row[rows-1].remove(product)
        self.row[rows-1].insert(grid-1, grid)  # (index, element)


wh1 = Warehouse()
wh1.addRow(5, 10)
wh2 = Warehouse()
wh2.addRow(5, 10)
wh3 = Warehouse()
wh3.addRow(5, 10)
wh4 = Warehouse()
wh4.addRow(7, 5)
wh5 = Warehouse()
wh5.addRow(20, 20)


while(1):
    Eninput = raw_input('Enter Input Command  : ')
    if (int(Eninput[0]) == 1):
        AtoT = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h', \
                'I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t']
        if (str(Eninput[1]) in AtoT):
            if (int(Eninput[2:5]) in range(100,486+1) ):
                wh5.addProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:]) # rows , grid , product
            else:
                print('\n Input Command Error \n')
        # elif((str)):


        else:
            print('\n Input Command Error \n')

    elif (int(Eninput[0]) == 0):
        print(2)

    elif (int(Eninput[:]) == 40000):
        print('\n')
        print(' Information of all warehouses :\n')
        print('Warehouse 1 : \n')
        wh1.sumtable()
        print('--------------\n')
        print('Warehouse 2 : \n')
        wh2.sumtable()
        print('--------------\n')
        print('Warehouse 3 \n')
        wh3.sumtable()
        print('--------------\n')
        print('Warehouse 4 : \n')
        wh4.sumtable()
        print('--------------\n')
        print('Warehouse 5 : \n')
        wh5.sumtable()
        print('--------------\n')

    else:
        print('\n Input Command Error \n')

# 1A125
# Eninput = raw_input('Enter Input Command  : ')
# wh1 = Warehouse()
# wh1.addRow(5, 10)
# wh1.addProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])
# print('---Warehouse 1---')
# wh1.addProduct(1, 100, "A125")  #ff
# wh1.addProduct(int(Eninput[1]), int(Eninput[2:]), Eninput)
# wh1.deleteProduct(int(Eninput[1]), int(Eninput[2:]), Eninput)
# wh1.sumtable()
