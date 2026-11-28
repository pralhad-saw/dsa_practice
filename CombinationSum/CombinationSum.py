class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        path = []

        def backtrack(index, remaining):

            # Base condition 1: target reached
            if remaining == 0:
                result.append(path.copy())
                return

            # Base condition 2: target exceeded
            if remaining<0 or index == len(candidates):
                return

            # Explore candidates
            for i in range(index, len(candidates)):

                # Choose
                path.append(candidates[i])
                # Explore
                backtrack(i,remaining-candidates[i])
                # Undo
                path.pop()
        backtrack(0, target)

        return result
