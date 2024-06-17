class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        listSet = set()

        def dfs(crs):
            if crs in listSet:
                return False
            if preMap[crs] == []:
                return True
            
            listSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            listSet.remove(crs)
            preMap[crs] = []

            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True