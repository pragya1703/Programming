def possiblePath(arr, i,j, x,y):
    def findPath(arr, i, j, x, y):
        print(i, j, x, y, arr[x][y])
        if i ==x and  j == y:
            return True
        else:
            n = [[0,1],[1,0],[0,-1],[-1,0]]
            for a in n:
                dx = i+a[0]
                dy = j+a[1]
                print(i,j,"-",dx, dy)
                if 0<=dx<len(arr) and 0<=dy<len(arr[0]) and arr[dx][dy]==0:
                    arr[dx][dy] = "#"
                    val = findPath(arr, dx, dy, x, y)
                    arr[dx][dy] = 0
                    print(val)
                    return val
            return False
    return findPath(arr, i, j, x, y)
arr = [[0,0,0],
       [0,1,0],
       [1,0,0],
       [0,0,0]]
print(possiblePath(arr,3,1,0,0))


