def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        动态规划的递归解法来解决爬楼梯问题
        爬到第n层楼的方法数量=爬到第n-1层楼的方法数量+爬到第n-2层楼的方法数量
        """
        climb = {}
        climb[0] = 0
        climb[1] = 1
        climb[2] = 2
        # 出错点：range(m,n)的取值为m<=i<n,为左闭右开的区间
        for i in range(3,n+1):
            climb[i] = climb[i - 1] + climb[i - 2]

        return climb[n]
