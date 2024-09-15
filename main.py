import os
import requests as req
import json
from headers import get_img_headers, get_namespace_headers

# 请先设置 headers 模块内的 cookies 的值
# 如何获取: 确保 bilibili 为登录状态, 然后访问下面的 namespace_url 网址，获取 Cookie
base_url = 'https://i0.hdslb.com/bfs/game-static/frame-picture/{}.png'
namespace_url = 'https://api.bilibili.com/x/kv-frontend/namespace/data?appKey=555.77&nscode=34'
namespace = []


def save_img(name, buf):
    if not os.path.exists('./tk/'):
        os.mkdir('./tk/')
    with open(f'tk/{name}.png', 'wb') as f:
        f.write(buf)


def download_img(name: str):
    res = req.get(base_url.format(name), headers=get_img_headers())
    if res.status_code == 200:
        save_img(name, res.content)
    else:
        print(f'ERROR: {res.status_code}')


def download_namespace():
    res = req.get(namespace_url, headers=get_namespace_headers())
    data = res.json()['data']['data']['rolelist.role_name']
    _namespace = json.loads(data)
    for i in _namespace:
        namespace.append(i['name'])


if __name__ == '__main__':
    print('开始下载器者命名空间。。。')
    download_namespace()
    print('开始下载器者透卡。。。')
    print(f'共 {len(namespace)} 位器者')
    for i in namespace:
        print(f'Downloading... {i}')
        download_img(i)
    print('已完成')
