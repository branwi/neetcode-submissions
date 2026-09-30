class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []  # [position, speed]

        for i in range(len(position)):
            stack.append([position[i], speed[i]])

        stack.sort()

        fleets = []

        # Start with the car closest to the target
        for i in range(len(stack) - 1, -1, -1):
            pos = stack[i][0]
            spee = stack[i][1]

            time = (target - pos) / spee

            # If this car cannot catch the fleet ahead,
            # it creates a new fleet
            if not fleets or time > fleets[-1]:
                fleets.append(time)

        return len(fleets)