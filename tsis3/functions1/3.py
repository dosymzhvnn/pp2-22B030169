def solve(numheads , numlegs):
    chickens = int(((4 * numheads) - numlegs)/2)
    rabbits = int(numheads - chickens)
    print("chickens :", chickens)
    print("rabbits :", rabbits)
    
    
numheads = int(input())
numlegs = int(input())
solve(numheads, numlegs)    