import os
import shutil
import random

DATAPATH = "data/raw_job_data"
SAMPLED_DATAPATH = "data/raw_job_data_balanced"
BALANCE = 90

for job_category in os.listdir(DATAPATH):
    
    # ignoring .DS-Store kind of files
    if job_category.startswith('.'):
        continue

    print(job_category)
    job_folder = os.path.join(DATAPATH, job_category)
    print("started", job_category)

    filenames = []
    for filename in os.listdir(job_folder):
        filenames.append(filename)
    print("length of folder before", len(filenames))    

    sampled_dir = os.path.join(SAMPLED_DATAPATH, job_category)
    if not os.path.exists(sampled_dir):
        os.makedirs(sampled_dir)
    
    if len(filenames) > BALANCE:
        sampled_filenames = random.sample(set(filenames), BALANCE)
    else:
        sampled_filenames = filenames
    print("length of folder after", len(sampled_filenames))

    for filename in os.listdir(job_folder):
        if filename in sampled_filenames:
            job_file = os.path.join(job_folder, filename)
            shutil.copy(job_file, sampled_dir)
    print("done: ", job_category)
    