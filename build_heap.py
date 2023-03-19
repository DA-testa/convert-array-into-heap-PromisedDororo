# python3


def build_heap(data,n):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(n//2,-1,-1):
        min_heap(i, swaps, n, data)
    return swaps

def min_heap(i, swaps, n , data):
    min_index = i
    lchild = 2 * i + 1
    if lchild < n and data[lchild] < data[min_index]:
        min_index = lchild
    rchild = 2 * i + 2
    if rchild < n and data[rchild] < data[min_index]:
        min_index = rchild
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        min_heap(min_index, swaps, n, data)


def main():
    
    input_t = ""
    text_input = input()
    if "I" in text_input:  
        # Input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    if "F" in text_input:
        filename = input()
        if "a" in filename:
           return
        else:
            filename = "tests/" + filename
            f = open(filename)
            n = f.readline()
            n = int(n)
            # print(n)
            input_t = f.readline()
            f.close()
            array = input_t.split(sep=" ")
            data = []
            for i in array:
                data.append(int(i))  
 
    # print("I or F")
    # input_type = input()
    # if "I" in input_type:
    #     n = int(input())
    #     data = list(map(int, input().split()))
    # elif "F" in input_type:
    #     filename = input()
    #     with open("tests/" + filename, 'r') as f:
    #         n = list (f.readline())
    #         data = list(map(int, input().split()))


    # # checks if lenght of data is the same as the said lenght
    # assert len(data) == n
     
    

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data,n)


    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
   
    assert len(swaps) <= 4*n

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
