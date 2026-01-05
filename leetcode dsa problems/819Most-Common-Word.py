class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        # Convert the paragraph to lowercase to make comparison case-insensitive
        paragraph = paragraph.lower()

        # Remove punctuation by replacing them with spaces
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        # Convert banned list to a set for fast lookup
        banned = set(banned)

        # Dictionary to store frequency of each valid word
        freq = {}

        # Split paragraph into words and iterate through them
        for word in paragraph.split():

            # Count only words that are not banned
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1

        # Return the word with the maximum frequency
        return max(freq, key=freq.get)
Solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])