def has_duplicates(*nums):
    nums.sort()
    a=1
    for j in nums:
        pnt1= j
        pnt2 = nums[a]
        if pnt1 ==pnt2:
            return True
        else:
            a = a+1
            
    print "No dublicates"
    return nums

lst = [1,2,3,3,6,9]

def has_dupli_cates(lst):
    d = dict()
    for item in lst:
        if item not in d:
            d[item] = 1
        else:
            return True
        return False
        
