
def Display(Arr, iLenght ):

    for i in range(iLenght):
        if Arr[i] % 11 == 0:
            print(Arr[i], end= " ")
    
    print()

def main():
    iSize = int(input("Enter number of elements : "))

    Arr = []
    for iCnt in range(iSize):
        iValue = int(input("Enter elments : "))
        Arr.append(iValue)

    Display(Arr , iSize)
   

if __name__ == "__main__":
    main()