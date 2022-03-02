import requests
import re
from bs4 import BeautifulSoup

url = "https://www.indeed.com/jobs?q=developer"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup)
jobs_html = soup.findAll("h2", class_="jobTitle")

jobs_clean = []
pattern = "<span title=\"(.*?)\">"
for job in jobs_html:
    jobs_clean.append(re.search(pattern, str(job)).group(1))

print(jobs_clean)
