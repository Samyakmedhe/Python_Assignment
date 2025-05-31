def factorial(iNo):
    iFact  = 1 
    print("( ",end = " ")
    for iCnt in range(iNo,1,-1):
        print(iCnt," * ",end = " ")
        iFact = iFact * iCnt
    print(" )")
    return iFact
def main():
    
    iValue = int(input("Enter number : "))
    iRet = factorial(iValue)
    print("Result is : ",iRet)
    
if __name__ =="__main__":
    main()