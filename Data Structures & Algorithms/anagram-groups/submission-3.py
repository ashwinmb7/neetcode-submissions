class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        grouped_list = []

        for s in strs:
            ##create a key for each str
            key = "".join(sorted(s))

            my_dict[key].append(s)
        

        return list(my_dict.values())