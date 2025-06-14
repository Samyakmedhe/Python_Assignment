


def rangeX(Arr , iLenght , iStart ,iEnd):

    result = []
    for iCnt in range(iLenght):
        if((Arr[iCnt] >= iStart) and (Arr[iCnt]<= iEnd)):
            result.append(Arr[iCnt])
    return result 

def main():
    
    iSize = int(input("Enter number of Elements : "))
    iNo1 = int(input("Enter Starting point : "))
    iNo2 = int(input("Enter Ending point : "))
    Arr = []
    for iCnt in range(iSize):
        iValue = int(input("Enter elements : "))
        Arr.append(iValue)
    
    iRet = rangeX(Arr , iSize , iNo1, iNo2)
    print("Elements in range : ",iRet)

        
if __name__ =="__main__":
    main()