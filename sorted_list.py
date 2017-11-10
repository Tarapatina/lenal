#students = ['Sasha','Ivan','Masha']
#students.reverse ()
#print(students)

#order_students = sorted (students)
#print(order_students)
#a= [int(i)for i in input().split()]
#s=map(int, input().split())
#print (sum(s))

a=[int(i) for i in input().split()]
s=0
for i in a:
    s+=i
print(s)