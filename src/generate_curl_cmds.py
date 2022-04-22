import os

filelength = 0
def get_name(url):
    url = url.split('/')[-1].split('.')[0]
    return url

def gen_commands(filename, max, outfile = None):
    global filelength
    category = filename.split('-')[-1].split('.')[0]
    with open(filename) as f:
        urls = [line.strip() for line in f.readlines()]
        urls = [url for url in urls if not os.path.exists(f"data/{category}/{get_name(url)}.txt")]
    print(len(urls))
    max = max - filelength
    for url in urls[:max]:
        print(f"curl {url} -o data/{category}/{get_name(url)}.txt")
    if outfile:
        with open(outfile, 'a') as f:
            f.write("#!/bin/bash\n")
            f.writelines([f"curl {url} -o data/{category}/{get_name(url)}.txt\n" for url in urls[:max]])
    filelength += len(urls[:max])



def remove_throttled(folder):
    count = 0
    for file in os.listdir(folder):
        if "We are currently throttling downloads for users who download more than 500 per day," in ' '.join(open(folder+"/"+file, encoding='latin1').readlines()):
            print(f"rm {folder}/{file}")
            count += 1

    print(count)


outfile = "getdata.sh"
with open(outfile, 'w') as f:
    pass # clean out file
categories = [883, 1206, 1235, 1213, 892, 1126, 871, 882, 61, 873, 874, 877, 1018, 879]
for category in categories:
    gen_commands(f"data/book_urls-{category}.txt", 50, "getdata.sh")

    remove_throttled(f"data/{category}")
    if filelength >= 50:
        break
