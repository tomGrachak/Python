""" Ultimate Vovel Counter 2018, Tomosoft Inc. """

str = 'taoeiu'

def vovels():
    vovel_count = 0
    for x in str:
        if x is 'a':
            vovel_count += 1
        elif x is 'e':
            vovel_count += 1
        elif x is 'i':
            vovel_count += 1
        elif x is 'o':
            vovel_count += 1
        elif x is 'u':
            vovel_count += 1
    print('There are', vovel_count, 'vovels in that word.')

vovels()

