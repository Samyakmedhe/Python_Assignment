
def MultiDisplay(iNo):  
    for iCnt in range(1,iNo+2):
        print(iCnt*iNo)
def main():
    iValue = 0
    print("Enter number : ",end=' ')
    iValue = int(input())
    MultiDisplay(iValue)
    
if __name__== "__main__":
    main()