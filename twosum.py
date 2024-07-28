"""
EASY LEVEL 
problem statement:
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

"""
class TwoSum:
    """
    takes an array and takes target and then find all pairs of number and cal
    their sum and check whether sum is equal to target or not 

    """
    def __init__(self,array,target):
        self.array=array 
        self.target=target 

    def pair_sum(self):
        if len(self.array)== 0:
            return "empty array "
        # brute force approach to get all the possible pair using nested loop
        for i in range (len(self.array)):
            for j in range (i,len(self.array)):
                # condition check 
                if self.array[i] + self.array[j] == self.target:
                    return i,j 
# obj refrence of class 
array = [2,3,4,8,12,6]
target = 7 
two_S = TwoSum(array,target)
print(two_S.pair_sum())