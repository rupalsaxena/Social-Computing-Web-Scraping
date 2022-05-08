# Social-Computing-Research-Project
Research Question: Determine the presence of age and gender-discriminating language in online job advertisements across heterogenous job industries in the United States?

## To web-scrape the job data from Indeed.com
Run the following to web-scrape the job data from indeed.com
```
python3 src/main/web-scrape.py
```
This command will create folders in data repository. There will be folders of job categories mentioned in src/main/configs/web-scrape.yaml file. In each job-category folder, there will be id.txt files, where id is job id for a job in indeed.com.