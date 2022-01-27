class Solution:
    def maxArea1(self, height: List[int]) -> int:
        output = 0
        size = len(height)
        for i, h1 in enumerate(height):
            for j in range(1, size):
                area = min(h1, height[j])*(j-i)
                output = max(area, output)
        return output
    
    
    def maxArea(self, height: List[int]) -> int:
        output = 0
        l = 0
        r = len(height) - 1
        N = len(height)
        while(l < r):
                area = min(height[l], height[r])*(r-l)
                output = max(area, output)
                if height[l] < height[r]:
                    l += 1
                else:
                    r -=1
        return output
                
            
        