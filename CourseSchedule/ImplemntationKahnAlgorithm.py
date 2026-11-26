#self implementation

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        #followup couses after finishing courses at this position
        adj=[[] for i in range(numCourses)]
        indegree = [0] *  numCourses
               
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
            
        #indegree is number of locks for unlocking that course
        queue =deque([i for i in range(numCourses) if indegree[i]==0]) #if lock 0 then popable
        courses_taken=0
        while queue:
            curCourse = queue.popleft()
            courses_taken+=1
            for nextCourses in adj[curCourse]:
                indegree[nextCourses]-=1
                if indegree[nextCourses]==0:
                    queue.append(nextCourses)
        return courses_taken == numCourses
