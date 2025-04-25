'''
给定一个字符串s ，请你找出其中不含有重复字符的最长子串的长度

示例
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是"abc"，所以其长度为3。

示例
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是"b"，所以其长度为1。

示例
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为3。请注意，你的答案必须是子串的长度，"pwke"是一个子序列，不是子串。
'''

class Solution(object):
    def lengthOfLongestSubString(self, s):
        charList = []
        max = 0
        for char in s:
            print(charList, char, charList.count(char) )
            while charList.count(char) >= 1:
                charList.pop(0)
                print("____", charList)
            charList.append(char)

            if len(charList) > max:
                max = len(charList)

        return max
def main():
    string = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubString(string))

if __name__ == "__main__":
    main()