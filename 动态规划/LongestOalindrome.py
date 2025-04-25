'''
给你一个字符串 s，找到 s 中最长的 回文 子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"
'''

class Solution:
    def longestPalindrome(self, s):
        stringLength = len(s)

        # 单个字符，肯定是回文串
        if stringLength < 2:
            return s

        maxLen = 1
        begin = 0

        # dp[i][j] 表示s [i, j] 是否是回文串
        # 会生成一个数据结构
        '''
            比如 abc这样的字符串
            [ [false, false, false],
              [false, false, false],
              [false, false, false]
            ]
        '''
        dp = [[False] * stringLength for _ in range(stringLength)]

        for subLength in range(2, stringLength):
            '''
                如输入 babad
                ba 2 bab 3 baba 4 babad 5  ___6
                
                为啥+1？
                因为阔位的时候不会报错
                
                感觉没必要呢
            '''
            for left in range(stringLength):
                '''
                    left 左边界 
                        0, 1, 2, 3, 4
                    right 右边界 = subLength + left - 1 (left + right - 1 = len)
                        1, 2, 3, 4, 5
                '''
                right = subLength + left - 1

                '''
                    回看边界检查，为啥需要这玩意
                    下面“究极处理中”，随着subString的长度边长，没有那么多种了，left往后推几个就没了，及时跳出循环 不然越界
                    也表示着，当前长度的字串已经全部检查完毕
                '''

                if right > stringLength:
                    break
                '''
                    究极处理：
                    在当前长度的子字符串内，一旦出现收尾不相等，就说明不是回文
                    以 babad 为例：生成了一个 5*5的map，
                    [
                        [nil, nil, nil, nil, nil] 
                        [nil, nil, nil, nil, nil]
                        [nil, nil, nil, nil, nil]
                        [nil, nil, nil, nil, nil]
                        [nil, nil, nil, nil, nil]
                    ]
                    ba ab ba ad
                    所以在2长度下，修改的dp的竖向 [0，1] [1, 2] [2, 3] [3, 4]
                    [
                        [T, F, nil, nil, nil]
                        [T, nil, F, nil, nil] 
                        [T, nil, nil, F, nil]
                        [T, nil, nil, nil, F]
                        [T, nil, nil, nil, nil]
                    ]
                    
                    bab aba bad
                    3 长度下，修改的dp [0, 2] [1, 3] [2, 4]
                    [
                        [T, F, T, nil, nil]
                        [T, nil, F, T, nil] 
                        [T, nil, nil, F, F]
                        [T, nil, nil, nil, F]
                        [T, nil, nil, nil, nil]
                    ]
                    
                    baba abad
                    4 长度下，修改的dp [0,3] [1,4]
                    [
                        [T, F, T, F, nil] --- 判断 [0, 3] 就依赖 [1,2] = F
                        [T, nil, F, T, nil] 
                        [T, nil, nil, F, F]
                        [T, nil, nil, nil, F]
                        [T, nil, nil, nil, nil]
                    ]
                    如果相等
                        且总长度属于 2， 3 的不需要进行内部检查了，属于AA ABA形式，必是回文
                        总长度超过3，就需要递归检查
                '''
                if s[left] != s[right]:
                    dp[left][right] = False
                else:
                    if right - left < 3:
                        dp[left][right] = True
                    else:
                        dp[left][right] = dp[left + 1][right - 1]

                # 刷新最长值，储存最长回文内容
                if dp[left][right] == True and right - left + 1 > maxLen:
                    maxLen = right - left + 1
                    beging = left

        return s[begin:begin + maxLen]