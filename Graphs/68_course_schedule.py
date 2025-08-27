from collections import deque
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
     # Build adjacency list and calculate in-degrees
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Initialize queue with courses having no prerequisites
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        # Process courses level by level
        courses_processed = 0
        
        while queue:
            # Take a course with no remaining prerequisites
            current_course = queue.popleft()
            courses_processed += 1
            
            # Remove this course and update dependent courses
            for dependent_course in graph[current_course]:
                in_degree[dependent_course] -= 1
                
                # If dependent course has no more prerequisites, add to queue
                if in_degree[dependent_course] == 0:
                    queue.append(dependent_course)
        
        # If we processed all courses, no cycle exists
        return courses_processed == numCourses

    # if not prerequisites:
    #     return True
    # course_map = {i: [] for i, _ in prerequisites}
    # for a, b in prerequisites:
    #     course_map[a].append(b)

    # q = deque([])
    # for course, prerequisite in prerequisites:
    #     q.extend([prerequisite])
    #     i = numCourses
    #     while q and i:
    #         pre_course = q.popleft()
    #         if pre_course == course:
    #             return False
    #         i -= 1
    #         q.extend(course_map.get(pre_course, []))

    # return True
