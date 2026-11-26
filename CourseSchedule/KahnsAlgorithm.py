
"""
The Easiest Approach: Kahn's Algorithm (BFS)

Think of this like peeling an onion from the outside in—you can only take courses that currently have 0 prerequisites:
1. Build the Graph: Populate adj and count the indegree for every course.
2. Find Starting Courses: Push all courses with indegree == 0 into a queue (collections.deque).
3. Process Queue: Pop a course, increment a taken counter, and reduce the indegree of all its neighboring courses by 1. If any neighbor's indegree drops to 0, add it to the queue.
4. Check for Cycles: If taken == numCourses, every course was unlocked (no cycles) → return True. If taken < numCourses, some courses remained stuck in a cycle → return False.

3. Quick Example

Suppose numCourses = 2 and prerequisites = [[1, 0]] (to take 1, you must take 0 first):
• indegree starts as [0, 1] (Course 0 needs 0 prereqs; Course 1 needs 1 prereq).
• Course 0 starts in the queue. When you take 0, Course 1's indegree drops from 1 to 0, so 1 enters the queue.
• Both courses get taken (taken == 2), returning True.


Example

Suppose numCourses = 2 and prerequisites = [[1, 0]] (to take 1, you must take 0 first):
• indegree starts as [0, 1] (Course 0 needs 0 prereqs; Course 1 needs 1 prereq).
• Course 0 starts in the queue. When you take 0, Course 1's indegree drops from 1 to 0, so 1 enters the queue.
• Both courses get taken (taken == 2), returning True.
"""
