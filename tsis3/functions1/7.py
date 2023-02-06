def has_33(nums):
  
    for i in range(len(nums) - 1):
        cnt = 0    
        if(nums[i] == 3 and nums[i] == nums[i+1]):
            cnt += 1
        else:
            continue
        
        if cnt > 0 :
            print("True")
        else: 
            print("False")
        
                  
n = list(map(int , input().split()))
has_33(n)       