# 此处填入 Cookie
cookies = ""
# 来自 Firefox 控制台复制全部
img_headers_ = [
    {
        "name": "Accept",
        "value": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8"
    },
    {
        "name": "Accept-Encoding",
        "value": "gzip, deflate, br, zstd"
    },
    {
        "name": "Accept-Language",
        "value": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
    },
    {
        "name": "Connection",
        "value": "keep-alive"
    },
    {
        "name": "Host",
        "value": "i0.hdslb.com"
    },
    {
        "name": "Priority",
        "value": "u=0, i"
    },
    {
        "name": "Referer",
        "value": "https://game.bilibili.com/"
    },
    {
        "name": "Sec-Fetch-Dest",
        "value": "document"
    },
    {
        "name": "Sec-Fetch-Mode",
        "value": "navigate"
    },
    {
        "name": "Sec-Fetch-Site",
        "value": "cross-site"
    },
    {
        "name": "Sec-Fetch-User",
        "value": "?1"
    },
    {
        "name": "Upgrade-Insecure-Requests",
        "value": "1"
    },
    {
        "name": "User-Agent",
        "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0"
    }
]
namespace_headers_ = [
    {
        "name": "Accept",
        "value": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8"
    },
    {
        "name": "Accept-Encoding",
        "value": "gzip, deflate, br, zstd"
    },
    {
        "name": "Accept-Language",
        "value": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
    },
    {
        "name": "Connection",
        "value": "keep-alive"
    },
    {
        "name": "Host",
        "value": "api.bilibili.com"
    },
    {
        "name": "Cookie",
        "value": cookies
    },
    {
        "name": "Priority",
        "value": "u=0, i"
    },
    {
        "name": "Sec-Fetch-Dest",
        "value": "document"
    },
    {
        "name": "Sec-Fetch-Mode",
        "value": "navigate"
    },
    {
        "name": "Sec-Fetch-Site",
        "value": "none"
    },
    {
        "name": "Sec-Fetch-User",
        "value": "?1"
    },
    {
        "name": "TE",
        "value": "trailers"
    },
    {
        "name": "Upgrade-Insecure-Requests",
        "value": "1"
    },
    {
        "name": "User-Agent",
        "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0"
    }
]
headers = {}
namespace_headers = {}
# 转为字典
for i in img_headers_:
    headers[i['name']] = i['value']
for i in namespace_headers_:
    namespace_headers[i['name']] = i['value']


def get_img_headers():
    return headers


def get_namespace_headers():
    return namespace_headers
