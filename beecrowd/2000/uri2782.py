n = int(input())
nums = list(map(int,input().split()))

c = 1
for i in range(2, n):
    if nums[i] - nums[i-1] != nums[i-1] - nums[i-2]:
        c += 1

print(c)