Eninput = ''
Atoy = []
for ic in range(ord('a'), ord('b')+1):
    Atoy.append(chr(ic).upper())

xtest = 0
for test in Atoy:
    for test2 in range(1, 6):
        for itest in range(00, 100):
            if itest in [0,1, 2, 3, 4, 5, 6, 7, 8, 9]:
                itest = str(xtest) + str(itest) 
            # Eninput = str(1) + str(test) + str(test2) + str(itest) #1A100
            Eninput =  test2, int(itest), str(1)+str(test)+str(test2)+str(itest)
            # w5.storeProduct(Eninput)
            # print 'sucsess'
            print Eninput
