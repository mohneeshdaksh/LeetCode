s = "O1O2O3"

odd_elements = s[0::2]
even_elements = s[1::2]

print(odd_elements)
print(even_elements)

for elem1, elem2 in zip(odd_elements, even_elements):
    if elem1 == elem2:
        count 