from playwright.sync_api import sync_playwright
import os
import pyenchant

playwright = sync_playwright().start()

browser = playwright.chromium.launch()

page = browser.new_page()

page.goto("https://daily.al.run/")

break_out_flag = False
for post in page.query_selector_all('p'):
  if not os.path.exists('2022'):
    os.mkdir('2022')
  f = open('2022/foo.txt', 'w')
  url = post.eval_on_selector("a", "el => el.href")
  page2 = browser.new_page()
  page2.goto(url) 
  for para in page2.query_selector_all("p"):
    f.write(para.inner_html())
    break_out_flag = True
    break
  if break_out_flag:
    break

browser.close()

playwright.stop()
