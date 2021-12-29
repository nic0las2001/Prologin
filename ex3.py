from sys import exit

target = int(input(''))
list_length = int(input(''))
main_list_string = input('')

#Convert list input into numeric sequence
main_list_text = main_list_string.split()

main_list = [int(item) for item in main_list_text]

#Diviseurs de target
other_sign_multiples = []
bounds = [-target,target]
bounds.sort()

multiples_list = [i for i in range(bounds[0]-1, bounds[1]+1) if (i != 0) and (target % i == 0)]

def sort_func(values):
    top_combination_str = ['','']
    for i in range(0,2):
        top_combination_str[i] = [str(item) for item in values[i]]

    list_a = ' '.join(top_combination_str[0])
    list_b = ' '.join(top_combination_str[1])
    if len(values[0]) >  len(values[1]):
        print(list_a)
        print(list_b)
    elif len(values[0]) < len(values[1]):
        print(list_b)
        print(list_a)
    else:
        if sum(values[0]) >=  sum(values[1]):
            print(list_a)
            print(list_b)
        else:
            print(list_b)
            print(list_a)
    exit()

#Iteration des listes
new_list = [list(main_list)]
if target != 0:
    lengths = {} #{sum:length}
    sums = {} #{sum:[list]}
    matches = {}
    for i_global in range(0,len(main_list)):
        for element in new_list:
            if sum(element) in multiples_list:
                sums[sum(element)] = list(element)
                lengths[sum(element)] = len(element)
                if target/sum(element) in sums:
                    matches[lengths[sum(element)] + lengths[target/sum(element)]] = [element,sums[target/sum(element)]]
        for value in matches:
            if value >= max(lengths.values()) + len(new_list[0]):
                    sort_func(matches[value])
        old_list = list(new_list)
        new_list = [list(old_list[i][0:len(main_list)-i_global-1]) for i in range(0,len(old_list))]
        new_list.append(list(old_list[len(old_list)-1][1:len(main_list)-i_global]))
    pairs = []
    top = [0,[]]
    for value in matches:
        if value >= max(lengths.values()) + len(new_list[0]):
            pairs.append(matches[value])
    if len(pairs) > 0:
        for i in range(0,len(pairs)):
            leng = len(pairs[i][0]) + len(pairs[i][1])
            if leng > top[0]:
                top[0] = leng
                top[1] = pairs[i]
        sort_func(top[1])
else:
    for i_global in range(0,len(main_list)):
        for element in new_list:
            if sum(element) == 0:
                sort_func([main_list,element])
        old_list = list(new_list)
        new_list = [list(old_list[i][0:len(main_list)-i_global-1]) for i in range(0,len(old_list))]
        new_list.append(list(old_list[len(old_list)-1][1:len(main_list)-i_global]))

print('IMPOSSIBLE')
