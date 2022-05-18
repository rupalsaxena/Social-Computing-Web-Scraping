import os
import pandas as pd


def arrays_of_stereotypes():
    directory = 'filtered_synonyms'
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            str = open('filtered_synonyms/' + filename, 'r').read()
            splitted = str.split()
            category_name = os.path.basename(filename).replace(".txt", "")
            d = {category_name: splitted}
            df = pd.DataFrame(data=d)
            return df


def percentages_stereotype_categories():
    # open raw_job_data folder
    directory = 'data/raw_job_data'
    for root, subdirectories, files in os.walk(directory):
        # open each folder in raw_job_data that contains a different job category
        for subdirectory in subdirectories:
            # open each file that exists in different job category folder
            for filename in os.listdir(directory+"/"+subdirectory):
                if filename.endswith(".txt"):
                    # import txt file in a string like variable
                    str = open(directory+"/"+subdirectory+'/' + filename, 'r').read()
                    # split the above string to independent words
                    splitted = str.split()
                    print(splitted)


                    """
                    TODO: Check how many words match
                    
                    We have all the stereotypes and in str we have the job advertisement so for each
                    stereotyping category we match the str and produce 4 percentages after that we pass them
                    to the lines below to be written in the appropriate txt file
                    """

                    """
                    write percentages in a txt file with the same name as the file of the job ad but, with added
                    _percentages
                    """

                    with open(filename + "_percentages.txt", "a") as f:
                        f.write("Starting of Synonyms of the Words from the Sentences: " +"the percetage"+ "\n")
                        f.close()


if __name__ == '__main__':
    percentages_stereotype_categories()

    """
    bartender = open("/Users/oroikon/PycharmProjects/Social-Computing-Research-Project/data/raw_job_data/bartender/2ca52b7d17ff81a4.txt", 'r').read()
    print(bartender)
    """
