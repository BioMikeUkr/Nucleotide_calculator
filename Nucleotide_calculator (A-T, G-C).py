#x=input('The number of nucleotides:')
running = True
A = 'A'
T = 'T'
C = 'C'
G = 'G'
STOP = 'STOP'
STOP1 = 'STOP1'
GetOppositeStrandOfDna = 'GetOppositeStrandOfDna'
#print("Type a nucleotide (A,T,G,C), STOP to stop the script or GetOppositeStrandOfDna to get the opposite strand Of DNA")
print(('Type the seguense, every new nucleotide in the next string as (A,T,C,G), when stop type STOP1'))
print(('start'))
print((''))
while running:
    f = input('')
    if f == STOP1:
        running = False
        print((''))
        print(('end '))
        print((''))
        print('Copy and paste the sequence with start and the space in the end:')
running = True
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
    #elif a == GetOppositeStrandOfDna:
    elif a == STOP:
        running = False
        print('The proces has been stopped')




