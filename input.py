class userinput:
    def __init__(self):
        self.command = []
    def userCommand(self):
        i = input("Enter Your Command :")
        self.command.append(i)
    def checkid(self):
        i = self.command
        if len(i[0]) ==5:
            if i[0][0].isdigit() == True:
                if int(i[0][0]) <= 5 or int(i[0][0]) == 9:
                    if i[0][1].isupper() == True and i[0][1] != "Z":
                        if i[0][2].isdigit() == True and int(i[0][2])<=5 and int(i[0][2]) != 0:
                            if i[0][3:4].isdigit() == True and int(i[0][3:4]) <= 99:
                                return True
        return False
    def readid(self):
        i = self.command
        if i[0][0] == "0":return "Retrieve"
        elif i[0][0] == "1":return "Store"
        elif i[0][0] == "2":return "Sort"
        elif i[0][0] == "3":return "Retrieve Belt"
        elif i[0][0] == "4":return "Output"
        elif i[0][0] == "5":return "Search"
        elif i[0][0] == "9":return "MN Change"

enter = userinput()
enter.userCommand()
if enter.checkid() == False:
    print("Product ID ERROR")
else:
    enter.readid()


