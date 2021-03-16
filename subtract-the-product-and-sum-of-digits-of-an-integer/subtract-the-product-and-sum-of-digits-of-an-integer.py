class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        _product = 1
        _sum = 0

        while n > 0:
            last_digit = n % 10
            _product *= last_digit
            _sum += last_digit
            n //= 10
        
        return _product - _sum