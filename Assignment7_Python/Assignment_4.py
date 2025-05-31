def Oddfactorial(iNo):
    iFact  = 1 
    if iNo <= 0 :
        iNo = - iNo 
    
    print("( ",end = " ")
    for iCnt in range(iNo,0,-1):
        if iCnt % 2  != 0 :
            print(iCnt," * ",end = " ")
            iFact = iFact * iCnt
    print(" )")
    return iFact
def main():
    
    iValue = int(input("Enter number : "))
    iRet = Oddfactorial(iValue)
    print("Result is : ",iRet)
    
if __name__ =="__main__":
    main()