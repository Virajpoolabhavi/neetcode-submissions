from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        dependency = [0]* numCourses

        for course,pre in prerequisites:
            graph[pre].append(course)

            dependency[course] += 1

        queue = deque()

        order = []

        for i in range(numCourses):
            if dependency[i] == 0:
                queue.append(i)
        
        while queue:
            current = queue.popleft()
            order.append(current)

            for nxt_course in graph[current]:
                dependency[nxt_course] -= 1

                if dependency[nxt_course] == 0:
                    queue.append(nxt_course)
        

        if len(order) != numCourses:
            return []
        else:
            return order







