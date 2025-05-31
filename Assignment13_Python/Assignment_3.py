def Pattern(iRows , iColumns):
    ch = 'A'
    for iCnt1 in range(iRows):
        
        for iCnt2 in range(iColumns):
            print(ch,end ="\t")
            
            
        print(" ")
        ch = chr(ord(ch) + 1 )
    
def main():

    iValue1 = int(input("Enter Rows : "))
    iValue2 = int(input("Enter Coloums : "))
    Pattern(iValue1 , iValue2)

if __name__ == "__main__":
    main()