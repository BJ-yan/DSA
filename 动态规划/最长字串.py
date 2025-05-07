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
        result_list = []
        maxLength = 0

        leftIndex = 0
        rightIndex = 0

        for leftIndex in range(0, len(s)):
            print(f"left{leftIndex}")
            if leftIndex < rightIndex:
                leftIndex += 1
            while rightIndex <= len(s) - 1 and (s[rightIndex] not in result_list):
                result_list.append(s[rightIndex])
                print(f"right{rightIndex}, result_list {result_list}")
                rightIndex += 1

            if len(result_list) > maxLength:
                maxLength = len(result_list)
            result_list.pop(0)
            print(f"left {leftIndex} right{rightIndex}, result_list {result_list}")

        return maxLength


if __name__ == "__main__":
    string = "pwwkew"
    solution = Solution()
    print(solution.lengthOfLongestSubString(string))