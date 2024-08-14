from bs4 import BeautifulSoup
import os
import pandas as pd
import json

# Importing the BeautifulSoup for Extracting the data from the files and os for listing the files and pandas for creating the csv file and json for json file

result=[]
# Empty list

for file in os.listdir("JOBDETAILS"):
    # listing all the files
    try:
        # handling the exceptions
        with open(f"JOBDETAILS/{file}") as f:
            # Opening the respective files
            html_doc = f.read()
        #     reading the file and storing to a variable
        soup = BeautifulSoup(html_doc, "html.parser")
        # parsing the html file

        # job Title
        job_title = soup.find("h3")
        if job_title:
            job_title = job_title.text.strip()
        #Finding The job title using Beautiful soup

        # company
        company = soup.find("h4")
        if company:
            company = company.text.strip()
        #Finding The job Company Name using Beautiful soup

        # getting location
        location = soup.find(attrs={"class": "job-search-card__location"})
        if location:
            location = location.text.strip()
        # Finding The job Location using Beautiful soup

        # posted_on
        posted_on = soup.find("time")
        if posted_on:
            posted_on = posted_on.text.strip()
        # Finding The job Posted By by value using Beautiful soup


        # datetime
        posted_date = soup.find("time").get("datetime") if posted_on else None
        # Finding The Posted Date title using Beautiful soup



        # job_id
        job_id = soup.find("div").get("data-entity-urn") if soup.find("div") else None
        if job_id:
            job_id = job_id.split(":")[3].strip()
        # Finding The job_id title using Beautiful soup

        seniority_type = soup.find(attrs={"class":"description__job-criteria-text"})
        # Finding The Seniority_type title using Beautiful soup

        employement_type = soup.find("span",attrs={"class":"description__job-criteria-text"})
        # Finding The Employement_type title using Beautiful soup



        Data = {
            "company": company if company else '',
            "job_title": job_title if job_title else '',
            "linkedin_job_id": job_id if job_id else '',
            "location": location if location else '',
            "posted_on": posted_on if posted_on else '',
            "posted_date": posted_date if posted_date else '',
            "Employment type": employement_type if employement_type else "None",
            "Seniority level": seniority_type if seniority_type else "None"
        }
        # Storing the Data in A Dictionary Format

        # Append data to the result dictionary
        result.append(Data)

    except Exception as e:
        print(e)
    #Printing The Exception

# Convert the result dictionary to a  CSV
df = pd.DataFrame(data=result)
df.to_csv("jobs.csv", index=False)


# Convert the result dictionary to a JSON
with open("Jobs.json","w",encoding="utf-8") as j:
    json.dump(result,j,indent=1)