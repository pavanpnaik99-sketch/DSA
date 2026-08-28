# Running sum of 1d array

def Running(nums):
    ans = []

    ans.append(nums[0])

    for i in range(1, len(nums)):
        x = ans[i - 1] + nums[i]
        ans.append(x)

    return ans

print(Running([1, 2, 3, 4]))