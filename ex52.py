nPuces = int(input(""))
nFils = int(input(""))
nQuestions = int(input(""))

signaux_str = input('')
signaux_list = signaux_str.split()
signaux = []
for signal in signaux_list:
    signaux.append(int(signal))

fils = {}
for i in range(0,nFils):
    fil_str = input("")
    fil_list = fil_str.split()
    fil = [int(fil_list[i]) for i in range(0,len(fil_list))]
    if fil[0] in fils:
        fils[fil[0]].append(fil[1])
    else:
        fils[fil[0]] = [fil[1]]
    if fil[1] in fils:
        fils[fil[1]].append(fil[0])
    else:
        fils[fil[1]] = [fil[0]]

questions = []
for i in range(0,nQuestions):
    question_str = input("")
    question_list = question_str.split()
    question = [int(question_list[i]) for i in range(0,len(question_list))]
    questions.append(list(question))

def dict_format(start,finish,fils):
        new_fils = dict(fils)
        delete_list=[]
        #del new_fils[finish]
        condition = True
        while condition:
            for entry in fils:
                if len(fils[entry]) == 1:
                    if entry not in [start,finish]:
                        del new_fils[entry]
                        delete_list.append(entry)
                elif len(fils[entry]) == 0:
                    del new_fils[entry]
            for entry in new_fils:
                temp = list(new_fils[entry])
                for i in range(0,len(new_fils[entry])):
                    if new_fils[entry][i] in delete_list:# and new_fils[entry][i] != [finish]:
                        temp.remove(new_fils[entry][i])
                new_fils[entry] = list(temp)
            fils = dict(new_fils)
            count = 0
            for val in new_fils:
                if len(fils[val]) == 0:
                    del fils[val]
            new_fils = dict(fils)

            condition = False
            for item in fils:
                if item in [start,finish]:
                    if len(fils[item]) != 1:
                        condition = True
                else:
                    if len(fils[item]) != 2:
                        condition = True
        return fils

for question in questions:
    path = dict_format(question[0],question[1],fils)
    signal_strength = 1
    for val in path:
        signal_strength *= signaux[val]
    while signal_strength > 1671404011:
        signal_strength = signal_strength % 1671404011
    print(signal_strength)
