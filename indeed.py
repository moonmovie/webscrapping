import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL =  "https://kr.indeed.com/jobs?q=python" 

def extract_indeed_pages():

    result = requests.get(URL)
    soup=BeautifulSoup(result.text,"html.parser")


    pagination = soup.find("div", {"class" : "pagination"})
    
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.find("span").string))


    max_page = pages[-1]
  
    return max_page

  
    #del pages[-1]

    #마지막 list 요소만 삭제됨
    #pages = pages[:-1]

def extract_job(html, page):
    title = html.find("div",{"class":"title"}).find("a")["title"]
    company = html.find("span",{"class":"company"}).string
        # company_anchor = company.find("a")
        # if company_anchor is not None:
        #     print(str(company_anchor.string))
        # else:
        #     print(str(company.sting))
    #company = company.strip()
    location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    
    
    return {'title' : title, 'company' : company, 'location' : location, 'link' : f"https://kr.indeed.com/viewjob?jk={job_id}&tk=1e2uhpd790tjk000&from=serp&vjs=3" }
    #{URL}&start={page*LIMIT}&vjk={job_id}

def extract_indeed_jobs(last_page):
    jobs=[]
    for page in range(last_page):
        print(f"scrapping page {page}")
        link = requests.get(f"{URL}&start={page*LIMIT}")
        soup=BeautifulSoup(link.text,"html.parser")
        results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})

        for result in results:
            job=extract_job(result, page)
            jobs.append(job)
    
    return jobs

def get_jobs():
    last_pages = extract_indeed_pages()
    jobs = extract_indeed_jobs(last_pages)

    return jobs