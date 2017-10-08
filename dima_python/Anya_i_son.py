A=int (input())
B=int (input())
H=int (input())

if H<A:
    print('Недосып')
if H>B:
    print('Пересып')
if (H>=A) and (H<=B):
    print('Это нормально')