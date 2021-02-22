class Backtracking:
    def subsets(self, nums):
        output =[]
        def backtrack(first, curr,k):
            if len(curr) == k:
                output.append(curr[:])
            else:
                for i in range(first, len(nums)):
                    curr.append(nums[i])
                    backtrack(i+1, curr,k)
                    curr.pop()
        for k in range(0, len(nums)+1):
            backtrack(0, [], k)
        return output
obj = Backtracking()
print(obj.subsets([1,2,3]))
    