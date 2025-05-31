
def FactDiff(iNo):  
    iSum1 = 0 
    iSum2 = 0 
    iDiff = 0
    for iCnt in range(1,iNo):
        if iNo % iCnt != 0:
            iSum1 += iCnt
        else:
            iSum2 += iCnt
    print("(",iSum2,"-",iSum1,")")
    iDiff = iSum2 - iSum1
    return iDiff
def main():
    iValue = 0
    print("Enter number : ",end=' ')
    iValue = int(input())
    iRet = FactDiff(iValue)
    print("Summation of Non factors is : ",iRet )
if __name__== "__main__":
    main()