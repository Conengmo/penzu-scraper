import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# you can receive a login link via email, paste it here
magic_link = ""
# this is the number in the url: https://penzu.com/journals/<user_id>
user_id = ""


driver = webdriver.Safari()

driver.get(magic_link)

time.sleep(4)

url_pattern = "https://penzu.com/journals/{}/entries?page={}"
urls_to_visit = []
for i in range(1, 15):
    url = url_pattern.format(user_id, i)
    driver.get(url)
    time.sleep(2)
    elements = driver.find_elements(By.CSS_SELECTOR, 'a.ng-scope')
    urls_to_visit.extend(
        [e.get_attribute('href').strip() for e in elements]
    )

with open("urls.txt", "w") as f:
    for url in urls_to_visit:
        print(url, file=f)


with open("urls.txt", "r") as f:
    urls_to_visit = [url.strip() for url in f]

os.makedirs("htmls", exist_ok=True)

for i, url in enumerate(urls_to_visit):
    driver.get(url)

    time.sleep(4)

    element = driver.find_element(By.CSS_SELECTOR, "textarea.h1")
    title = element.get_attribute('value').strip()

    element = driver.find_element(By.CSS_SELECTOR, "a.created-at")
    date = element.get_attribute('innerHTML').replace("&nbsp;", " ").strip()

    element = driver.find_element(By.ID, "cke_editor")
    element = element.find_element(By.CLASS_NAME, "cke_wysiwyg_div")
    html = element.get_attribute('innerHTML').strip()

    with open(f"htmls/{i}.html", "w") as f:
        print(f"<h1>{title}</h1>", file=f)
        print(f"<p class='date'>{date}</p>", file=f)
        print("<hr>", file=f)
        print(html, file=f)


driver.quit()
