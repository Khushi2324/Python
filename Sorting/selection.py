def selection_sort(arr):
    for i in range(0,len(arr)):
        smallest=i
        for j in range(i+1,len(arr)):
            if arr[smallest]>arr[j]:
                smallest=j

        arr[i],arr[smallest]=arr[smallest],arr[i]
    return arr

def main():
    arr=[8, 3, 6, 2, 7, 1]
    sorted_array=selection_sort(arr)
    print(sorted_array)





main()

''' worst case complexity of bubble sort is O(n**2)'''
'''best case complexity is O(n**2)'''