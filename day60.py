def find_children(dancing_brigade):
    return "".join(sorted(dancing_brigade, key=lambda x:(x.lower(), x)))