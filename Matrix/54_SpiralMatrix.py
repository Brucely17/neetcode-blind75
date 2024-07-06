class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m= len(matrix)
        n=len(matrix[0])
        top=0
        bottom=m-1
        right=n-1
        left=0
        def spiralAddition(matrix,top,bottom,right,left,res=[]):


            
            print("\n")
            print("\n")
            print("\n")

            for i in range(left,right+1):
                print(matrix[top][i])
                
                res.append(matrix[top][i])
                if len(res)==m*n:
                    return res
            print(res)

            for i in range(top+1,bottom+1):
                
                res.append(matrix[i][right])
                if len(res)==m*n:
                    return res
            print(res)

            for i in range(right-1,left-1,-1):
               
                res.append(matrix[bottom][i])
                if len(res)==m*n:
                    return res
            print(res)

            for i in range(bottom-1,top,-1):
                
                res.append(matrix[i][left])
                if len(res)==m*n:
                    return res
            print(res)
            top+=1
            bottom-=1
            right-=1
            left+=1
            if top > bottom or left > right:
                return res
            print("Directions:",top,bottom,right,left)
            return spiralAddition(matrix,top,bottom,right,left,res)

        return spiralAddition(matrix,top,bottom,right,left,[])

                