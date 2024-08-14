class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N, m, n = len(s3), len(s1), len(s2)
        # Base case: If the lengths of s1 and s2 don't add up to the length of s3, it's not possible to interleave them.
        if m + n != N:
            return False
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        def interleave(i, j):
            # Base case: If we've reached the end of all strings, it's an interleaving.
            if i + j == N and i == m and j == n:
                return True
            # If we've gone past the end of s3, it's not an interleaving.
            elif i + j >= N:
                return False
            # If we've already computed the result for this subproblem, return the cached result.
            elif dp[i][j] != -1:
                return dp[i][j]
            result = False
            # If the current character in s1 matches the current character in s3, try interleaving the rest of s1 and s2.
            if i < m and s1[i] == s3[i + j]:
                result = result or interleave(i + 1, j)
            # If the current character in s2 matches the current character in s3, try interleaving the rest of s1 and s2.
            if j < n and s2[j] == s3[i + j]:
                result = result or interleave(i, j + 1)
            # Cache the result for this subproblem.
            dp[i][j] = result
            return result
        return interleave(0, 0)
solution = Solution()
s1 =input("Enter the first string:")
s2 =input("Enter the second string:")
s3 =input("Enter the third string:")
result = solution.isInterleave(s1, s2, s3)
print("Output is ",result)  
