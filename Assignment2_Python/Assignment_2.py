
def Display(iNo):
    iCnt = 0
    while iNo > iCnt :
        print(" * ",end=" ")
        iCnt+=1
    print()
   
        
    print()
def main():
    iValue = 0
    print("Enter number :" )
    iValue = int(input())
    Display(iValue)


if __name__== "__main__":
    main()