class Quick_sort():
    def get_index(self,num,low,high):
        tmp=num[low]
        while low<high:
            while low<high and tmp<num[high]:
                high-=1
            if low<high:
                num[low]=num[high]
                low=+1
            while low<high and tmp>num[low]:
                low+=1
            if low<high:
                num[high]=num[low]
                high-=1
        num[low]=tmp
        return low
    def quicksort(self,num,low,high):
        if low<high:
            index=self.get_index(num,low,high)
            self.quicksort(num,low,index-1)
            self.quicksort(num,index+1,high)


num=[11, 10, 3, 12, 33, 1000, 1, 333, -11]
Quick_sort().quicksort(num,0,len(num)-1)
print(num)