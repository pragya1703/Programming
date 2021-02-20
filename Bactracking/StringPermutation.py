"""
Using Backtracking to solve string Permutation
                               "abc"
                              /  |  \
                             /   |   \
                    "{a}bc"    "{b}ac"  "{c}ba"
                      /\        /\            / \
                     /  \      /  \          /   \
              "a{b}c" "a{c}b""b{a}c""b{c}a" "c{b}a 
{}-indicates start  which is fixed position and elements before it don't change for current level
"""
def StringPermutation(str):
    result = []
    def permutate(str, start, end):
        if start==end:
            result.append(''.join(str))
        else:
            for i in range(start, end+1):
                #Swapping start with the element at current index i
                str[start], str[i] = str[i], str[start]
                #Calling permute for the subset of the string
                permutate(str, start+1, end)
                #Swapping the element at index i to it's original position backtracking
                str[start], str[i] = str[i], str[start]
    permutate(str, 0, len(str)-1)
    return result
print(StringPermutation([i for i in "abc"]))

#Output: ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']




