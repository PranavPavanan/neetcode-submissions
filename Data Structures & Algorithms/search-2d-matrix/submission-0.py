class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        first_array=0
        last_array=len(matrix)-1

        while first_array <= last_array:
            cur = (first_array+last_array) // 2
            if target >= matrix[cur][0] and target <= matrix[cur][-1]:
                left = 0
                right = (len(matrix[cur]))-1

                while left <= right:
                    mid = (left+right) // 2

                    if target == matrix[cur][mid]:
                        return True
                    elif target <= matrix[cur][mid]:
                        right = mid-1
                    else:
                        left = mid+1
                return False
            

            elif target <= matrix[cur][0]:
                last_array = cur-1

            elif target >= matrix[cur][-1]:
                first_array = cur+1

        return False



        