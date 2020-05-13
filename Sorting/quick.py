
arr = [9, 5, 7, 2, 6]
def quick_sort(arr,start,end):

    if (start<end):
        partition_index=partition(arr,start,end)
        quick_sort(arr,start,partition_index-1)
        quick_sort(arr,partition_index+1,end)





def partition(A,start,end):
    pivot=A[end]
    partition_index=start
    for i in range(start,end):
        if A[i]<=pivot:
            A[partition_index],A[i]=A[i],A[partition_index]
            partition_index=partition_index+1
    A[partition_index],A[end]=A[end],A[partition_index]

    return partition_index


def main():

    start=0
    end=len(arr)-1
    print(f"Before Sorting :{arr}")
    quick_sort(arr,start,end)
    print(f"After Sorting :{arr}")

main()