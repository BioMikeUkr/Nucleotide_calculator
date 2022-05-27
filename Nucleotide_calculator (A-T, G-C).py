x=input('The number of nucleotides:')
running = True
A = 'A'
T = 'T'
C = 'C'
G = 'G'
STOP = 'STOP'
GetOppositeStrandOfDna = 'GetOppositeStrandOfDna'
print("Type a nucleotide (A,T,G,C), STOP to stop the script or GetOppositeStrandOfDna to get the opposite strand Of DNA")
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
    elif a == GetOppositeStrandOfDna:
        b = input('Copy and paste the sequence upper:')
        result_str = ""
        for i in range(1, len(b)):
            if i != 2:
                result_str = result_str + b[i]
                print(result_str)


    elif a == STOP:
        running = False
        print('The proces has been stopped')




