def insertion_sort(arr):

    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while (j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

    return arr


def main():
    arr=[8, 3, 6, 2, 7, 1]
    new_list=insertion_sort(arr)
    print(new_list)


main()

''' worst case complexity of bubble sort is O(n**2)'''
'''best case complexity is O(1)'''