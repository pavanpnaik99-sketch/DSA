nums = [7, 11, 15, 2, 2,4]
target = 11

left = 0
right = len(nums) - 1

while left < right:

    sum_ = nums[left] + nums[right]

    if sum_ == target:
        print([left, right])
        break

    elif sum_ > target:
        right -= 1
    else:
        left += 1