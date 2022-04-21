import os

def get_name(url):
    url = url.split('/')[-1].split('.')[0]
    return url

def gen_commands(filename, max, outfile = None):
    category = filename.split('-')[-1].split('.')[0]
    with open(filename) as f:
        urls = [line.strip() for line in f.readlines()]
        urls = [url for url in urls if not os.path.exists(f"data/{category}/{get_name(url)}.txt")]
    print(len(urls))
    for url in urls[:max]:
        print(f"curl {url} -o data/{category}/{get_name(url)}.txt")
    if outfile:
        with open(outfile, 'w') as f:
            f.write("#!/bin/bash\n")
            f.writelines([f"curl {url} -o data/{category}/{get_name(url)}.txt\n" for url in urls[:max]])

gen_commands("data//book_urls-1206.txt", 50, "getdata.sh")


def remove_throttled(folder):
    count = 0
    for file in os.listdir(folder):
        if "We are currently throttling downloads for users who download more than 500 per day," in ' '.join(open(folder+"/"+file, encoding='latin1').readlines()):
            print(f"rm {folder}/{file}")
            count += 1

    print(count)

remove_throttled("data/1206")
