#complexity is same as kahn's algorithm
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            
        # 0 = unvisited, 1 = visiting (in current path), 2 = safe (completely checked)
        state = [0] * numCourses
        
        def has_cycle(course: int) -> bool:
            if state[course] == 1:  # Hit a node currently in our active recursion stack!
                return True
            if state[course] == 2:  # Already verified safe, no need to re-check
                return False
                
            state[course] = 1  # Mark as currently visiting
            
            for next_course in adj[course]:
                if has_cycle(next_course):
                    return True
                    
            state[course] = 2  # All paths from here are safe!
            return False
            
        # Check every course (handles disconnected graph components)
        for c in range(numCourses):
            if has_cycle(c):
                return False
                
        return True

