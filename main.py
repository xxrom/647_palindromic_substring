from typing import List


class Solution:

  def checkIfPolindrom(self, checkStr: str, start: int, end: int) -> bool:
    middle = (end - start) / 2
    i = 0
    # print('check %s' % checkStr)

    while i <= middle:
      # print('%s === %s' % (checkStr[start + i], checkStr[end - i]))
      if checkStr[start + i] != checkStr[end - i]:
        return False
      i += 1

    return True

  def countSubstrings(self, s: str) -> int:
    # ans = []
    num = 0

    # print('str %s' % s)

    # print(self.checkIfPolindrom('abba', 0, 3))

    # arr = [0] * len(s)
    # for i in range(len(s)):
    #   arr[i] = [0] * len(s)
    # print(arr[i])
    # for j in range(len(s)):
    #   arr[i][j] = 'i= %d, j= %d' % (i, j)

    # for i in range(len(s)):
    #   for j in range(len(s)):
    #     print('%s | ' % arr[i][j], end='')
    #   print()

    # print('____________')
    for i in range(len(s)):
      for j in range(i, len(s)):
        # print(arr[i][j])
        if self.checkIfPolindrom(s, i, j) == True:
          # print('TRUE = %s' % s[i:j + 1])
          num += 1
          # ans.append(s[i:j + 1])

    # print('ans', ans)
    return num
    # return len(ans)


my = Solution()
n = 'abc'
# n = 'abba'

n = 'abccbe'
# n = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
ans = my.countSubstrings(n)
print("ans", ans)

# abba
# a b b a bb abba

#     a   b   b   a
#   a 1
#   b 0   1
#   b 0   1   1
#   a 1   0   0   1

# abccbe
# a b c c b e bccb cc

#   a   b   c   c   b   e
# a 1
# b 0   1
# c 0   0   1
# c 0   0   1   1
# b 0   1   0   0   1
# e 0   0   0   0   0   1


# ababaaaa

#   a   b   a   b   a   a   a   a
# a 1
# b 0   1
# a 1   0   1
# b 0   1   0   1
# a 1   0   1   0   1
# a 0   0   0   0   1   1
# a 0   0   0   0   1   1
# a 0   0   0   0   1   1
#                   *   #

# # => aAAA если aAAAa = полиндром
# # then => copy from prev
# a => 1
# aa => aAa = True
# aaa => aAAa = True
# aaaa => aAAAa = True
