    number = int(input("Enter the number:- "))
    z = 0
    while number != 0:
        temp = number % 10
        if number // 10 == 0:
            z += temp
        else:
            z += temp * 10 ** (len(str(number // 10)))
        number = number // 10

    print(z)


