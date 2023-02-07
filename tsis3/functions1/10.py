def to_unique(list):
    uniq_list = []
    for x in list:
        if x not in uniq_list:
            uniq_list.append(x)
        else:
            continue
        
          
    print(uniq_list)       


list = list(map(int , input().split()))
to_unique(list)