# Largest Element in an Array
class Solution:
    def largestElement(self, arr):
        
        best = arr[0]

        for x in arr[1:]:
            if x > best:
                best = x
        return best



s = Solution()


arr = [1,2,3,4,5,6,7,8,9,10]


print(s.largestElement(arr))

