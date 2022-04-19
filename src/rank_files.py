

categories = {"horror": 883, "fantasy": 1206, "romance": 1235,
            "science fiction": 1213, "adventure": 892, "sports": 1126,
            "western": 871, "humor & comedy": 882, "children's": 61, "urban": 873,
            "thriller & suspense": 874, "religious": 877, "YA/teen": 1018, "mystery & detective": 879}

import os

num_books = {}
for genre in categories:
    filename = f"../data/book_urls-{categories.get(genre)}.txt"
    if os.path.isfile(filename):
        with open(filename) as f:
            lines = [line for line in f.readlines() if line.strip() != ""]
            num_books[genre] = len(lines)

sorted_list = sorted(num_books, reverse=True, key=num_books.get)
total = 0
for genre in sorted_list:
    print(f"{genre} ({categories.get(genre)}):\t{num_books.get(genre)}")
    total += num_books.get(genre)

print(f"total: {total}")
