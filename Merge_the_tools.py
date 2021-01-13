def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        unique_array=''
        for j in range(k):
            if string[i+j] not in unique_array:
                unique_array+=string[i+j]
        print(unique_array)
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)