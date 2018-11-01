while 1:
    try:
        def reverse(s): 
            return s[::-1] 
    
        def isPalindrome(s): 
            rev = reverse(s) 
            if (s == rev): 
                return True
            return False
            
        s = input()
        ans = isPalindrome(s) 
        if ans == 1: 
            print("Is palindrome") 
        else: 
            print("Is not palindrome") 
        break
    except:
        print("invalid")