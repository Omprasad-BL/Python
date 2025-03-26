# solution for possible subset for 2 power
def subsets(nums):
    res=[]
    subset=[]
    def dfs(i):
        if i>=len(nums):
            subset.append(nums[i])
            return
        # inlcude element
        subset.append(nums[i])
        dfs(i+1)

        # exclude element
        subset.pop()
        dfs(i+1)

    dfs(0)
    return res