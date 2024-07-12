"Bucket Sort "
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<=1:
            return nums
        count={}
        freq=[[] for i in range(len(nums)+1)]

        for num in nums:
            count[num]=1+count.get(num,0)
        print(count)
        for key,val in count.items():
            freq[val].append(key)
        print

        print(freq)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res


        return []
