from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # använder count för att räkna:
        counter = Counter(nums)
        length = len(nums)

        buckets = [[] for _ in range(length + 1)]
         # från 0 då ett tal kan förekomma 0 ggr
        for num, freq in counter.items():
                buckets[freq].append(num) 
        # go backward through the list to get what we want        
        ret = []
        for i in range(length, -1,-1):
            if buckets[i] != 0: # if it is list
                ret.extend(buckets[i]) # we extend the list (picking up all things in the list)
            if len(ret) == k: 
                break
        return ret



        

    
numbers = [1,2,2,3,3,3]
sol = Solution()
print(sol.topKFrequent(numbers, 2))


            
        