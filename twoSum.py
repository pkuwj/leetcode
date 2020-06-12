#方法一
def twoSum(self, nums, target):
        """
        :type nums: 输入一个列表
        :type target: int
        :rtype: 返回一个列表类型
        """
        # j=-1用来判断是否对其作出修改
        j = -1
        # 得到数组的长度，便于接下来进行循环
        lens = len(nums)
        for i in range(lens):
            # 循环这个列表
            if (target - nums[i]) in nums:
                # 排除一种情况：这个结果是num1本身
                if(nums.count(target - nums[i])==1)&(target - nums[i]==nums[i]):
                    continue
                else:
                    # 假设每种输入只有一个答案
                    j = nums.index(target - nums[i],i + 1)
                    break
        if j > 0:
            return [i,j]
        else:
            # 即使没有结果，也要返回空的列表？
            return []
        
#方法二：改进了在整个列表中查找num2的过程，降低了运行时间
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int] 返回一个列表类型
        """
        j=-1
        lens = len(nums)
        for i in range(lens):
            #使用tmp缩短查找列表长度
            tmp = nums[i+1:lens]
            if (target-nums[i]) in tmp:
                j=tmp.index(target-nums[i])+i+1
                break
        if j>0:
            return [i,j]
        else:
            return []
