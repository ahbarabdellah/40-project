import random
list_of_word = [
    'people', 'history', 'way', 'art', 'world', 'map', 'two', 'family', 'health', 'system', 'meat', 'year', 'thanks', 'music', 'person', 'reading', 'method', 'data', 'food', 'theory', 'law', 'bird', 'problem', 'control', 'power', 'ability', 'love', 'television', 'science', 'library', 'nature', 'fact', 'product', 'idea', 'investment', 'area', 'society', 'story', 'media', 'thing', 'oven', 'definition', 'safety', 'quality', 'language', 'player', 'variety', 'video', 'week', 'country', 'exam', 'movie', 'equipment', 'physics',
    'policy', 'series', 'thought', 'basis', 'direction', 'technology', 'army', 'camera', 'freedom', 'paper', 'child', 'month', 'truth', 'university', 'writing', 'article', 'difference', 'goal', 'news', 'fishing', 'growth', 'income', 'user', 'failure', 'meaning', 'philosophy', 'teacher', 'night', 'disease', 'disk', 'energy', 'nation', 'road', 'role', 'soup', 'location', 'success', 'apartment', 'math', 'moment', 'politics', 'decision', 'event', 'shopping', 'student', 'wood', 'distribution', 'office', 'president', 'unit', 'cigarette', 'context', 'opportunity', 'driver', 'flight', 'length', 'newspaper', 'teaching', 'cell', 'dealer', 'finding', 'lake', 'member', 'message', 'phone', 'scene', 'association', 'concept', 'death', 'housing', 'insurance', 'mood', 'woman', 'advice', 'blood',
    'effort', 'importance', 'opinion', 'payment', 'reality', 'situation', 'skill', 'wealth', 'city', 'county', 'depth', 'estate', 'grandmother', 'heart', 'photo', 'recipe', 'studio', 'topic', 'depression', 'passion', 'resource', 'setting', 'ad', 'agency', 'college', 'criticism', 'debt', 'memory', 'secretary', 'administration', 'aspect', 'director', 'psychology', 'response', 'storage', 'version', 'alcoho', 'argumen', 'contrac', 'emphasi', 'highwa', 'los', 'possessio', 'stea', 'unio', 'cance', 'currenc', 'engineerin', 'entr', 'mixtur', 'regio', 'republi', 'viru', 'acto', 'deliver', 'devic', 'dram', 'electio', 'engin', 'footbal', 'guidanc', 'hote', 'owne', 'priorit', 'suggestio', 'tensio', 'anxiet', 'awarenes', 'bat', 'brea', 'climat', 'confusio', 'elevato', 'emotio', 'employe', 'employe', 'gues', 'heigh', 'mal', 'manage', 'recordin', 'sampl', 'charit', 'cousi', 'disaste', 'edito', 'excitemen', 'exten', 'feedbac', 'guita', 'homewor', 'leade', 'mo', 'outcom', 'presentatio', 'reflectio', 'resolutio', 'revenu', 'sessio', 'singe', 'tenni', 'baske', 'bonu', 'cabine', 'churc', 'clothe', 'coffe', 'dinne', 'drawin', 'hai', 'hearin', 'judgmen', 'la', 'mod', 'mu', 'orang', 'poetr', 'polic', 'procedur', 'quee', 'rati', 'relatio', 'satisfactio', 'secto', 'significanc', 'son', 'toot', 'tow', 'vehicl', 'volum', 'wif', 'acciden', 'airpor', 'arriva', 'basebal', 'chapte', 'conversatio', 'databas', 'erro', 'farme', 'gat', 'gir', 'hal', 'hospita', 'injur', 'maintenanc', 'mea', 'pi', 'poe', 'presenc', 'proposa', 'replacemen', 'rive', 'so', 'speec', 'te', 'villag', 'warnin', 'winne', 'worke', 'write', 'breat', 'buye', 'ches', 'conclusio', 'cooki', 'courag', 'da', 'des', 'drawe', 'examinatio', 'garbag', 'grocer', 'hone', 'improvemen', 'insec', 'inspecto', 'kin', 'ladde', 'men', 'penalt', 'pian', 'potat', 'professo', 'quantit', 'reactio', 'sala', 'siste', 'tongu', 'weaknes', 'weddin', 'affai', 'ambitio', 'analys', 'appl', 'assistan', 'bathroo', 'bedroo', 'bee', 'birthda', 'championshi', 'chee', 'clien', 'departur', 'diamon', 'dir', 'ea', 'fortun', 'funera', 'gen', 'ha', 'intentio', 'lad',
    'midnigh', 'obligatio', 'pizz', 'platfor', 'poe', 'recognitio', 'shir', 'si', 'speake', 'strange', 'surger', 'sympath', 'tal', 'throa', 'traine', 'uncl', 'yout', 'time']

rndm_word = random.choice(list_of_word)
print(rndm_word)

ltr_chs = (len(rndm_word)*2)+1
alpha = 'qwertzuiopasdfghjklyxcvbnm'

# algo letter to chose from :
list_of_btn = []

# del evrey letter allready exist in the word
for i in rndm_word:
    list_of_btn.append(i)
    alpha.replace(i, '')
    #
for i in range(ltr_chs):
    k = random.choice(alpha)
    list_of_btn.append(k)
    alpha.replace(k, '')

# Arrange the values in a list_of_btn alphabiticly :
list_of_btn.sort()


# find position of a ltr in a wrd :


def find_ltr(wrd, ch):
    l = []
    for i in range(len(wrd)):
        if wrd[i] == ch:
            l.append(i)
    return(l)


# word to guess :
wrd = ['_']*len(rndm_word)
'''
    block de code vous permet de cree une liste de variable 
qui la meme taille que la langueur de rndm_wrd.

'''

# the main Game :

print('guess the rghit word to won :', end='')
print('to help the word is composed from thos letter.')
print(list_of_btn)
chance = 7
while(chance >= 0):
    if ''.join(wrd) == rndm_word:
        break
    print(''.join(wrd))
    print('you have '+str(chance)+' chance.')
    a = input('chose a letter: ')
    if a in rndm_word:
        l = find_ltr(rndm_word, a)
        for i in range(len(l)):
            wrd[l[i]] = a

    else:
        chance -= 1

if chance < 0:
    print('solotion is {}'.format(rndm_word))
    print('\n Game Over ')
else:
    print('\n winner ')
