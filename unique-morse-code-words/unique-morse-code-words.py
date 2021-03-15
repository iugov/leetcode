from string import ascii_lowercase


morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return self.__naive(words)

    def __naive(self, words: List[str]) -> int:
        """
        Time: O(n^2)
        Space: O(n)
        """
        morse_encoding = {k: v for k, v in zip(ascii_lowercase, morse)}
        return len(set(''.join(morse_encoding[c] for c in word) for word in words))
