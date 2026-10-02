from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_strs = list(set(["".join(sorted(s)) for s in strs]))

        str_map = defaultdict(list)

        for s in sort_strs:
            str_map[s] = []


        for s in strs:
            str_map["".join(sorted(s))].append(s)
        
        str_map = dict(str_map)
        op_list = list()

        for s in str_map.values():
            op_list.append(s)

        return op_list
            