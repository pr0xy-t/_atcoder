from itertools import groupby

# "aabbbca" -> [('a', 2), ('b', 3), ('c', 1), ('a', 1)]
def EncRunLength(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

# [('a', 2), ('b', 3), ('c', 1), ('a', 1)] -> "aabbbca"
def DecRunLength(L: "list[tuple(str, int)]") -> str:
    res = ""
    for c, n in L:
        res += c*n
    return res

