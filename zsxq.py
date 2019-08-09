# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=chrome_options)
# res = driver.get("http://www.baidu.com")
# print(res)
# driver.close()
# //*[@id="topic-detail-container"]/div/div[2]/app-talk-content/div/div
from selenium import webdriver
import time
from xml.etree.ElementInclude import ElementTree

import lxml.html as html

links = ['https://t.zsxq.com/zjIuZ3v']
# with open('input.txt', 'r') as f:
#     x = f.readline()
#     while x:
#         x = f.readline()
#         if 'https://t.zsxq.com' in x:
#             links.append(x.strip())

# for i in os.walk('./chemas', topdown=True, οnerrοr=None, followlinks=False):
# files = set(map(lambda x: x.strip(".html"), os.listdir('./schemas')))

driver = webdriver.Chrome()
for i in links:
    driver.get(i)
    time.sleep(10)

    with open('./schemas/{}.html'.format(i.strip("https://t.zsxq.com/")), 'w') as f:
        f.write(driver.page_source)

# root = html.fromstring(driver.page_source)
# res = root.xpath('//*[@id="topic-detail-container"]/div/div[2]/app-talk-content/div/div')

pass
driver.quit()
driver.close()
