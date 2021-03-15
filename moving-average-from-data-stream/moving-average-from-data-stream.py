from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.stream = deque()

    def next(self, val: int) -> float:
        self.stream.append(val)
        
        if len(self.stream) > self.size:
            self.stream.popleft()

        return sum(self.stream) / len(self.stream)
