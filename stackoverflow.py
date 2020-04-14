import requests
from bs4 import BeautifulSoup

URL="https://stackoverflow.com/jobs?q=python"

def extract_so_pages():
    
    result = requests.get(URL)
    soup=BeautifulSoup(result.text,"html.parser")


    pagination = (soup.find("div", {"class" : "s-pagination"}).find_all("a"))
    last_page =pagination[-2].get_text(strip=True)
 
    return int(last_page)
        

def extract_so_jobs(last_page):
    jobs = []
    for page in range(5):
        print(f"stackoverflow jobs {page}")
        link = requests.get(f"{URL}&pg={page+1}")
        soup=BeautifulSoup(link.text,"html.parser")
        results = soup.find_all("div",{"class" : "-job"})
        for result in results:
            job = info_so_jobs(result, last_page)
            jobs.append(job)
    
    return jobs
    
def info_so_jobs(html, page):
    title = html.find("a", {"class":"s-link"})["title"]
    company = html.find("h3", {"class" : "fc-black-700"}).find("span").get_text(strip=True)
    location = html.find("span",{"class" : "fc-black-500"}).get_text(strip=True)
    link =html["data-jobid"]
    
    return {"title" : title, "company" : company, "location" : location, "link" : f"https://stackoverflow.com/jobs/{link}"}

def get_so_jobs():
    last_page = extract_so_pages()
    jobs_test = extract_so_jobs(last_page)
    
    return jobs_test


