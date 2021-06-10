""" First Solution: Math Concept
2 * (a + b + c) - (a + a + b + b + c) =c """

def singleNumber(nums):
  return 2*sum(set(nums)) - sum(nums)

""" Second Solution: List Operation 
Iterate over all the elements in the list
If some number in the list is new to array, append it
If some number is already in the array, remove it """

 def singleNumber(nums):
       
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()
