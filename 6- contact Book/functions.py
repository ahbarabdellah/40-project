def cherchre(n, p):
    with open('data base.txt') as file:
        db = file.readlines()
        data = []
        res = []
        for i in db:
            data.append(i.split(','))
        for i in range(len(data)):
            if n in data[i][0]:
                res.append(data[i])
        if res == []:
            res = -1
        return res


def write(res):
    txt = ''
    j = 0
    for i in res:
        txt = txt + i[0] + ' : '+i[1]+'\n'
    return txt


def add2db(n, p):
    with open('data base.txt', 'a') as file:
        file.write('\n'+n+','+p+'\n')
    return n+' phone number is added \nto data base.'
