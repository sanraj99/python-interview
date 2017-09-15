

'''
Create a dictionary of value->index for all index, value pairs in nums. Note that you can have multiple values with different indices. In this case, the highest index will be stored in the dictionary and lower indexes will be overwritten. This behavior can be modified, of course, but I don't believe it needs to be for this problem because part of the problem statement is this: "You may assume that each input would have exactly one solution." Thus, each input has a single unique output so we never have to worry about returning a "wrong-pair" of indices.
Loop through the enumeration of nums, getting i as index, and v as value. Check if target-v is a key in the dictionary we created, and simultaneously assert that the value pointed to by that key is not i. If this is ever true, return the tuple i+1, lookup.get(target-v)+1.

Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

'''

class Solution:
    # # @return a tuple, (index1, index2)
    def twoSum(self,num,target):
        lookup = {}
        for i in range(0,len(num)):
            if target-num[i] in lookup:
                return [lookup[target-num[i]]+1,i+1]
        lookup[num[i]] = i

