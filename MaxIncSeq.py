class Solution:
    def LIS(self, nums):
        LIS = [1]*len(nums)
        for i in range(len(nums),-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS[i]= max(LIS[i],LIS[j]+1)
        print(LIS)
        return max(LIS)
sol = Solution()
nums = [int(num) for num in input("Enter the element of array :").split(",")]
print("Largest increasing sequence :",sol.LIS(nums))