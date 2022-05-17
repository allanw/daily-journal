from playwright.sync_api import sync_playwright
import os
from enchant.checker import SpellChecker

chkr = SpellChecker("en_UK")
chkr.add("Haglund's") # alternatively can maybe use PWL (personal word list) in Enchant

playwright = sync_playwright().start()

browser = playwright.chromium.launch()

page = browser.new_page()

page.goto("https://daily.al.run/")

f2 = open('spelling_errors.txt', 'w')
# break_out_flag = False
for post in page.query_selector_all('p'):
  if not os.path.exists('2022'):
    os.mkdir('2022')
  f = open('2022/{}.txt'.format(post.inner_text().split(':')[0]), 'w')
  url = post.eval_on_selector("a", "el => el.href")
  page2 = browser.new_page()
  page2.goto(url) 
  for para in page2.query_selector_all("p"):
    innerhtml = para.inner_html()
    chkr.set_text(innerhtml)
    for err in chkr:
      f2.write(err.word)
      sug = err.suggest()[0]
      err.replace(sug)
    f.write(chkr.get_text().strip())
#     break_out_flag = True
#     break
#   if break_out_flag:
#     break

browser.close()

playwright.stop()
