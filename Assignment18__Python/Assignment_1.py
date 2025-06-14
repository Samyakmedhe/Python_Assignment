
def DifferenceEvenOdd(Arr, iLenght ):
    iSumEven = 0 
    iSumOdd = 0 
    
    for i in range(iLenght):
        if Arr[i] %  2 == 0 :
            iSumEven = iSumEven + Arr[i]
        else :
            iSumOdd = iSumOdd + Arr[i]

    iDiff = iSumEven - iSumOdd
    return iDiff
    

def main():
    iSize = int(input("Enter number of elements : "))

    Arr = []
    for iCnt in range(iSize):
        iValue = int(input("Enter elments : "))
        Arr.append(iValue)

    iRet = DifferenceEvenOdd(Arr , iSize)
    print("Result is : ",iRet)

if __name__ == "__main__":
    main()