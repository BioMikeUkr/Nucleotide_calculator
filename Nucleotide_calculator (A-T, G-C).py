running = True
A = 'A'
T = 'T'
C = 'C'
G = 'G'
print(('Type the seguense, every new nucleotide in the next string as (A,T,C,G), when stop type STOP1'))
print(('start'))
print((''))
while running:
    f = input('')
    if f == 'STOP':
        break
print((''))
print(('end '))
print((''))
print('Copy and paste the sequence with start and the space in the end:')
while running:
    a = input('')
    if a == A:
        print(C)
    elif a == T:
        print(A)
    elif a == C:
        print(G)
    elif a == G:
        print(C)
    elif a == 'STOP':
        break
print('The proces has been stopped')




