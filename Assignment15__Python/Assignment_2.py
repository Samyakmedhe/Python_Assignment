def Pattern(iRows , iColumns):
    
    for i in range(iRows):
        for j in range(iColumns, 0 , -1):
            if i>= j:
                print("#", end ="\t")
            else:
                print("*" ,end= "\t")
            
        print(" ")
    
def main():

    iValue1 = int(input("Enter Rows : "))
    iValue2 = int(input("Enter Coloums : "))
    Pattern(iValue1 , iValue2)

if __name__ == "__main__":
    main()