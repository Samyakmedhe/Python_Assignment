def Pattern(iNo):
    for iCnt in range(-iNo,iNo+1):
        print(iCnt,end = " ")
        iCnt -= 1
    print(" ")
    
def main():
    
    iValue = int(input("Enter number : "))
    Pattern(iValue)

    
if __name__ =="__main__":
    main()