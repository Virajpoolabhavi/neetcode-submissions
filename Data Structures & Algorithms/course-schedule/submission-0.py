from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]

        dependency = [0] * numCourses

        for course,pre in prerequisites:
            graph[pre].append(course)
            dependency[course] += 1
        
        queue = deque()
        completed = 0

        for course in range(numCourses):
            if dependency[course] == 0:
                queue.append(course)
        
        while queue:
            current = queue.popleft()
            completed += 1

            for nxt_course in graph[current]:
                dependency[nxt_course] -= 1 

                if dependency[nxt_course] == 0:
                    queue.append(nxt_course)
            
        return completed == numCourses


        