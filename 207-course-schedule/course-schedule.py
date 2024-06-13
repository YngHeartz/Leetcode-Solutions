class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        listset = set()

        def helper(crs):
            if crs in listset:
                return False
            if preMap[crs] == []:
                return True
            
            listset.add(crs)

            for pre in preMap[crs]:
                if not helper(pre):
                    return False
            
            listset.remove(crs)
            preMap[crs] = []

            return True

        for crs in range(numCourses):
            if not helper(crs):
                return False

        return True