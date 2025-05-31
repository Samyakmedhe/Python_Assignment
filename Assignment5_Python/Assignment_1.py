def Pattern(iNo):
    for iCnt in range(iNo):
        print(" *  $",end = " ")
    
    
def main():
    
    iValue = int(input("Enter number : "))
    Pattern(iValue)

    
if __name__ =="__main__":
    main()