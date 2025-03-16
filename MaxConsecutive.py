def consecutive(nums:list[int]):
    numsSet=set(nums)
    longest=0
    for num in numsSet:
        if num-1 not in numsSet:
            length=1
            currentEle=num
            while currentEle+1 in numsSet:
                length+=1
                currentEle+=1
            longest=max(length,longest)
    return longest

# ex [1,2,3,4] in [1,2,3,42,7,5,37]
