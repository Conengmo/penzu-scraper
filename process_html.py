import os
import re

from bs4 import BeautifulSoup
from html2text import html2text


os.makedirs("htmls_pretty", exist_ok=True)
os.makedirs("texts", exist_ok=True)

for filename in os.listdir("htmls"):
    with open(f"htmls/{filename}") as f:
        html = "".join(f.readlines())

    html = re.sub(r"(?:<p><br></p>){3,}", "<hr>", html)
    html = re.sub(r"(?:<p><br></p>){2,}", "<p><br /></p>", html)
    html = re.sub(r"<p><br></p>", "", html)

    needle = """<span style="font-size:11pt"><span style="line-height:107%"><span style="font-family:&quot;Calibri&quot;,sans-serif">"""
    if needle in html:
        html = html.replace(
            """<span style="font-size:11pt"><span style="line-height:107%"><span style="font-family:&quot;Calibri&quot;,sans-serif">""",
            "",
        )
        html = html.replace("</span></span></span>", "")

    soup = BeautifulSoup(html, 'html.parser')
    formatted_html = soup.prettify()

    with open(f"htmls_pretty/{filename}", "w") as f:
        f.write(formatted_html)

    text = html2text(html)
    with open(f"texts/{filename.replace('.html', '.md')}", "w") as f:
        f.write(text)

