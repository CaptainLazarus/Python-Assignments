while 1:
    try:
        a,n,d = map(int, input().split()) 

        sum = ((n / 2) * (2 * a + (n - 1) * d))
        print(sum)
        break
    except:
        print("Invalid")