import os
#import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

jobs = ['plumber', 'computer-engineer', 'nurse', 'oil-field-engineer',
        'clerk', 'graphic-designer', 'doctor', 'bartender', 'Customer-Service-Representative', 'house-cleaner']
    
#link example
path_texts = "data/raw_job_data"

def main():
    for job_name in jobs:
        complete_link = path_texts+"/"+job_name
        for filename in os.listdir(complete_link):
            text = str(open(complete_link+"/"+str(filename)).readlines())
            text_tokens = word_tokenize(text)
            tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
            
            # this keeps empty spaces punctuations marks
            #I put extra filtering for jsut words. this removes also numbers which I think is valid
            words = list(filter(lambda x: x.isalpha(), tokens_without_sw))
            
    
if __name__ == "__main__":
    main()
