import re
import pprint

f = open("files/input3", "r")
lines = [line.strip() for line in f.readlines()]
# print(lines)

n_curries = lines[0]
n_customers = len(lines) - 1
pref_list = lines[1:]  # lines of preferences
print(pref_list)


def surely_meat(paired_pref):
    n = len(paired_pref)
    #choice = {}
    ids = []
    for i in range(1, n+1):
        if len(paired_pref[i]["curry_id"]) == 1 and paired_pref[i]["taste"] == ["M"]:
            # choice[paired_pref[i][0][0]] = paired_pref[i][0][1]
            ids.append(paired_pref[i]["curry_id"][0])
    return ids


def pair_pref(preferences, meat_ids=[]):
    pref = {}
    client_id = 1
    i = 0
    for el in preferences:
        client_pref = {"curry_id": "", "taste": ""}
        numbers, letters = re.findall(r'\d+', el), re.findall(r'[a-zA-z]+', el)
        """
        ignora i numeri che già so essere meat only
        """

        client_pref["curry_id"] = numbers
        client_pref["taste"] = letters
        pref[client_id] = client_pref
        client_id += 1
    meat_ids = surely_meat(pref)  # qui ho gli id dei curry che sono sicuramente mea
    """
    reparse here the dictionary
    """


    return pref, meat_ids


paired, meat_ids = pair_pref(pref_list)
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(paired)
print(meat_ids)


# meat_curry_ids = surely_meat(paired)
# print(meat_curry_ids)


def optimal(n, meat_only, paired=""):
    temp = []
    for i in range(1, n+1):
        if str(i) not in meat_only:
            temp.append("V")
        else:
            temp.append("M")
    optimal_comb = " ".join(temp)
    return optimal_comb


print(optimal(int(n_curries), meat_ids))

f.close()