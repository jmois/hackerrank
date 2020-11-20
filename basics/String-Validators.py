if __name__ == '__main__':
    s = raw_input()
    isalnum = False
    for i in s:
        if i.isalnum():
            isalnum = True
            break
    print(isalnum)

    isalpha = False
    for i in s:
        if i.isalpha():
            isalpha = True
            break
    print(isalpha)

    isdigit = False
    for i in s:
        if i.isdigit():
            isdigit = True
            break
    print(isdigit)

    islower = False
    for i in s:
        if i.islower():
            islower = True
            break
    print(islower)

    isupper = False
    for i in s:
        if i.isupper():
            isupper = True
            break
    print(isupper)