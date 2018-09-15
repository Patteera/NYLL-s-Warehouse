
class Warehouse:
    def __init__(self):
        self.row = []

    def addRow(self, rows=0, grid=0):
        t1 = grid*grid
        for i in range(rows):
            grid = []
            for y in range(0, t1):
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
        self.row[rows-1].pop(grid)
        self.row[rows-1].insert(grid, product)  # (index, element)

    def deleteProduct(self, rows=0, grid=0, product=None):
        self.row[rows-1].remove(product)
        self.row[rows-1].insert(grid, grid)  # (index, element)


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
    DtoY = ['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y' ]
    if (int(Eninput[0]) == 1):

        if (str(Eninput[1].upper()) in ['A']):
            if (int(Eninput[2:5]) in range(100, 499+1)):
                 # rows , grid , product
                wh1.addProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])
            else:
                print('\n Input Command Error \n')

        elif(str(Eninput[1].upper()) in ['B']):
            if (int(Eninput[2:5]) in range(100, 499+1)):  # 100
                wh2.addProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])
            else:
                print('\n Input Command Error \n')

        elif(str(Eninput[1].upper()) in ['C']):
            if (int(Eninput[2:5]) in range(100, 499+1)):  # 100
                wh3.addProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])
            else:
                print('\n Input Command Error \n')

        elif(str(Eninput[1].upper()) in DtoY):
            if (int(Eninput[2:5]) in range(100, 7999+1)):  # 100
                wh5.addProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])
            else:
                print('\n Input Command Error \n')

        else:
            print('\n Input Command Error \n')

    elif (int(Eninput[0]) == 0):
        if (str(Eninput[1]) in AtoT):
            if (int(Eninput[2:5]) in range(100, 486+1)):
                wh5.deleteProduct(int(Eninput[2]), int(
                    Eninput[3:]), Eninput[1:])
            else:
                print('\n Input Command Error \n')

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

# Type A - T , 1 0 0 - 4 8 6 warehouse 5
