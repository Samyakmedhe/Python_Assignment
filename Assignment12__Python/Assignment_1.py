def Pattern(iRows , iColumns):

    for iCnt in range(iRows):
        for iCnt in range(iColumns):
            print(" * ",end ="\t")
        print(" ")
       
    
def main():

    iValue1 = int(input("Enter Rows : "))
    iValue2 = int(input("Enter Coloums : "))
    Pattern(iValue1 , iValue2)

if __name__ == "__main__":
    main()