def histogram(List):
    for number in List:
        print("*" * number)
        
        
L = list(map(int , input().split()))     
histogram(L)   