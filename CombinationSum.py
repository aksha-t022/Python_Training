from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # Stop if current number exceeds target
                if candidates[i] > remaining:
                    continue
                
                # Choose the number
                path.append(candidates[i])
                
                # IMPORTANT: use i (not i+1) → reuse allowed
                backtrack(i, path, remaining - candidates[i])
                
                # Backtrack
                path.pop()

        candidates.sort()  # optional but helps pruning
        backtrack(0, [], target)
        return result


# ----------- Example Run -----------
if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7

    sol = Solution()
    answer = sol.combinationSum(candidates, target)

    print("Combinations:", answer)