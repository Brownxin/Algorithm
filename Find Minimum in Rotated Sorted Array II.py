class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        def mergeSort(temp):
            length=len(temp)
            if length<2:
                return temp
            left=temp[:int(length/2)]
            right=temp[int(length/2):]

            temp_left=mergeSort(left)
            temp_right=mergeSort(right)

            return merge(temp_left,temp_right)


        def merge(left,right):
            temp_res=[]
            while len(left)>0 and len(right)>0:
                if left[0]<right[0]:
                    temp_res.append(left.pop(0))
                else:
                    temp_res.append(right.pop(0))

            if len(left)>len(right):
                temp_res.extend(left)
            else:
                temp_res.extend(right)

            return temp_res

        list=mergeSort(num)
        return list[0]