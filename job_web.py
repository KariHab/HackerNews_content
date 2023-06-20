import requests
from bs4 import BeautifulSoup as sp

my_url = "https://emplois.ca.indeed.com/"
page = requests.get(url)
soup = sp(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
# print(results.prettify())
python_jobs = results.find_all(
    "h2", string=lambda text: "software" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
        
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

