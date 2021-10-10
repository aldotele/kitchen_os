import re

f = open("files/input3", "r")
lines = [line.strip() for line in f.readlines()]
# print(lines)

n_curries = lines[0]
n_customers = len(lines) - 1
pref_list = lines[1:]  # lines of preferences
print(pref_list)


def pair_pref(preferences):
    pref = {}
    client_id = 1
    for el in preferences:
        numbers, letters = re.findall(r'\d+', el), re.findall(r'[a-zA-z]+', el)
        pairs = []
        for i in range(len(numbers)):
            pairs.append(numbers[i] + letters[i])
        pref[client_id] = pairs
        client_id += 1
    return pref


paired = pair_pref(pref_list)
print(paired)


def surely_meat(paired_pref):
    n = len(paired_pref)
    #choice = {}
    ids = []
    for i in range(1, n+1):
        if len(paired_pref[i]) == 1 and paired_pref[i][0][1] == "M":
            # choice[paired_pref[i][0][0]] = paired_pref[i][0][1]
            ids.append(paired_pref[i][0][0])
    return ids


meat_curry_ids = surely_meat(paired)
print(meat_curry_ids)


def optimal(n, meat_only):
    temp = []
    for i in range(1, n+1):
        if str(i) not in meat_only:
            temp.append("V")
        else:
            temp.append("M")
    optimal_comb = " ".join(temp)
    return optimal_comb


print(optimal(int(n_curries), meat_curry_ids))

f.close()
# paired = pair_preferences(p)
# print(paired)
# print(meat_for_sure(paired))

# numbers = re.findall(r'\d+', lines[1])
# print(numbers)
# letters = re.findall(r'[a-zA-z]+', lines[1])
# print(letters)