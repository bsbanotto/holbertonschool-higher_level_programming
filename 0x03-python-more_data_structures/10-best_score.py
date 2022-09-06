#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        sorted_scores = sorted(a_dictionary.values())
        sorted_dict = {}

        for i in sorted_scores:
            for k in a_dictionary.keys():
                if a_dictionary[k] == i:
                    sorted_dict[k] = a_dictionary[k]
                    break
        return list(sorted_dict)[-1]
    else:
        return None
