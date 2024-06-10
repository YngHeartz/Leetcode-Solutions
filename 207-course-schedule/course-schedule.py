class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prevMap[crs].append(pre)
        
        Listset = set()

        def helper(crs):
            if crs in Listset:
                return False
            if prevMap[crs] == []:
                return True
            
            Listset.add(crs)

            for pre in prevMap[crs]:
                if not helper(pre):
                    return False
                    
            Listset.remove(crs)
            prevMap[crs] = []

            return True
            

        for crs in range(numCourses):
            if not helper(crs):
                return False
                
        return True