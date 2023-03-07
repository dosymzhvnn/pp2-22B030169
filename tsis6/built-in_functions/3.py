def palindrome(str):
    s = ''.join(reversed(str))
    if str == s:
        print("Is palindrome")
    else:
        print("Is not palindrome")
        
        
string = input()
palindrome(string)