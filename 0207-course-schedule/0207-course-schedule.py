class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        my_dict = {i: [] for i in range(numCourses)}


        for course, prereq in prerequisites:
            my_dict[prereq].append(course)

        visited = set()
        in_rec_stack = set()

        def dfs(course):
            if course in in_rec_stack:
                return False
            if course in visited:
                return True

            in_rec_stack.add(course)
            

            for neighbor in my_dict[course]:
                if not dfs(neighbor):
                    return False
            
            in_rec_stack.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True