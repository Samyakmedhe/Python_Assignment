def Pattern(iRows , iColumns):
  
    for iCnt in range(iRows):
        ch = 'A'
        for iCnt in range(iColumns):
            print(ch,end ="\t")
            ch = chr(ord(ch) + 1 )
        print(" ")
       
    
def main():

    iValue1 = int(input("Enter Rows : "))
    iValue2 = int(input("Enter Coloums : "))
    Pattern(iValue1 , iValue2)

if __name__ == "__main__":
    main()