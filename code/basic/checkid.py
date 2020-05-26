def checkId(s: str):
    if s[0].isalpha() or s[0] == "_":
        for ch in s:
            if not ch.isalnum() and not ch == "_":
                return "Error. Other chars must be alphas number or _."
        return "Valid identifier."
    else:
        return "Error. First char must be alphas or _."


print(checkId(input()))
