while 1:
    try:
        print("even") if int(input())%2 == 0 else print("odd")
    except:
        print("Invalid")