new_list = []
suffix0 = '0123456789'
suffix1 = 'abcdefghijklmnopqrstuvwxyz'
postcodes = open("postcode_prefix.txt",'r').readlines()

postcodes = [word.lower().strip() for word in postcodes]


for s in postcodes:

    for suf0 in suffix0:

        for suf1 in suffix1:

            for suf2 in suffix1:

                new_list.append((s + ' ' +suf0+suf1+suf2).upper())

print('created: ' + str(len(new_list)) + ' valid postcodes')




def check(query):

    if query.upper() in new_list:

        print('Valid')

    else:

        print('Invalid')
        


    
