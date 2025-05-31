def Display(iNo):
    
    for iCnt in range(iNo * 2 ):
        if(iNo > iCnt):
            print(" * ",end =" ")
        else :
            print(" # ",end = " ")
    print(" ")
def main():
    
    iValue = int(input("Enter number : "))
    Display(iValue)

    
if __name__ =="__main__":
    main()