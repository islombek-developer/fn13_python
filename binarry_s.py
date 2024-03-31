# numbers = [3, 7, 24, 28, 33, 39, 70, 78, 78, 84, 103, 107, 111, 134, 135, 138, 150, 164, 176, 178, 186, 189, 193, 226,
#            229, 232, 246, 274, 278, 285, 292, 292, 296, 309, 328, 349, 353, 355, 383, 392, 399, 434, 436, 437, 439, 468,
#            468, 470, 481, 506, 506, 509, 511, 519, 527, 531, 538, 542, 555, 563, 592, 623, 650, 666, 667, 680, 724, 735,
#            736, 740, 754, 768, 771, 807, 821, 842, 845, 849, 853, 858, 872, 875,
#            883, 888, 907, 917, 920, 924, 927, 928, 930, 947, 950, 953, 953, 965, 970, 990, 995, 998]

# def binary_search(target, sorted_list):
#     start = 0
#     end = len(sorted_list)-1

#     count = 0


#     while start <=end:
#         mid = (start + end) // 2
#         mid_value = sorted_list[mid]

#         count+=1

#         print(count)
#         if mid_value == target:
#             return mid
#         elif mid_value < target:
#             start = mid + 1

#         elif mid_value > target:
#             end = mid -1



#     return "Bu son ro'yhat ichida mavjud emas"


# print(binary_search(998, numbers))

# def buble_sort(tartibsiz_list):
#     n = len(tartibsiz_list)

#     for i in range(n):
#         for j in range(0, n-1):
#             if tartibsiz_list[j] < tartibsiz_list[j+1]:
#                 tartibsiz_list[j+1], tartibsiz_list[j] = tartibsiz_list[j], tartibsiz_list[j+1] 
#     return tartibsiz_list
# print(buble_sort([2,4,5,6,1]))

# a=[-4,-3,2,4,8,10,15]
# def f(x,n):
#     d=[]
#     b=[]
#     s=[]
#     c=0
#     for i in x:
#         d.append(i)
#         for j in d:
#             if i+j==n:
#                 b.append(j)
#                 s.append(i)
#     return  b,s
# n=5
# print(f(a,n))

# def f(x):
#     if len(x)<=140 and x[0] == '#':    
#         a = x.title()
#         b = a.replace(' ', '')
#         return b
#     else:
#         return False
# print(f('# Hello world salom dunyo'))



# count = 0
# file = open('main.txt', 'r')
# reader = file.read()
# for i in reader.split():
#     count+=1

# print(count)
# file.close()


def teskari(list1):
    juft = []
    toq = []
    for i in list1:
        if i > 9 and i%2==0:
            juft.append(int(str(i)[::-1]))
        else:
            toq.append(int(str(i)))

    x = juft + toq
    y = len(juft + toq)    

    for a in range(y):
        for j in range(0, y-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x


print(teskari([1,21,48,21,48,56,789]))



