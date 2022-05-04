
import yaml
import requests
import asyncio
from bs4 import BeautifulSoup
from distutils.log import error

CONFIG_PATH = "src/main/configs/web-scrape.yaml"

def read_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def write_text(content, name):
    with open(name, 'w') as f:
        f.write(content)

def main():
    jobs = read_yaml(CONFIG_PATH)
    for job, link in jobs.items():
        try:
            # way 1
            response = requests.get(link)
            content = BeautifulSoup(response.content, 'html.parser')
            html_list = content.find_all('a', class_="jcs-JobTitle")
            print(html_list)
        except (error):
            print("error occured while getting data for {job} from indeed.com link {link}")


    

if __name__ == "__main__":
    main()