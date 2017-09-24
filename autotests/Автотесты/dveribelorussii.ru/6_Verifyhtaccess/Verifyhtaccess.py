
message = 'Attention! The file was modified!'

with open('test') as example, open('htaccess') as origin:
    schetchik=0
    for x, y in zip(example, origin):
        schetchik=schetchik+1
        if x != y:
            print(message)
        else:
            print('ok',schetchik)

