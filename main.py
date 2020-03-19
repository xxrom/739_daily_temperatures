from typing import List


class Solution:

  def dailyTemperatures(self, T: List[int]) -> List[int]:
    if len(T) == 0:
      return []

    max = T[len(T) - 1]
    ans = [0] * len(T)

    # cycle from end to start
    for i in range(len(T) - 1, -1, -1):
      value = T[i]

      if value < max:
        # index for checking
        nearestIndex = i + 1
        # check next value more then current temperature
        while T[nearestIndex] <= T[i]:
          # !!! the main speed improvement !!!
          # dynamic programming - get ans from previous steps
          nearestIndex += ans[nearestIndex]
        ans[i] = nearestIndex - i

      if value > max:
        max = value

    return ans


my = Solution()
v = [73, 74, 75, 71, 69, 72, 76, 73]  # 0
# v = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]  # 1
# v = [80, 34, 80, 80, 80, 34, 34, 34, 34, 34]  # 2
ans = my.dailyTemperatures(v)
print("ans", ans)

nAns = [1, 1, 4, 2, 1, 1, 0, 0]  # 0
# nAns = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]  # 2

print(ans == nAns)

# Runtime: 468 ms, faster than 98.44% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Daily Temperatures.