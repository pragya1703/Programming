"""
                                          [2,3,6,7]
                                       /             
                                      /              
                                      [2]            
                                /     |     \    \   
                               /      |      \    \
                            [2,2]    [2,3] [2,6]   [2,7]
                            /    \      /   >7      >7
                           /      \    /
                    [2,2,2] #[2,2,3]# [2,2,3]
                    /   \             >7
                   /     \
            [2,2,2,2]     [2,2,2,3] 
                 >7             >7

Recursion Tree only for element 2  similar will be followed for 3,6,7
There is loop running from current element till end
which appends the current element and calls the function findSum with appending currelemt to list and range current element till end
once the curValreaches 0 it appends list to result and returns to curr base func and pops the last element i.e backtracking
or if curVal < 0 it returns to curr base func and pops the last element
finally it returns result


Time Complexity Analysis
Let's suppose we have n-array tree
Time complexity to visit each node = No. of node
No. of nodes of n-array tree given height
O(n power(h+1) - 1)
Hence time complexity will be O(n^(h+1)-1)
"""




def CombinationSum(arr, target):
    result = []
    def findSum(currVal, currSet, start, end):
        if currVal == 0:
            result.append(currSet[:])
            # got the value, stop exploration
            return
        elif currVal<0:
            # exceed the scope, stop exploration
            return
        else:
            for i in range(start, end):
                #Add number to currSet
                currSet.append(arr[i])
                 # give the current number another chance, rather than moving on
                findSum(currVal-arr[i], currSet, i, end)
                #Backtrack, remove number from currSet
                currSet.pop()
    findSum(target, [], 0, len(arr))
    return result
print(CombinationSum([2,3,6,7], 7))
#Output: [[2, 2, 3], [7]]



#Second case when arr contains repeated elements

def combinationSum2(arr, target):
            result = []
            elem = -1
            arr = sorted(arr)
            def findSum(currVal, currSet, start, end):
                nonlocal elem
                if currVal == 0:
                    result.append(currSet[:])
                    return
                elif currVal<0:
                    return
                else:
                    for i in range(start, end):
                        if arr[i] == elem:
                            continue
                        currSet.append(arr[i])
                        findSum(currVal-arr[i], currSet, i+1, end)
                        elem = currSet.pop()
            findSum(target, [], 0, len(arr))
            return (result)

print(combinationSum2([10,1,2,7,6,1,5], 8))
#Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]