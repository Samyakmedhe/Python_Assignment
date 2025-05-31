def Pattern(iRows , iColumns):
    
    iCount = 1
    for iCnt1 in range(iRows):
        iCount = 1
        ch = 'a'
        for iCnt2 in range(iColumns):
            if iCnt1 % 2 == 0 :
                print(ch,end ="\t")
                ch = chr(ord(ch) + 1 )
            else:
                print(iCount , end="\t")
                iCount += 1
            
        print(" ")
        
    
def main():

    iValue1 = int(input("Enter Rows : "))
    iValue2 = int(input("Enter Coloums : "))
    Pattern(iValue1 , iValue2)

if __name__ == "__main__":
    main()