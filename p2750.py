
inputs = [200,99,-23,32,1]

# 내장함수
print(inputs)
inputs.sort()
print(inputs)
print('********************')

# Bubble Sort
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubbleSort(x):
    for size in range(len(x)):
        for i in range(size): 
            if x[i] > x[i+1]:
                swap(x, i, i+1)

inputs = [200,99,-23,32,1]
print(inputs)
bubbleSort(inputs)
print(inputs)
print('********************')

# Selection Sort

