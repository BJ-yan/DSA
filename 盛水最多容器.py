"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。
"""

class Solution:
    def maxArea(self, height_list):
        left_index = 0
        right_index = len(height_list) - 1

        max_area = 0
        while left_index != right_index:
            current_area = min(height_list[left_index], height_list[right_index]) * (right_index - left_index)
            # print(f"开始 left:{left_index}, right:{right_index}, list: {height_list[left_index:right_index+1]}, length:{right_index - left_index}, current_area:{current_area} ")
            if current_area > max_area:
                max_area = current_area

            if height_list[left_index] <= height_list[right_index]:
                left_index += 1
            else:
                right_index -= 1

        return (max_area)

if __name__ == "__main__":
    soultion = Solution()
    print(soultion.maxArea([1,8,6,2,5,4,8,3,7]))
