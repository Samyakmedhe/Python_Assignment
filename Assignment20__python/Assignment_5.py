


def Productodd(Arr , iLenght):
    iMulti = 1
    oddFound = False
    for iCnt in range(iLenght):
        if(Arr[iCnt] % 2 != 0):
            iMulti = iMulti * Arr[iCnt]
            oddFound = True
    if oddFound == True:
        return iMulti
    else:
        return 0
def main():
    
    iSize = int(input("Enter number of Elements : "))

    Arr = []
    for iCnt in range(iSize):
        iValue = int(input("Enter elements : "))
        Arr.append(iValue)
    
    iRet = Productodd(Arr , iSize)
    print("OUTPUT : ",iRet)
    

    
if __name__ =="__main__":
    main()