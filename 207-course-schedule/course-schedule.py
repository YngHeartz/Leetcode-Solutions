class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prevMap[crs].append(pre)

        scott = set()

        def dfs(crs):
            if crs in scott:
                return False
            if prevMap[crs] == []:
                return True

            scott.add(crs)

            for pre in prevMap[crs]:
                if not dfs(pre):
                    return False

            scott.remove(crs)
            prevMap[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True