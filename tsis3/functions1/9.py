def volume_of_a_sphere(r):
    V = (4 * 3,14 * (r * r * r) / 3)
    print(V)
        
r = list(map(int , input().split()))
volume_of_a_sphere(r)