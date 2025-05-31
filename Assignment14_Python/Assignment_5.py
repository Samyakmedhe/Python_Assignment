def Pattern(iRows , iColumns):

    for iCnt1 in range(1, iRows+1):
        iCount = iCnt1
        for iCnt2 in range(iColumns):
            print(iCount,end ="\t")
            iCount += 1
            
        print(" ")
    
def main():

    iValue1 = int(input("Enter Rows : "))
    iValue2 = int(input("Enter Coloums : "))
    Pattern(iValue1 , iValue2)

if __name__ == "__main__":
    main()