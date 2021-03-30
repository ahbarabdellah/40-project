'''advature game'''
import time

ans = input('Slam WAx msta3ed ta5ed had l moramar ou la la ? \n (Ah/la) : ')
if ans.lower() == 'ah':
    print('Bravo ha hna ranbdaw mn daba maratb9ach l omour sahla...... daba mora 5 d tawani ranta9lo l domaine d lo3ba \n ' +
          ' hahna ranta9lo ')
    time.sleep(5)
    print('__________________________________________________ \n' +
          '                 03/03/3020 \n' +
          '__________________________________________________ \n')
    time.sleep(1)
    print('Smh liya nsit mageltch lik l mision dyalk ra f l 3am 3000 .\n' +
          'f l 3am 300 ta haja mab9at kima kat3refha l fadaiyin li hakmin l ard  \n' +
          'ou nta woya l bachar l wahid li b9a red lbal ra t9der tmout ila chfouk...\n' +
          '9edamk tiyara ou 9edamk tomobil chno rat5tar (tiyara/bateuax ) :\n')
    ans = input('>>> ')
    print('hanta radi ou rkebti :')
    time.sleep(1)
    print('------------ 3 ------------')
    time.sleep(1)
    print('------------ 2 ------------')
    time.sleep(1)
    print('------------ 1 ------------')
    if ans.lower() == 'tiyara':
        print(
            'HMAR NTA fin 3emer mok konti pilot bach t5edem had tiyara rje3 lard rak meti')
    if ans.lower() == 'tomobila':
        print(
            'HMAR NTA fin 3emer mok kan 3endek pirmi rak meti bksida')

else:
    print('5eawf sir bhalk')
