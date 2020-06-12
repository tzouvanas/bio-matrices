import numpy as np

class MathTools:

    @staticmethod
    def transpose(array: list):

        newArray = []
        for element in array:
            newArray.append([element])

        return newArray

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

        if len(arrays) == 1:
            return MathTools.transpose(arrays[0])

        cartesian_so_far = None
        
        for i in range(0, len(arrays)):
            if i == 0:
                cartesian_so_far = arrays[i]
            if (i + 1) < len(arrays): 
                next_Column = arrays[i+1]
                cartesian_so_far = MathTools.cartesian_of_two(cartesian_so_far, next_Column)

        return cartesian_so_far
