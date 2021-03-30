
import random


dict_words = {
    'adjective': ['able',
                  'bad',
                  'best',
                  'better',
                  'big',
                  'black',
                  'certain',
                  'clear',
                  'different',
                  'early',
                  'easy',
                  'economic',
                  'federal',
                  'free',
                  'full',
                  'good',
                  'great',
                  'hard',
                  'high',
                  'human',
                  'important',
                  'international',
                  'large',
                  'late',
                  'little',
                  'local',
                  'long',
                  'low',
                  'major',
                  'military',
                  'national',
                  'new',
                  'old',
                  'only',
                  'other',
                  'political',
                  'possible',
                  'public',
                  'real',
                  'recent',
                  'right',
                  'small',
                  'social',
                  'special',
                  'strong',
                  'sure',
                  'true',
                  'white',
                  'whole',
                  'young'],
    'plural_noun': ['truss',
                    ' trusses',
                    'bus',
                    'buses',
                    'marsh',
                    'marshes',
                    'lunch',
                    'lunches',
                    'tax',
                    'taxes',
                    'blitz',
                    'blitzes'],
    'noun': ['Actor',
             'Gold',
             'Painting',
             'Advertisement',
             'Grass',
             'Parrot',
             'Afternoon',
             'Greece',
             'Pencil',
             'Airport'	,
             'Guitar'	,
             'Piano',
             'Ambulance',
             'Hair',
             'Pillow'],
    'place': [' Bahamas', ' Chine', 'Taïwan', 'Nicaragua', 'Russie', 'Afrique of Sud ', 'Algérie'],
    'noise': [
        'gibber', 'screech', 'growl', 'hum and buzz', 'chirrup', 'moo', 'cheep', 'cluck', 'crow', 'low', 'bark'
    ],
    'person_name': ['Abde', 'Jack', 'Philip']
}


chosen_words = {
    'adjective': random.choice(dict_words['adjective']),
    'plural_noun': random.choice(dict_words['plural_noun']),
    'noun': random.choice(dict_words['noun']),
    'place': random.choice(dict_words['place']),
    'noise': random.choice(dict_words['noise']),
    'person_name': random.choice(dict_words['person_name'])
}
print(
    "One of the most " + chosen_words['adjective'] + " characters in fiction is named Tarzan of the" + '\n' +
    chosen_words['plural_noun'] + '.' + "Tarzan was raised by a/an " + chosen_words['noun'] + " and lives in the " +'\n' +
    chosen_words['adjective'] + " jungle in the heart of darkest " + chosen_words['place'] + " ." +'\n' +
    "He spends most of his time eating " + chosen_words['plural_noun'] + " and swinging from tree to " +'\n' +
    chosen_words['noun'] +'\n' +
    " . Whenever he gets angry,he beats on his chest and says," + chosen_words['noise'] +'\n' +
    " ! This is his war cry." + " Tarzan always dresses in " + chosen_words['adjective'] +'\n' +
    " shorts made from the skin of a/an " + chosen_words['noun'] + " and his best friend is a/an " + '\n' +
    chosen_words['adjective'] + " chimpanzee named Cheetah. He is supposed to be able to speak to elephants and " + '\n' +
    chosen_words['plural_noun'] + " . In the movies, Tarzan is played by " +'\n' +
    chosen_words['person_name'] + " ."
)
