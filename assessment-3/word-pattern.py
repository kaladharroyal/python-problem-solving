# ✅ Question 1 (Easy) – Word Pattern

# Problem:
# Given a pattern string and a sentence s, check whether s follows the same pattern.

# Key idea:

# One-to-one (bijection) mapping between pattern letters and words

# Same letter → same word

# Different letters → different words

# Example:

# abba + dog cat cat dog → true

# abba + dog cat cat fish → false


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        p_to_w = {}
        w_to_p = {}
        
        for p, w in zip(pattern, words):
            if p in p_to_w and p_to_w[p] != w:
                return False
            if w in w_to_p and w_to_p[w] != p:
                return False
            
            p_to_w[p] = w
            w_to_p[w] = p
        
        return True


Solution.wordPattern("abba", "dog cat cat dog")