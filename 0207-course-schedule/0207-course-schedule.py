class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            course_map[crs].append(pre)
        seen = set()
        def dfs(crs):
            if course_map[crs] == []:
                return True
            if crs in seen:
                return False
            seen.add(crs)
            for pre in course_map[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            course_map[crs] = []
            return True
        
        for crs in course_map:
            if not dfs(crs):
                return False
        return True