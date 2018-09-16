
class Warehouse:
    def __init__(self):
        self.row = []

    def addRow(self, rows=0, grid=0):
        t1 = grid*grid
        for i in range(rows):
            grids = []
            self.row.append(grids)
            for y in range(0, t1):
                grids.append([y])

    def sumtable(self):
        x = 0
        print(' \n')
        for x1 in self.row:
            x += 1
            print(x , x1)  # (x, x1)
            print('\n')

    def addProduct(self, rows=0, grid=0, product=None):
        # self.row[rows-1].pop(grid)
        # self.row[rows-1].insert(grid, product)  # (index, element)
        self.row[rows - 1][grid].append(product)
    
    def addProductwh5(self, rows=0, grid=0, product=None):
        self.row[rows][grid].append(product)

    def deleteProduct(self, rows=0, grid=0, product=None):
        self.row[rows-1][grid].remove(product)
        # self.row[rows-1].insert(grid, grid)  # (index, element)


wh1 = Warehouse()
wh1.addRow(5, 10)  # rows, grid
wh2 = Warehouse()
wh2.addRow(5, 10)
wh3 = Warehouse()
wh3.addRow(5, 10)
wh4 = Warehouse()
wh4.addRow(7, 5)
wh5 = Warehouse()
wh5.addRow(20, 20)
# print(wh1.row)


while(1):
    Eninput = raw_input('Enter Input Command  : ').upper()
    Dtoy = []
    for ic in range(ord('d'), ord('y')+1):
        Dtoy.append(chr(ic).upper())

    if (int(Eninput[0]) == 1):
        if (len(str(Eninput)) == 5):
            if (str(Eninput[1]) in ['A']):
                    
                if (int(Eninput[2:5]) in range(100, 499 + 1)):
                    # rows , grid , product 1A125
                    wh1.addProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])

                    for cL in wh1.row[int(Eninput[2])-1]: #check
                        if len(cL) > 2:
                            print('Warehouse' + Eninput[2] + ' row' + Eninput[2] + ' slot : ' + Eninput[3:] + ' is full')
                            wh1.deleteProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])
                else:
                    print('\n Input Command Error \n')

            elif(str(Eninput[1]) in ['B']):
                if (int(Eninput[2:5]) in range(100, 499+1)):  # 100
                    wh2.addProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])

                    for cL in wh2.row[int(Eninput[2])-1]: #check
                        if len(cL) > 2:
                            print('Warehouse : ' + Eninput[2] + ' rows :' + Eninput[2] + ' is full')
                            wh2.deleteProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])
                else:
                    print('\n Input Command Error \n')

            elif(str(Eninput[1]) in ['C']):
                if (int(Eninput[2:5]) in range(100, 499+1)):  # 100
                    wh3.addProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])

                    for cL in wh3.row[int(Eninput[2])-1]: #check
                        if len(cL) > 2:
                            print('Warehouse : ' + Eninput[2] + ' rows :' + Eninput[2] + ' is full')
                            wh3.deleteProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])
                else:
                    print('\n Input Command Error \n')

            elif(str(Eninput[1]) in Dtoy):
                for c20 in range(20):
                    xc = 0
                    for countwh5 in wh5.row[c20]:  #1D100 
                        if (len(countwh5) == 1):
                            wh5.addProductwh5(c20, xc, Eninput[1:])
                            break
                        else:
                            pass
                        xc += 1
                    break
                # wh5.addProductwh5(Eninput[1:])


                for cL in wh5.row[int(Eninput[2])-1]: #check
                    if len(cL) > 2:
                        print('Warehouse : ' + Eninput[2] + ' rows :' + Eninput[2] + ' is full')
                        wh5.deleteProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])

            
        else:
            print('\n Input Command Error \n')

    elif (int(Eninput[0]) == 0):  # cammand 0 Delete
        if (str(Eninput[1]) in ['A']):
            if (int(Eninput[2:5]) in range(100, 499+1)):  # 0A100
                wh1.deleteProduct(int(Eninput[2]), int(Eninput[3:]), Eninput[1:])
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
