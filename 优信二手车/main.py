import master
import redis_or
import slave


# a=master.Master_Spider("shenzhen")
# html = a.get_html("https://www.xin.com/beijing/benchi/i3/")
# urls=a.get_detail_url(html)
q = redis_or.Redis_Data()
# for url in urls:
#     q.set_into_data("test_car_urls",url)

url = q.pop_data("test_car_urls")
html = master.Master_Spider("shenzhen").get_html(url)
a = slave.Slave_Spisder()
data = a.parse_detail_data(html)
print(data)
