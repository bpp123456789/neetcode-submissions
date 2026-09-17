class Solution:
    mem = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if self.mem.get(n, -1) != -1:
            return self.mem.get(n)
        num = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.mem[n] = num
        return num