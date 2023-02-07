def is_palindrome(s):
    cnt = 0
    if (len(s) % 2) != 0:
        for i in range(int(len(s)+1 / 2)):
            if s[i] == s[len(s) - i - 1]:
                cnt += 1
            else:
                continue
            if cnt == int((len(s)+1)/2):
                            print("YES")
            else:
                            print("NO") 
    else:
        print("NO") 
            
s = list(map(str , input().split()))
is_palindrome(s)             
        