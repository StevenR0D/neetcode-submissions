class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker_s = {}
        tracker_t = {}
        for i in range(len(s)):
            if s[i] not in tracker_s:
                tracker_s[s[i]]=1
            tracker_s[s[i]]+=1
        for j in range(len(t)):
            if t[j] not in tracker_t:
                tracker_t[t[j]]=1
            tracker_t[t[j]]+=1
        return tracker_t==tracker_s