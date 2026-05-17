class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] +=1
        counter_sorted=sorted(counter.items(), key=lambda pair: pair[1], reverse=True)
        final = []
        x=0
        while x<k:
            final.append(counter_sorted[x][0])
            x+=1
        return final
        