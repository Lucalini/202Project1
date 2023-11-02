# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []


def perm_gen_lex(str_in):
    return_list = []
    if len(str_in) == 1:
        return [str_in]
    if len(str_in)== 0:
        return []
    return_list = []
    for letter in str_in:
        str_2 = str_in.replace(f"{letter}", "")
        recursive = perm_gen_lex(str_2)

        for val in recursive:
            return_list.append(letter + val)
    return return_list







