taille_chaine = int(input(''))
taille_mdp = int(input(''))
chaine = input('')

minuscules = 'abcdefghijklmnopqrstuvwxyz'
majuscules = 'abcdefghijklmnopqrstuvwxyz'.upper()
nombres = '1234567890'
speciaux = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

possible_combinations = 0
for i in range(0,len(chaine)-taille_mdp+1):
    (min, maj, nb, sp) = (False, False, False, False)
    for j in range(i,i+taille_mdp):
        if chaine[j] in minuscules:
            min = True
        if chaine[j] in majuscules:
            maj = True
        if chaine[j] in nombres:
            nb = True
        if chaine[j] in speciaux:
            sp = True
    if min and maj and nb and sp:
        possible_combinations += 1

print(possible_combinations)
