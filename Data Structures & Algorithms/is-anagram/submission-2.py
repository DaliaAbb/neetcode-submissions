class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length = len(s)
        length2 = len(t)

        if length != length2:
            return False

        count = {}
        for i, j in zip(s, t):
            count[i] = count.get(i, 0) + 1
            count[j] = count.get(j, 0) - 1
            
        for x in count.values():
            if x != 0:
               return False
        return True

s = "racecar"
t = "carrace"

sol = Solution()
print("both words are anagrams", sol.isAnagram(s,t))

        