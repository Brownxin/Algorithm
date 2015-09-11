class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        max=0
        length_A=len(A)
        length_B=len(B)

        for i in range(length_A):
            for j in range(length_B):
                temp_length=0
                while (i+temp_length<length_A) and (j+temp_length<length_B) and (A[i+temp_length]==B[j+temp_length]):
                    temp_length+=1

                if max<temp_length:
                    max=temp_length

        return max

A="www.lintcode.com code"
B="www.ninechapter.com code"

so=Solution().longestCommonSubstring(A,B)
print(so)