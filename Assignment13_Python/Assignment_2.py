def Pattern(iRows , iColumns):
  
    for iCnt1 in range(iRows):
        ch1 = 'A'
        ch2 = 'a'
        for iCnt2 in range(iColumns):
            if iCnt1 % 2 == 0 :
                print(ch1,end ="\t")
                ch1 = chr(ord(ch1) + 1 )
            else:
                print(ch2,end ="\t")
                ch2 = chr(ord(ch2) + 1 )

        print(" ")
       
    
def main():

    iValue1 = int(input("Enter Rows : "))
    iValue2 = int(input("Enter Coloums : "))
    Pattern(iValue1 , iValue2)

if __name__ == "__main__":
    main()