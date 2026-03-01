n,s = map(int,input().split())
nums = list(map(int,input().split()))

left = 0
curr = 0
count = 0

for right in range(len(nums)):
    curr += nums[right]

    while curr > s and left < right:
        curr -= nums[left]
        left += 1

    count += right - left + 1

print(count)
    