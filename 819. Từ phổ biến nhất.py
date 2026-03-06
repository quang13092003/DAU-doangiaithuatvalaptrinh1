class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banned = set(banned)
        
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
            
        words = paragraph.lower().split()
        
        count = {}
        
        for word in words:
            if word not in banned:
                count[word] = count.get(word, 0) + 1
        
        return max(count, key=count.get)
        