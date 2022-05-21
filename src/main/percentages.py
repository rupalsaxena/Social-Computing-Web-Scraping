import os
import pandas as pd
import csv

stereotypes= ['older','younger','feminine','masculine']
#or
def Stereotypes():
    directory = 'filtered_synonyms'
    stereotypes=[]
    for filename in os.listdir(directory):

        if filename.endswith(".txt"):
            stereotype = os.path.basename(filename).replace(".txt", "")
            stereotypes.append(stereotype)
    return stereotypes


def arrays_of_stereotypes(stereotype):
    directory = 'filtered_synonyms'
    for filename in os.listdir(directory):
        if filename.endswith(".txt") :
            category_name = os.path.basename(filename).replace(".txt", "")
            if category_name == stereotype :
                str = open('filtered_synonyms/' + filename, 'r').read()
                splitted = str.split()
                d = {category_name: splitted}
                return splitted 


def percentages_stereotype_categories():
    
    # open preprocessed_job_data folder
    directory = 'data/preprocessed_data' 
    for root, subdirectories, files in os.walk(directory):
        # open each folder in preprocessed__job_data that contains a different job category
        for subdirectory in subdirectories:
            # open each file that exists in different job category folder
            for filename in os.listdir(directory+"/"+subdirectory):
                if filename.endswith(".txt"):
                    # import txt file in a string like variable
                    str = open(directory+"/"+subdirectory+'/' + filename, 'r').read()
                    # split the above string to independent words
                    splitted = str.split()
                    
                    """
                    TODO: Check how many words match
                    
                    We have all the stereotypes and in str we have the job advertisement so for each
                    stereotyping category we match the str and produce 4 percentages after that we pass them
                    to the lines below to be written in the appropriate txt file
                    """
                    #word_counter={}
                    #percentage_counter={}
                    dictionary={}
                    #total_words = {"total words": len(splitted)}

                    for stereotype in stereotypes:
                        count=0
                        stereotype_list = arrays_of_stereotypes(stereotype) #stereotype_df = arrays_of_stereotypes()
                        for i in stereotype_list :
                            for j in splitted :
                                if (i.endswith('*') and i[:-1] in j) or (i==j) :
                                    count = count+1
                        percentage= count/ len(splitted) 
                        #word_counter[stereotype]=count #stereotype: feminine,masculine etc
                        #percentage_counter[stereotype]=percentage 
                        dictionary[stereotype] = percentage 
                    dictionary['total_words'] = len(splitted)
           
                    """
                    write percentages in a csv file with the same name as the file of the job ad but, with added
                    _percentages
                    """
                    file = "percentages" + "/" + subdirectory + '/' + filename[:-4] + "_percentages.csv"
                    with open(file, 'w', newline="") as f:
                        for key in dictionary.keys():
                            #print(key, dictionary[key])
                            f.write("%s, %s\n" % (key, dictionary[key])) 

if __name__ == '__main__':
    percentages_stereotype_categories()

    """
    bartender = open("/Users/oroikon/PycharmProjects/Social-Computing-Research-Project/data/raw_job_data/bartender/2ca52b7d17ff81a4.txt", 'r').read()
    print(bartender)
    """