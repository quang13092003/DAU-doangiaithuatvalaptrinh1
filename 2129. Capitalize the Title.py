class Solution:
    def capitalizeTitle(self, title):
        words = title.split()
        result = []
        
        for word in words:
            word = word.lower()
            if len(word) <= 2:
                result.append(word)
            else:
                result.append(word.capitalize())
        
        return " ".join(result)