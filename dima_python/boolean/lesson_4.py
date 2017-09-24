def fun(a):
    ostatok=a%400
    if ostatok==0:
        return "Высокосный"
    else:
        return "Обычный"
z=fun (2000)
print(z)

