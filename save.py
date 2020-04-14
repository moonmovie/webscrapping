import csv

def save_to_file(jobs):
    file = open("jobs.csv", "w", -1 ,"utf-8")
    wr = csv.writer(file)
    wr.writerow(["title", "company", "location", "link"])
    for job in jobs:
        wr.writerow(list(job.values()))
    return