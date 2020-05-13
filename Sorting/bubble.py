from sys import exit
def bubble_sort(arr):
    flag=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-(i+1)):

            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                flag=1
        if flag==0  :
            print("Element Already Sorted")
            exit()

    return arr


def main():
    arr=[2, 3, 4, 5, 7, 8]
    new_list=bubble_sort(arr)
    print(new_list)


main()

''' worst case complexity of bubble sort is O(n**2)'''
'''best case complexity is O(1)'''