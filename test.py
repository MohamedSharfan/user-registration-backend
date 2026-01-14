
def build_prefix_sum(nums):
    p = [0]*(len(nums)+1)

    for i in range(len(nums)):
        p[i + 1] = p[i] + nums[i]
    return p 

def range_sum(p,i,j):
    summ = p[j+1] - p[i]
    return summ

def get_final_array(diff):
    out = build_prefix_sum(diff)
    return out
 


total = sum(nums)
leftsum = 0

for i in range(len(nums)+1):
    rightsum = total - leftsum - nums[i] 
    if leftsum == rightsum:
        return i 
    leftsum += nums[i]
return -1