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