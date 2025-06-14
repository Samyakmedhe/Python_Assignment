


def lastOcc(Arr , iLenght , iNo):

    iPos = -1

    for iCnt in range(iLenght):
        if(Arr[iCnt] == iNo):
            iPos = iCnt
    
    return iPos

def main():
    
    iSize = int(input("Enter number of Elements : "))
    iNo = int(input("Enter number that you want to check : "))

    Arr = []
    for iCnt in range(iSize):
        iValue = int(input("Enter elements : "))
        Arr.append(iValue)
    
    iRet = lastOcc(Arr , iSize , iNo)
    if(iRet != -1):
        print("OUTPUT : ",iRet)
    else:
        print("Number not found : -1")

        
if __name__ =="__main__":
    main()