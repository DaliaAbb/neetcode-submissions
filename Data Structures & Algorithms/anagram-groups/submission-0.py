class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_list = {} # lista vi kan lägga in våran anagram
        for words in strs: # gå igenom listan ord för ord
            count = [0]*26 # skapa en count lista med nollor (pos för varje bokstav)
            for l in words:  # gå igenom varje bokstav i ordet
                pos = ord(l)-ord('a') # kolla vilka bosktäver den har
                count[pos] += 1
            key = tuple(count) # lägg till ordet i en tuple
        
            if key not in group_list: # om ordet ej finns i listan, skapa en lista med nya ordet
                group_list[key] = [words]
            else:
                group_list[key].append(words) # om det finns, bara lägg till i existerade lista
        return list(group_list.values())


strs = ["act","pots","tops","cat","stop","hat"]
sol = Solution()
print(sol.groupAnagrams(strs))