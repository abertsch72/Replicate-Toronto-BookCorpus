
def dedup(filename):
    with open(filename) as f:
        lines = f.readlines()
        print(len(lines))
        lines = list(set(lines))
        print(len(lines))
    with open(filename, 'w') as f:
        f.writelines(lines)

dedup("../data/book_urls-883.txt")
