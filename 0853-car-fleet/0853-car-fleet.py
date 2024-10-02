class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time = [(target - position[i]) / speed[i] for i in range(len(position))]

        car =  sorted(zip(position, time), reverse= True, key=lambda x:x[0])
        stack = []
        

        for position, time in car:

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)