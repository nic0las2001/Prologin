taille_chaine = int(input(''))
taille_mdp = int(input(''))
chaine = input('')

minuscules = 'abcdefghijklmnopqrstuvwxyz'
majuscules = 'abcdefghijklmnopqrstuvwxyz'.upper()
nombres = '1234567890'
speciaux = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

decoded = ''
keys = 'mMns'
for char in chaine:
    if char in minuscules:
        decoded += 'm'
    elif char in majuscules:
        decoded += 'M'
    elif char in nombres:
        decoded += 'n'
    else:
        decoded += 's'

possible_combinations = 0
for i in range(0,len(decoded)-taille_mdp+1):
    val_count = 1
    for item in keys:
        if item not in decoded[i:i+taille_mdp]:
            val_count = 0
    possible_combinations += val_count

print(possible_combinations)
