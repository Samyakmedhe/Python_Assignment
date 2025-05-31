def DiffOddEven(iNo):
    iFactEven  = 1 
    iFactodd = 1 
    iDiff = 0 

    if iNo <= 0 :
        iNo = - iNo 
    
    print("( ",end = " ")
    for iCnt in range(iNo,0,-1):
        if iCnt % 2  == 0 :
            iFactEven = iFactEven * iCnt
        else:
            iFactodd = iFactodd * iCnt
    print(iFactEven," - ",iFactodd, end = " ")
    print(" )")
    iDiff = iFactEven - iFactodd
    return iDiff
def main():
    
    iValue = int(input("Enter number : "))
    iRet = DiffOddEven(iValue)
    print("Result is : ",iRet)
    
if __name__ =="__main__":
    main()