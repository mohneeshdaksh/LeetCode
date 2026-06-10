
strs = ["act","pots","tops","cat","stop","hat"]

dic_sorted = {}
output_arr = []
for i in strs:
    sorted_string = ''.join(sorted(i))
    if sorted_string in dic_sorted:
        dic_sorted[sorted_string].append(i)
    else:
        dic_sorted[sorted_string] = [i]
for j in dic_sorted:
    output_arr.append(dic_sorted[j])
print(output_arr)
