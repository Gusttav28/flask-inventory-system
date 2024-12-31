import re

def mini_max_s(arr):
    first_count = 0
    second_count = 0
    # max_number = max(arr)
    print(arr)
    arr.sort()
    print(arr)
    for i in arr[:4]:         
        first_count += i
    
    for e in arr[1:]:
        second_count += e
    
    print(first_count, second_count)
    



if __name__== "__main__":
    arr = list(map(int, input("put the number list: ").rstrip().split()))
    mini_max_s(arr)
