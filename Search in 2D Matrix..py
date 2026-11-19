
def solution(matrix2D,target):
    m,n = len(matrix2D), len(matrix2D[0])
    left,right=0, (m*n)-1
    while left<= right:
        mid=left+(right-left)//2
        row=mid//n
        col=mid%n
        if matrix2D[row][col]==target:
            return matrix2D[row][col]
        elif matrix2D[row][col]>target:   
            right= mid-1
        else:
            left= mid+1
    return -1
# Complexity: O(log(m × n)) time, O(1) space.
