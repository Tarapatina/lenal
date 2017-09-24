
message = 'Attention! The file was modified!'

with open('test') as example, open('htaccess') as origin:
    for x, y in zip(example, origin):

        if x != y:
            print(message)
        else:
            print('ok')

