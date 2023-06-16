words = ['five', 'ten', 'two', 'three']
num = [5, 10, 2, 3]

x = {words[i]: num[i] for i in range(len(num))}

print(x)