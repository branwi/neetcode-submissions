class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0] * len(position)
        stack = [] #pos, speed
        for i in range(len(position)):
            stack.append([position[i], speed[i]])
        stack.sort()
        for i in range(len(stack)):
            time[i] = (target - stack[i][0]) / stack[i][1]

        t = time[-1]
        fleet = 1
        for i in range(len(stack) - 2, -1, -1):
            if time[i] > t:
                fleet += 1
                t = time[i]
        return fleet
                
