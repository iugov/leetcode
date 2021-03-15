class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        return self.__naive(keyboard, word)
    
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