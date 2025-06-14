def Pattern(iRows , iColumns):
    
    for i in range(1, iRows+1):
        for j in range(1 ,iColumns+1):
            if i == 1  or i == iColumns or j == 1 or j == iColumns:
                print("*", end ="\t")
            else:
                print("@" ,end= "\t")
            
        print(" ")
    
def main():

    iValue1 = int(input("Enter Rows : "))
    iValue2 = int(input("Enter Coloums : "))
    Pattern(iValue1 , iValue2)

if __name__ == "__main__":
    main()