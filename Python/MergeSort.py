def MergeSort(arr,left:int,right:int):

    if left>=right:
        return
    
    mid = (left+right)//2
    MergeSort(arr,left,mid)
    MergeSort(arr,mid+1,right)
    Merge(arr,left,mid,right)

def Merge(arr,left:int,mid:int,right:int):
    i = left
    j = mid+1
    k=0
    temp=[]

    # two point
    while(i<=mid and j<=right):
        if arr[i]<= arr[j]:
            temp.append(arr[i])
            i+=1
        else: 
            temp.append(arr[j])
            j+=1
        k+=1

    # the rest num
    while(i<=mid):
        temp.append(arr[i])
        k+=1
        i+=1
    while(j<=right):
        temp.append(arr[j])
        k+=1
        j+=1

    # modify arr
    for i in range(left,right+1):
        arr[i]=temp[i-left]


def main():
    arr=[3,5,4,8,9,6,3,5,4,70,1]
    MergeSort(arr,0,len(arr)-1)
    print(arr)

if __name__ == "__main__":
    main()
