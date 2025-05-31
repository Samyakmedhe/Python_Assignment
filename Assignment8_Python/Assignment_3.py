



def KMtoMeter(iNo):

    Meter = iNo * 1000

    return Meter
def main():

    iValue = int(input("Enter Distance : "))
    iRet = KMtoMeter(iValue)

    print("Meters is : ",iRet)


if __name__ == "__main__":
    main()