def find_outlier(integers):
    even_list = []
    odd_list = []
    for i in range(len(integers)):
        if integers[i]/2 % 1:
            even_list.append(integers[i])
        else:
            odd_list.append(integers[i])
    if len(even_list) == 1:
        return even_list[0]
    else:
        return odd_list[0]
