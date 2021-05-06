def search(nums, target):
    first=0
    last=len(nums)-1
    while first <= last:
        mid = (first+last)//2
        if nums[mid]== target:
            return mid
        elif target<nums[mid]:
                last=mid - 1
        else:
            first=mid + 1
    return mid
 
numList=[5,35,78,79,125,182,364,640]
tar=5
print(search(numList, tar))