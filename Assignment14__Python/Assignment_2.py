def Pattern(iRows , iColumns):
    iEven = 2 
    iOdd = 1 
    for iCnt1 in range(iRows):
        for iCnt2 in range(iColumns * 2):
            if iCnt1 % 2 == 0 :

                print(iEven,end = "\t")
                iEven+= 2 
            else:
                print(iOdd , end ="\t")
            odd +=2
        print("")
    
def main():

    iValue1 = int(input("Enter Rows : "))
    iValue2 = int(input("Enter Coloums : "))
    Pattern(iValue1 , iValue2)

if __name__ == "__main__":
    main()