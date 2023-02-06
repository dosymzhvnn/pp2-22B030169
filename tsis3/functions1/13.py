import random
def guessthenumber():
    cnt = 0
    n = random.randint(1 , 20)
    # print(n)
    k = 0
    while k == 0:
        number = int(input())
        if number == n:
            print(f"Good job,{name}! You quessed my number in {cnt} quesses! ")
            k += 1
        else:
            cnt += 1
            print(f"Your guess is too law.\nTake a guess.")
            k = 0
 

print(f"What's your name?")
name = str(input())
print(name)
print(f"Well , {name} , I am thinking of a number between 1 and 20.\nTake a quess.")
guessthenumber()
