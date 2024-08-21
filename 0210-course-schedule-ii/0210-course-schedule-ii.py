class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses_map = {}
        for i in range(numCourses):
            courses_map[i] = []
        
        for crs, pre in prerequisites:
            courses_map[crs].append(pre)

        to_study = set()
        l = []
        def dfs(crs):
            if crs in to_study:
                return False
            if courses_map[crs] == []:
                l.append(crs)
                return True
            
            to_study.add(crs)
            for pre in courses_map[crs]:
                if not dfs(pre):
                    return False
            to_study.remove(crs)
            courses_map[crs] = []
            l.append(crs)
            return True 
        
        for crs in courses_map:
            if not dfs(crs):
                return []

        seen = set()
        result = []
        for crs in l:
            if crs not in seen:
                result.append(crs)
                seen.add(crs)

        return result