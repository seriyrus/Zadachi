m = int(input())
n = int(input())

nums = []

usl_T = {0:(0,0)}

for i in range(n):
    nums.append(int(input()))

for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if (nums[i] + nums[j]) % m == 0:
            usl_T[nums[i] * nums[j]] = (nums[i], nums[j])

print(usl_T[max(usl_T.keys())][0], usl_T[max(usl_T.keys())][1])