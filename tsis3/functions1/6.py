def reverse(a):
    i = 0
    for i in range(len(a)):
        print(a[len(a) - i - 1] , end=" ")
        
words = list(map(str , input().split()))
reverse(words)       