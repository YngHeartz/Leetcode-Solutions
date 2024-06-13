class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Create a map that will store the pre recs inside of the map
        preMap = {i: [] for i in range(numCourses)}

        #for each cours and prerec inside the prerequisties append the pre to the premap course in the dict
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        #Create a empty list that is a set so we can detect infinite loops
        listset = set()

        #Helper function to itterate through the graph
        def helper(crs):
            #Base case if the crs is already in the list we return false and if the preMap is empty return True
            if crs in listset:
                return False
            if preMap[crs] == []:
                return True
            
            #Add the crs to the listset
            listset.add(crs)


            #For each prerec in the preMap run a recursive call on the prerecs in the preMap and if there is not a prerec return False
            for pre in preMap[crs]:
                if not helper(pre):
                    return False
            
            #remove the crs from the listset and then set the preMap to empty so we can do the steps over when we call the function recursivly we will start fresh
            listset.remove(crs)
            preMap[crs] = []

            return True

        #check to see if the crs is in the numCourses and if it is not return False after recursivly calling to make sure the course is not in there or the prerecs
        for crs in range(numCourses):
            if not helper(crs):
                return False

        return True