def Belt():
    b = []
    for i in range(10):
        b.append([])
    return b
belt = Belt()
def Inbelt(product = None):
    for i in range(10):
        if i == 0 and belt[0] == []:
            belt[i].append(product)
        elif i != 0 and belt[i-1] != []and belt[i] == [] and belt[i-1] != [product]:
            belt[i].append(product)
            break
def Outbelt():
    popproduct = []
    popproduct.append(belt[0])
    belt.remove(belt[0])
    belt.append([])
    print("out = ",popproduct)

Inbelt("A125")
Inbelt("A225")
Inbelt("A325")
Inbelt("A425")
Inbelt("A525")
Inbelt("A625")
Inbelt("A725")
Inbelt("A825")
Inbelt("A925")
Inbelt("A025")
Outbelt()
print(belt)
