
def SquareMeter(iNo):

    Meter = iNo * 0.0929

    return Meter
def main():

    iValue = int(input("Enter area in Square feet : "))
    dRet = SquareMeter(iValue)

    print("Square meter is : ",dRet)


if __name__ == "__main__":
    main()