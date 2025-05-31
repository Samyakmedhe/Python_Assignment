def Pattern(iRows , iColumns):
    
    for iCnt1 in range(iRows):
        
        for iCnt2 in range(1,iColumns+1):
            if iCnt1 % 2 == 0 :
                print(iCnt2,end ="\t")
            else:
                print(iCnt2,end ="\t")
            
        print(" ")
    
def main():

    iValue1 = int(input("Enter Rows : "))
    iValue2 = int(input("Enter Coloums : "))
    Pattern(iValue1 , iValue2)

if __name__ == "__main__":
    main()