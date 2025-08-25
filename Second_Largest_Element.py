class Solution:
    def secondLargestElement(self, arr):
        if len(arr) < 2:
            return None  

        largest = second = float('-inf')

        for x in arr:
            if x > largest:
                second = largest
                largest = x
            elif x > second and x != largest:
                second = x

        
        if second == float('-inf'):
            return None
        return second

s = Solution()

print(s.secondLargestElement([3, 3, 6, 1]))    
print(s.secondLargestElement([10, 20, 4, 45, 99])) 
print(s.secondLargestElement([5, 5, 5]))      
print(s.secondLargestElement([1]))              
