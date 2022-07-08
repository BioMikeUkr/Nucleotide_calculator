#ATAAGGTAAGTCCCCTGAATGCTAATTTCCGATCGTCTCGAGATCTGAGGGCGCGCCCTTAAATAAAAAAA
a = input('Type tour DNA sequence.:')
list1 = list(a.upper().strip())
list2 = []
for i in list1:
    if i == 'A':
        list2.append('T')
    if i == 'T':
        list2.append('A')
    if i == 'G':
        list2.append('C')
    if i == 'C':
        list2.append('A')
str1 = ''.join(list2)
print(f'Opposite strand of DNA: \n\t {str1}')
print(f'First strand of DNA: \n\t {str1}')
print(f'Full DNA: \n\t {a.upper().strip()} \n\t {str1}')