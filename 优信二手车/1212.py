import requests
from lxml import etree
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}

url = "https://item.jd.com/6186384.html"
r = requests.get(url,headers = HEADERS)
html = etree.HTML(r.text)
items = html.xpath('/html/body/div[7]/div/div[2]/div[3]/div/div[1]/div[2]/span[1]/span[2]/text()')
print(r.status_code)
print(r.text)
f = open("tststs.html","w")
f.write(r.text)
f.close()
