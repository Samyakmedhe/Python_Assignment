def MultiFact(iNo):
    iMulti = 1 

    print("( ",end = " ")
    for iCnt in range(1,iNo):
        if(iNo % iCnt == 0):
            print(iCnt," * ",end = " ")
            iMulti = iMulti * iCnt
    print(" )")
    return iMulti
    
    
def main():
    
    iValue = int(input("Enter number : "))
    iRet = MultiFact(iValue)

    print("Result is : ",iRet)
if __name__ =="__main__":
    main()