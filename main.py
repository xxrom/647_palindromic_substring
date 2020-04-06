from typing import List


class Solution:

  def countSubstrings(self, s: str) -> int:
    num = 0
    arr = [0] * len(s)
    for i in range(len(s)):
      arr[i] = [0] * len(s)

    isPalindrom = False
    for i in range(len(s), -1, -1):
      for j in range(i, len(s)):
        isPalindrom = False

        if j == i:
          isPalindrom = True
        elif j - i == 1:
          if s[i] == s[j]:
            isPalindrom = True
        else:  # j - i >= 2
          #            cabbac
          # If abbac |  10010
          #                ^
          #                 \
          # Cabbac   | 100001
          # abba == palindrom =>
          # Cabbac - palindrom if abba - palindrom and
          # first and last Chars are equal!
          if arr[j - 1][i + 1] == 1 and s[i] == s[j]:
            isPalindrom = True

        if isPalindrom == True:
          num += 1
          # Change j and i for correct array printing
          arr[j][i] = 1

    # for i in range(len(s)):
    #   for j in range(len(s)):
    #     print('%s | ' % arr[i][j], end='')
    #   print()

    return num


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
# a 0   0   0   0   1   1   1
# a 0   0   0   0   1   1   1   1
#                   *   #

# # => aAAA если aAAAa = полиндром
# # then => copy from prev
# a => 1
# aa => aAa = True
# aaa => aAAa = True
# aaaa => aAAAa = True
