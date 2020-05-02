# import requests
# url = 'https://movie.douban.com/top250'
# res = requests.get(url)
# text = res.text
# text
#
# with open('dou_ban_top50.txt','w')as f:
#     f.write(text)
# print(text)


import re
import requests

def main(url):
    global num
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    req = requests.get(url ,headers=headers)

    pattern = re.compile(r"<span class=\"title\">(.*?)</span>", re.S)
    for name in re.findall(pattern, req.text):
        if name.startswith("&"):
            continue
        else:
            print("%s: %s" % (num, name))
            num += 1

if __name__ == '__main__':
    num = 1
    for i in range(0, 256, 25):
        url = "https://movie.douban.com/top250?start=%s&filter=" % i
        main(url)