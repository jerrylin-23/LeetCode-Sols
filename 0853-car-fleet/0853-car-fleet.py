class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse = True)

        times = [(target - pos) / spd for pos, spd in cars]

        for time in times:
            if not stack or time > stack [-1]:
                stack.append(time)
        return len(stack)
