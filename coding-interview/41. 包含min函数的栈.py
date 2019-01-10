'''
设计一个支持push，pop，top等操作并且可以在O(1)时间内检索出最小元素的堆栈。

push(x)–将元素x插入栈中
pop()–移除栈顶元素
top()–得到栈顶元素
getMin()–得到栈中最小元素
样例
MinStack minStack = new MinStack();
minStack.push(-1);
minStack.push(3);
minStack.push(-4);
minStack.getMin();   --> Returns -4.
minStack.pop();
minStack.top();      --> Returns 3.
minStack.getMin();   --> Returns -1.
'''


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min_s = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.s.append(x)

        t = len(self.min_s) - 1
        self.min_s.append(x)
        while t >= 0 and x > self.min_s[t]:
            self.min_s[t + 1] = self.min_s[t]
            t -= 1
        self.min_s[t + 1] = x

    def pop(self):
        """
        :rtype: void
        """
        t = self.s[-1]
        self.s = self.s[:-1]

        l = len(self.min_s) - 1
        while l >= 0 and self.min_s[l] != t:
            l -= 1
        self.min_s = self.min_s[:l] + self.min_s[l + 1:]

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_s[-1]


        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()

'''
栈+插入排序
应用到栈的知识，要想O(1)时间复杂度得到最小值，需要另外开辟一个栈顶为最小值有序栈，这就用到插入排序的知识了。
'''