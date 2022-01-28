#link: https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target < nums[mid]:
                if nums[mid] > nums[left]:
                    """
                    If the smallest is on the right side of mid
                    caused by a possible rotate.
                    """
                    if target > nums[left]:
                        """
                        nums[left] < target < nums[mid],
						since smallest in the right side,
						it's a perfect interval (non-decreasing).
                        """
                        right = mid - 1
                    elif target == nums[left]:
                        return left
                    else:
                        """
                        Target possibly on the second half of 
                        the right part.
                        """
                        left = mid + 1
                elif nums[mid] < nums[left]:
                    """
                    Smallest on the left side inclusively,
                    so if target is less than, it is only
                    possible on the left.
                    """
                    right = mid - 1
                else:
                    """If and only if there are only one
                    or two items in the range.  In which case
					check the next or terminate while loop."""
                    left += 1
            elif target > nums[mid]:
                if nums[mid] < nums[left]:
                    """Smallest on the left inclusively."""
                    if target > nums[right]:
                        """Since smallest on the left, leaving
                        the right part non decreasing. So if 
                        greater, must only possible on the
                        first part of the left."""
                        right = mid - 1
                    elif target == nums[right]:
                        return right
                    else:
                        """
						 nums[mid] < target < nums[right],
						since smallest in the left side,
						it's a perfect interval (non-decreasing).
                        """
                        left = mid + 1
                elif nums[mid] > nums[left]:
                    """
                    Smallest on the right = left part non-decreasing,
                    therefore if target greater than mid, must be in 
                    the first part of right if exists.
                    """
                    left = mid + 1
                else:
                    """If and only if there are only one
                    or two items in the range. In which case
					check the next or terminate while loop."""
                    left += 1
            else:  # target == nums[mid]:
                return mid
        
        return -1