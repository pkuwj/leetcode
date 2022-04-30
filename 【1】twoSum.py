class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_list = dict()
        for i,num in enumerate(nums):
            # 此处查找字典没有时间复杂度么？
            # python的机制查找词典和集合没有时间复杂度，查找列表时间复杂度是O(n),因为列表的的元素可以是不同类型的，
            # 不同类型的元素存在不连续的地址上，所以列表存储的是地址，需要遍历每一个地址进行查找
            if target-num in hash_list:
                return [hash_list[target-num], i]
            hash_list[num]=i
        return []
