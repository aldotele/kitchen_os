from helper.file_parse import get_lines, file_check, extract_num_let
import os


class KitchenOS:
    def __init__(self, file_content):
        all_lines = get_lines(file_content)
        if file_check(all_lines) == "ok":
            self.n_curries = all_lines[0]  # number of curry types
            self.n_customers = len(all_lines) - 1
            self.full_pref = all_lines[1:]  # raw preferences of the input files
            self.is_meat_asked = False
            self.is_veggie_asked = False
            self.veggie_only, self.meat_only = self.recursive_parser(self.full_pref)
            self.optimal_sequence = KitchenOS.find_optimal(self.veggie_only, self.meat_only)

    def get_meat_only(self, pref, n_curries):
        """
        :param pref: list
        :param n_curries: integer
        :return: list
        """
        meat_ids = []  # will store the identifiers of meat only curry types
        for p in pref:
            numbers, letters = extract_num_let(p, n_curries)
            if not self.is_meat_asked:
                if "M" in letters:
                    self.is_meat_asked = True
            if not self.is_veggie_asked:
                if "V" in letters:
                    self.is_veggie_asked = True
            if "V" not in letters:
                meat_ids += numbers
        if self.is_meat_asked and self.is_veggie_asked and int(n_curries) < 2:
            print("no solution exists")
            quit()
        return list(set(meat_ids))  # set is used to return unique identifiers

    @staticmethod
    def update_pref(pref, meat_ids):
        """
        :param pref: list of preferences
        :param meat_ids: list of only meat identifiers
        :return: list of preferences rearranged, keeping those who will still count for deciding M or V
        """
        rearranged = []
        j = 0
        for p in pref:
            rearranged.append("")
            numbers, letters = extract_num_let(p)
            for i in range(len(numbers)):
                # only keeping the preferences for the curry types that are not surely M (meat)
                if numbers[i] not in meat_ids:
                    rearranged[j] += f" {numbers[i]} {letters[i]}"  # spaces matter here!
            rearranged[j] = rearranged[j].strip()
            j += 1
        return rearranged

    @staticmethod
    def get_veggie_only(parsed_pref):
        """
        :param parsed_pref: list of parsed and rearranged preferences
        :return: list of identifiers of the curry types that will be V (veggie)
        """
        veggie_ids = []  # will store the identifiers of vegetarian only curry types
        for p in parsed_pref:
            numbers = extract_num_let(p)[0]
            veggie_ids += numbers
        return list(set(veggie_ids))

    def recursive_parser(self, p, meat_ids=[]):
        """
        :param p: list of raw preferences for each client
        :param meat_ids: list of identifiers for the curry types that will have to be M (meat) taste
        :return: either a tuple of veggie-meat identifiers or the function itself
        """
        meat_ids += self.get_meat_only(p, self.n_curries)  # as the parser keeps parsing, new identifiers get added
        parsed = self.update_pref(p, meat_ids)
        if parsed == p:  # BASE CASE: no more possibilities for meat curry types
            veggie_ids = self.get_veggie_only(parsed)  # the remaining ones can all be made veggie
            return list(set(veggie_ids)), list(set(meat_ids))
        return self.recursive_parser(parsed, meat_ids)  # RECURSIVE CASE: still need to parse preferences

    @staticmethod
    def find_optimal(veggie_ids, meat_ids):
        """
        :param veggie_ids: list of identifiers of the vegetarian curry types
        :param meat_ids: list of identifiers of the meat curry types
        :return: string (sequence of M/V for each curry type)
        """
        comb = {}
        for n in veggie_ids:
            comb[n] = "V"
        for n in meat_ids:
            comb[n] = "M"
        ordered_keys = sorted(comb)
        optimal = []
        for k in ordered_keys:
            optimal.append(comb[k])
        return " ".join(optimal)  # converts the list to a string with in-between spaces


if __name__ == '__main__':
    filename = input("enter the name of the input file: ")
    filepath = os.path.join("files", filename)
    try:
        f = open(filepath, "r")  # change input file here!
        optimal_curry = KitchenOS(f)  # business logic triggered
        print(optimal_curry.optimal_sequence)
        f.close()
    except FileNotFoundError:
        print("file not found. Please retry.")

