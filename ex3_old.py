target = int(input(''))
list_length = int(input(''))
main_list_string = input('')

#Convert list input into numeric sequence
main_list_text = main_list_string.split()

main_list = []
for item in main_list_text:
    main_list.append(int(item))

'''if list_length != len(main_list):
    print("IMPOSSIBLE")
    exit()'''

#Diviseurs de target
multiples_list = []
other_sign_multiples = []
if target > 0:
    for i in range(1, target+1):
        if target % i == 0:
            multiples_list.append(i)
            other_sign_multiples = [-item for item in multiples_list]
elif target < 0:
    for i in range(target-1,-1):
        if target % i == 0:
            multiples_list.append(i)
            other_sign_multiples = [-item for item in multiples_list]
multiples_list.extend(other_sign_multiples)
print(multiples_list)

#Découpage des listes
possible_lists = []
for i_global in range(0,len(main_list)):
    list_one = []
    for i in range(i_global,len(main_list)):
        list_one.append(main_list[i])
        if (sum(list_one) in multiples_list) and target != 0:
            possible_lists.insert(len(possible_lists),list(list_one))
        elif target == 0:
            possible_lists.insert(len(possible_lists),list(list_one))

#Classement des listes / suppression des plus courtes
val_dict = {}
for item in possible_lists:
    if sum(item) in val_dict:
        if len(val_dict[sum(item)]) < len(item):
            val_dict[sum(item)] = item
    else:
        val_dict[sum(item)] = item

possible_combinations = []
blacklist = []
#target = 0 case:
if target == 0:
    if 0 in val_dict:
        for subitem in val_dict:
            new_element = [list(val_dict[0]),list(val_dict[subitem])]
            new_element.sort()
            possible_combinations.append(new_element)
    else:
        print('IMPOSSIBLE')
        exit()
else:
#Pair lists together
    for item in val_dict:
        if (round(target/item) in val_dict) and (item not in blacklist):
            blacklist.append(round(target/item))
            new_element = [list(val_dict[item]),list(val_dict[round(target/item)])]
            new_element.sort()
            possible_combinations.append(new_element)

#Check list isn't empty
if possible_combinations == []:
    print('IMPOSSIBLE')
else:
    #Work out best combination
    highest_length = 0
    for sublist in possible_combinations:
        length_combination = len(sublist[0]) + len(sublist[1])
        if length_combination > highest_length:
            highest_length = length_combination
            top_combination = sublist
        elif length_combination == highest_length:
            sum_combination = sum(sublist[0]) + sum(sublist[1])
            sum_highest = sum(top_combination[0]) + sum(top_combination[1])
            if sum_combination >= sum_highest:
                highest_length = length_combination
                top_combination = sublist

    #Work out lists print order
    top_combination_str = ['','']
    for i in range(0,2):
        top_combination_str[i] = [str(item) for item in top_combination[i]]

    list_a = ' '.join(top_combination_str[0])
    list_b = ' '.join(top_combination_str[1])
    if len(top_combination[0]) >  len(top_combination[1]):
        print(list_a)
        print(list_b)
    elif len(top_combination[0]) < len(top_combination[1]):
        print(list_b)
        print(list_a)
    else:
        if sum(top_combination[0]) >=  sum(top_combination[1]):
            print(list_a)
            print(list_b)
        else:
            print(list_b)
            print(list_a)
