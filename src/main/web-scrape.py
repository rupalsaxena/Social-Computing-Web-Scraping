
import os
import yaml
import random
import requests
import numpy as np
from bs4 import BeautifulSoup

# web scraping job description data from indeed.com USA version

CONFIG_PATH = "src/main/configs/web-scrape.yaml"
base_url = "https://www.indeed.com/viewjob?jk="

#to define ones all the pages to get
pages_results = np.array(range(40))*10

def read_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def write_text(content, name):
    with open(name, 'w') as f:
        f.write(content)

def main():
    job_categories = read_yaml(CONFIG_PATH)

    # looping for all job categories in data
    for job_name, link in job_categories.items():
      print("working with", job_name)
      #get all links
      links_full = []
      [links_full.append(link+"&start="+str(x)) for x in pages_results]

      full_html_list =[]
      for link in links_full:
            # get the data from website--> looping because there is inconsistency in reponse. Sometimes reponse is empty.
            run = True
            while (run):
                response = requests.get(link)
                content = BeautifulSoup(response.content, 'html.parser')
                html_list = content.find_all('a', class_="jcs-JobTitle")
                if len(html_list) > 0:
                    run = False
                    for html_element in html_list:
                        full_html_list.append(html_element)
    
      #some ids are duplicated
      full_html_list = list(set(full_html_list))
      full_html_list = random.sample(full_html_list, 300)
      
        # for each job in list
      for element in full_html_list:
        # get job ids from scraped data
        job_id = element.attrs["data-jk"]
        full_job_url = base_url+job_id

        # looping until response is not received
        run_description = True
        while (run_description):
            # get full job descirption using the link made with ids
            response = requests.get(full_job_url)
            content_des = BeautifulSoup(response.content, 'html.parser')
            html_des_list = content_des.find_all('div', class_="jobsearch-jobDescriptionText")

            # checking if received content list is greater than 0
            if len(html_des_list) > 0:
                text_data = ""
                html_format = html_des_list[0]

                # find all the element data which are either paragraphs or lines
                paras = html_format.find_all("p")
                lines = html_format.find_all("li")

                #skipping divs for now
                #divs = html_format.find_all("div")

                # converting paragraph elements to text and saving it in text_data
                for para in paras:
                    text = para.text
                    if len(text) > 0:
                        text_data = text_data + " " + text

                # converting lines elements to text and saving it in text_data
                for line in lines:
                    text = line.text
                    if len(text) > 0:
                        text_data = text_data + " " + text

                # skippings divs for now since data is repeated
                #for div in divs:
                #    text = div.text
                #    text_data = text_data + " " + text

                foldername = "data/raw_job_data/" + str(job_name)

                # checking if text_data len is greater than 0, if so saving the file
                if not os.path.exists(foldername):
                    print("creating folder with name:", foldername)
                    os.makedirs(foldername)

                if len(text_data) > 0:
                    filename = foldername + "/" + str(job_id) + ".txt"
                    print("writing in:", filename)
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(text_data)

                run_description = False

if __name__ == "__main__":
    main()