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

def path_func(signaux,start,finish,fils,blacklist):
    blacklist.append(start)
    found = False
    signal_strength = signaux[start]
    if start != finish:
        if finish in fils[start]:
            found = True
            signal_strength *= signaux[finish]
            return signal_strength,found
        else:
            for connection in fils[start]:
                if connection not in blacklist:
                    output,found = path_func(signaux,connection,finish,fils,blacklist)
                    if found == True:
                        signal_strength *= output
                        return signal_strength,found
    else:
        found = True
        return signal_strength, found
    return 1, found

def dict_format(signaux,start,finish,fils,blacklist):
        new_fils = dict(fils)
        delete_list=[]
        for entry in fils:
            if len(fils[entry]) == 1 and fils[entry][0] not in [finish,start] and entry not in [finish,start]:
                print
                del new_fils[entry]
                delete_list.append(entry)
        for entry in new_fils:
            temp = list(new_fils[entry])
            for i in range(0,len(new_fils[entry])):
                if new_fils[entry][i] in delete_list:
                    temp.remove(new_fils[entry][i])
            new_fils[entry] = list(temp)

        signal_strength,found = path_func(signaux,question[0],question[1],new_fils,blacklist)
        return signal_strength,found

for question in questions:
    blacklist = []
    signal_strength,found = dict_format(signaux,question[0],question[1],fils,blacklist)
    while signal_strength > 1671404011:
        signal_strength = signal_strength % 1671404011
    print(signal_strength)
