import numpy as np

class MathTools:

    @staticmethod
    def unique_arrays(listOfarrays: list):
        
        uniqueList = []

        if len(listOfarrays) == 0:
            return uniqueList

        uniqueList.append(listOfarrays[0])
        
        for i in range(1, len(listOfarrays)):
            
            exists = False
            for j in range(0, len(uniqueList)):
                if np.array_equal(listOfarrays[i], uniqueList[j]):
                    exists = True
            
            if exists == False:
                uniqueList.append(listOfarrays[i])

        return uniqueList

    @staticmethod
    def cartesian_of_two(arrayA: list, arrayB: list):

        result = []
        for row_of_a in arrayA:
            for row_of_b in arrayB:
                row = np.hstack((row_of_a, row_of_b))
                result.append(row)

        return result

    @staticmethod
    def cartesian_of_many(arrays:list):

        cartesian_so_far = None
        
        for i in range(0, len(arrays)):
            if i == 0:
                cartesian_so_far = arrays[i]
            if (i + 1) < len(arrays): 
                next_Column = arrays[i+1]
                cartesian_so_far = MathTools.cartesian_of_two(cartesian_so_far, next_Column)

        return cartesian_so_far
