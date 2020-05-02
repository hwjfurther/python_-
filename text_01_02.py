import requests


def translate(word):
    url = "http://fy.iciba.com/ajax.php?a=fy"

    data = {
        'f': 'auto',
        't': 'auto',
        'w': word,
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    }  # User-Agent会告诉网站服务器，访问者是通过什么工具来请求的，如果是爬虫请求，一般会拒绝，如果是用户浏览器，就会应答。
    response = requests.post(url, data=data, headers=headers)  # 发起请求
    json_data = response.json()  # 获取json数据
    # print(json_data)
    return json_data


def run(word):
    result = translate(word)['content']['out']
    print(result)
    return result


def main():
    with open('zon_of_python.txt') as f:
        zh = [run(word) for word in f]

    with open('zon_of_python_zh-CN.txt', 'w') as g:
        for i in zh:
            g.write(i + '\n')


if __name__ == '__main__':
    main()