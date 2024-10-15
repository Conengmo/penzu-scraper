# Penzu scraper

Export your data from Penzu, then navigate and read your entries from your local computer.

## How to  run

- Get Python
- On the Penzu website, request a login link via email
- In `crawl.py`, insert your login link and your user id at the top of the script
- Run `python crawl.py`
  - It may fail at some point. No worries, just try again.
  - If it fails again immediatly, wait an hour, get a new login link and try again.
- Run `python process_html.py` to create pretty html and Markdown files.
- Open `index.html` in your browser to navigate and read your entries.
