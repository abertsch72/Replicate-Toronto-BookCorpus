
def dedup(filename):
    with open(filename) as f:
        lines = f.readlines()
        print(len(lines))
        lines = list(set(lines))
        lines = ["https://www.smashwords.com/" + url.strip("https://www.smashwords.com") for url in lines]
        print(len(lines))
    with open(filename, 'w') as f:
        f.writelines(lines)

categories = {"horror": 883, "fantasy": 1206, "romance": 1235,
            "science fiction": 1213, "adventure": 892, "sports": 1126,
            "western": 871, "humor & comedy": 882, "children's": 61, "urban": 873,
            "thriller & suspense": 874, "religious": 877, "YA/teen": 1018, "mystery & detective": 879}

for genre in categories:
    dedup(f"../data/book_urls-{categories.get(genre)}.txt")
