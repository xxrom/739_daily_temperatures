from typing import List


class Solution:

  def getNextValueIndex(self, dictValues: dict, value: int, currentIndex: int,
                        maxValue: int) -> int:
    print(dictValues, maxValue)

    # get maxValue
    nearestIndex = dictValues[maxValue]

    for item in dictValues:
      dictIndex = dictValues[item]

      print('index %d/ value %d' % (dictIndex, item))
      if item > value and dictIndex < nearestIndex:
        nearestIndex = dictIndex

    return nearestIndex - currentIndex

  def dailyTemperatures(self, temp: List[int]) -> List[int]:
    # print(temp)

    dictValues = {}
    min = temp[len(temp) - 1] if len(temp) > 0 else None
    max = temp[len(temp) - 1] if len(temp) > 0 else None
    if min != None:
      dictValues[min] = len(temp) - 1

    ans = []
    for i in range(len(temp) - 1, -1, -1):

      value = temp[i]
      if value < max:
        ans.append(self.getNextValueIndex(dictValues, value, i, max))
      else:
        ans.append(0)

      if value < min:
        min = value
      if value > max:
        max = value

      dictValues[value] = i

    ans.reverse()
    return ans


my = Solution()
# v = [73, 74, 75, 71, 69, 72, 76, 73]  # 0
# v = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]  # 1
v = [80, 34, 80, 80, 80, 34, 34, 34, 34, 34]  # 1
ans = my.dailyTemperatures(v)
print("ans", ans)

# nAns = [1, 1, 4, 2, 1, 1, 0, 0]  # 0
nAns = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]  # 1

print(ans == nAns)
