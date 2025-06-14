def Pattern(iRows , iColumns):

    for iCnt1 in range(iRows):
        for iCnt2 in range(iColumns,0, -1):
            print(iCnt2,end ="\t")
        print(" ")
       
    
def main():

    iValue1 = int(input("Enter Rows : "))
    iValue2 = int(input("Enter Coloums : "))
    Pattern(iValue1 , iValue2)

if __name__ == "__main__":
    main()