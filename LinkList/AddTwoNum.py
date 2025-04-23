'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
'''

class ListNode(object):
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next

class Solution:
    def AddTwoNum(self, l1, l2):
        #虚拟头节点
        start = ListNode()
        current = start
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            #计算总和与进位
            total = x + y + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            # 移动链表指针
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return start.next

    def createLinkList(self, listData):
        prevNode = None
        headNode = None

        for i, num in enumerate(listData):
            currentNode = ListNode(num)

            if prevNode != None:
                prevNode.next = currentNode
                prevNode = currentNode
            else:
                prevNode = currentNode

            if headNode == None:
                headNode = currentNode

        return headNode

def main():
    list1 = [2, 4, 3]
    list2 = [5, 6, 4]

    solution = Solution()
    l1 = solution.createLinkList(list1)
    l2 = solution.createLinkList(list2)

    startNode = solution.AddTwoNum(l1, l2)
    resultList = []

    while startNode:
        resultList.append(startNode.val)
        startNode = startNode.next

    print(resultList)

main()