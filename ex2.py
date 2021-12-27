nCouleurs = int(input(''))
couleurs = []
for i in range(0,nCouleurs):
    couleur = input('')
    couleurs.append(str(couleur))

nCotes = int(input(''))
couleurscotes = []
for i in range(0,nCotes):
    couleurcote = input('')
    couleurscotes.append(str(couleurcote))

pieces = []
nPieces = int(input(''))
for i in range(0,nPieces):
    nCotesPiece = int(input(''))
    couleurPiece = input('')
    pieces.append([int(nCotesPiece),str(couleurPiece)])

output_string = ''
output_count = 0
for piece in pieces:
    if (piece[0] == nCotes) and (piece[1] not in couleurscotes):
            output_count += 1
            output_string += 'O'
    else:
        output_string += 'X'

print(output_string)
print(output_count)
