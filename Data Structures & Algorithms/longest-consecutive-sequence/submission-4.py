class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        longest = 1
        my_set = set()

        for num in nums:
            my_set.add(num)
        

        ##[2,20,4,10,3,5]

        sorted_list = sorted(my_set)

        if not sorted_list:
            return 0

        ##[2,3,4,5,10,20]
        print(sorted_list)

        for i in range(1, len(sorted_list)):
            if sorted_list[i] == sorted_list[i-1] + 1:
                count += 1
            
            else:
                count = 1
            

            longest = max(longest, count)
            



        

        return longest

