


def FirstOCC(Arr , iLenght , iNo):

    iCount = 0

    for iCnt in range(1,iLenght):
        iCount = iCount + 1
        if(Arr[iCnt] == iNo):
            break
    else:
        return -1
    return iCount

def main():
    
    iSize = int(input("Enter number of Elements : "))
    iNo = int(input("Enter number that you want to check : "))

    Arr = []
    for iCnt in range(iSize):
        iValue = int(input("Enter elements : "))
        Arr.append(iValue)
    
    iRet = FirstOCC(Arr , iSize , iNo)
    print("OUTPUT : ",iRet)
    

    
if __name__ =="__main__":
    main()