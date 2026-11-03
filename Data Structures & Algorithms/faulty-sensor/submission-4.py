class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        n = len(sensor1)
        l = 0
        while l < n and sensor1[l] == sensor2[l]:
            l += 1
        
        if l == n:
            return -1
        
        first = True
        second = True
        for i in range(l, n - 1):
            if sensor1[i] != sensor2[i + 1]:
                first = False
        for i in range(l, n - 1):
            if sensor1[i + 1] != sensor2[i]:
                second = False
        
        return (1 if first else 2) if first != second else -1
