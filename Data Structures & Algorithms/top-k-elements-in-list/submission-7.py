class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        my_dict = {}

        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1
        

        for num in my_dict.keys():
            heapq.heappush(min_heap, (my_dict[num], num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        

        return [num for freq, num in min_heap]