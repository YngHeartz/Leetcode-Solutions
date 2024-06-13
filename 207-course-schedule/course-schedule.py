class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a map (dictionary) to store the prerequisites for each course
        preMap = {i: [] for i in range(numCourses)}

        # Populate the preMap with the given prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # Initialize a set to keep track of visited courses and detect cycles
        visited = set()

        # Define a helper function to perform a depth-first search (DFS) on the course graph
        def dfs(crs):
            # If the course is already in the visited set, a cycle is detected, return False
            if crs in visited:
                return False
            # If the course has no prerequisites, it can be finished, return True
            if not preMap[crs]:
                return True
            
            # Add the course to the visited set to track the current path in the DFS
            visited.add(crs)

            # Recursively perform DFS on all prerequisites of the current course
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            # Remove the course from the visited set and mark it as having no prerequisites
            visited.remove(crs)
            preMap[crs] = []

            return True

        # Check each course to see if it can be completed by performing a DFS
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        # If all courses can be completed, return True
        return True