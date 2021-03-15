class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        return self.__cool_trick(keyboard, word)
    
    def __cool_trick(self, keyboard: str, word: str) -> int:
        """
        Time: O(len(word))
        Space: O(n)
        """
        letterarr = [0] * 26
        for i, value in enumerate(keyboard):
            letterarr[ord(value) - ord('a')] = i
        
        result = 0
        move_from = 0
        for c in word:
            move_to = letterarr[ord(c) - ord('a')]
            result += abs(move_from - move_to)
            move_from = move_to
        return result
        
    
    def __dictn(self, keyboard: str, word: str) -> int:
        """
        Time: O(len(word))
        Space: O(n)
        """
        lettermap = {letter: i for i, letter in enumerate(keyboard)}
        result = 0
        move_from = 0
        for c in word:
            move_to = lettermap[c]
            result += abs(move_from - move_to)
            move_from = move_to
        return result
    
    def __naive(self, keyboard: str, word: str) -> int:
        """
        Time: O(len(word) * len(keyboard))
        Space: O(1)
        """
        result = 0
        move_from = 0
        for c in word:
            move_to = keyboard.index(c)
            result += abs(move_from - move_to)
            move_from = move_to
        return result
