class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        stack = []

        for component in components:
            if component == ".." and stack:
                    stack.pop()
            elif component not in ["", ".", ".."]:
                stack.append(component)
            
            simplified_path = "/" + "/".join(stack)

        return simplified_path