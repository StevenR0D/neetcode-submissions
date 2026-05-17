class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker_anagram = {}
        for i in range(len(strs)):
            signature_match=sorted(strs[i])
            word=""
            for j in signature_match:
                word += j
            if word in tracker_anagram:
               tracker_anagram[word].append(strs[i])
            else:
                 tracker_anagram[word]= [strs[i]]
        return list(tracker_anagram.values())

