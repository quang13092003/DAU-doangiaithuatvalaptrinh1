class Solution(object):
    def groupAnagrams(self, strs):
        result = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key not in result:
                result[key] = []

            result[key].append(s)

        return list(result.values())