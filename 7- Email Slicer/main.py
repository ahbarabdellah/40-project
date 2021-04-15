email = input('Enter email:')
if '@' in email:
    res = email.partition('@')
    print('uesr : {}\ndomain : {}'.format(res[0], res[2]))
else:
    print('Make sure you entre an email cntan @ character !!')
