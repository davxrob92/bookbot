def count_book_words(text):
    return len(text.split())

def get_book_characters(path_to_file):
    with open(path_to_file) as file:
        characters = {}
        for f in file:
            fl = f.lower()
            for j in fl:
                if j not in characters:
                    characters[j] = 0
                characters[j] += 1
    return characters

def sort_on(items):
    return items["num"]

def sorted_dict(webster):
    web = []
    for k, v in webster.items():
        j = {"char": k, "num": v}
        web.append(j)
    web.sort(reverse=True, key=sort_on)
    print(web)
    return web