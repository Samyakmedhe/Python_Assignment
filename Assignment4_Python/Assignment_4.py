
def SumNonFact(iNo):  
    iSum = 0 
    for iCnt in range(1,iNo):
        if iNo % iCnt != 0:
            iSum += iCnt
    return iSum
def main():
    iValue = 0
    print("Enter number : ",end=' ')
    iValue = int(input())
    iRet = SumNonFact(iValue)
    print("Summation of Non factors is : ",iRet )
if __name__== "__main__":
    main()