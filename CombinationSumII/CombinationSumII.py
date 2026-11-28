class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        path=[]
        candidates.sort()
        def backtrack(index,nums,remaining):
            if remaining==0:
                result.append(path.copy())
                return
            if remaining<0 or index==len(candidates):
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:#prevents dupllicate at same level
                #example if [1,1,1,2]
                #then only [[1,1],[2]] will be result and not [[1,1],[1,1],[1,1],[2]]
                    continue
                if candidate[i]>remaining:
                    break
                path.append(nums[i])
                backtrack(i+1,nums,remaining-nums[i])
                path.pop()


        backtrack(0,candidates,target)
        return result
