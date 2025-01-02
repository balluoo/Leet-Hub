class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = lambda w: w[0] in 'aeiou' and w[-1] in 'aeiou'
        words = map(vowels, words)
        pref = list(accumulate(words, initial = 0))
        return [pref[r+1] - pref[l] for l,r in queries] 