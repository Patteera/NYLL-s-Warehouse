
# TODO: 1A100      A-Y , 1-5 , 00-99
#
# FIXME:


def Functestcase():
    alllist = []
    Atoy = []
    for countay in range(ord('a'), ord('y')+1):
        Atoy.append(chr(countay).upper())
    cominput = ''
    add0 = 0
    for testcaseay in Atoy:
        # print testcase
        for count15 in range(1, 6):
            # print str(testcaseay) + str(count15)
            for count99 in range(0, 100):
                if count99 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    count99 = str(add0) + str(count99)
                # print count99
                cominput = str('1') + str(testcaseay) + \
                    str(count15) + str(count99)
                alllist.append(cominput)
    return alllist


    # return cominput
    # print cominput
# print(Functestcase())
# print alllist
for i in Functestcase():
    print i
