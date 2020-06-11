def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int] 返回一个列表类型
        """
        # j=-1用来判断是否对其作出修改
        j = -1
        # 得到数组的长度，便于接下来进行循环
        lens = len(nums)
        for i in range(lens):
            # 循环这个列表
            if (target - nums[i]) in nums:
                if(nums.count(target - nums[i])==1)&(target - nums[i]==nums[i]):
                    continue
                else:
                    # 假设每种输入只有一个答案
                    j = nums.index(target-nums[i],i+1)
                    break
        if j > 0:
            return [i,j]
        else:
            return []
