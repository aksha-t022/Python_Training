from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to handle duplicates
        result = []

        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Stop if current number exceeds remaining target
                if candidates[i] > remaining:
                    break
                
                # Choose the number
                path.append(candidates[i])
                
                # Move to next index (i + 1 → element used only once)
                backtrack(i + 1, path, remaining - candidates[i])
                
                # Backtrack
                path.pop()

        backtrack(0, [], target)
        return result


# ----------- Example Run -----------
if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    sol = Solution()
    answer = sol.combinationSum2(candidates, target)

    print("Combinations:", answer)