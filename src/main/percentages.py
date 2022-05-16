import os
import pandas as pd

def arrays_of_stereotypes():
    directory = 'filtered_synonyms'
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            str = open('filtered_synonyms/'+filename, 'r').read()
            splitted = str.split()
            category_name = os.path.basename(filename).replace(".txt","")
            d = {category_name: splitted}
            df = pd.DataFrame(data=d)
            print(df)

def percentages_stereotype_categories():





if __name__ == '__main__':
    arrays_of_stereotypes()

    """
    bartender = open("/Users/oroikon/PycharmProjects/Social-Computing-Research-Project/data/raw_job_data/bartender/2ca52b7d17ff81a4.txt", 'r').read()
    print(bartender)
    """