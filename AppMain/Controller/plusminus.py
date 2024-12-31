import re


def arrays(arr):
    positive_n = 0
    negative_n = 0
    zeros_n = 0
    total_numbers = len(arr)
    
    
    for i in arr:
        if i > 0:
            positive_n += 1 
        elif i < 0:
            negative_n += 1
        else:
            zeros_n += 1
    
    result_for_positive = positive_n / total_numbers
    result_for_negative = negative_n / total_numbers
    result_for_zeros = zeros_n / total_numbers
    # print("{:.6f}".format(round(result_for_positive, 2)))
    # # print("{:.6f}".format(round(result_for_negative, 2)))
    # print(round(result_for_negative, 6))
    # # print("{:.6f}".format(round(result_for_zeros, 2)))
    # print(round(result_for_zeros, 6))

    print(f"{result_for_positive:.6f}")
    print(f"{result_for_negative:.6f}")
    print(f"{result_for_zeros:.6f}")
    

if __name__ == "__main__":
    arrays_numbers = input("Please put the number list: ")
    list_convert = list(map(int, arrays_numbers.split()))
    arrays(list_convert)