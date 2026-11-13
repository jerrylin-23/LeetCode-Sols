class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        persons = [i for i in range(n)]
        components = n
        

        def find(person):
            if persons[person] != person:
                persons[person] = find(persons[person])
            return persons[person]
    
        logs.sort()
        
        for timestamp, a, b in logs:
            a = find(a)
            b = find(b)

            if a != b:
                persons[a] = b
                components -= 1

                if components == 1:
                    return timestamp 

        return -1