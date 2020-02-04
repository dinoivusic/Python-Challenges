def generate_hashtag(s):
    if len(s) > 140 or len(s) == 0:
        return False
    word = s.title()
    word = "".join(word.split())
    return '#' + word
