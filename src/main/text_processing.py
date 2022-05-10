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
            text = str(open(complete_link+"/"+str(filename), encoding = "ISO-8859-1").readlines())
            text_tokens = word_tokenize(text)
            #bring to lower
            text_tokens_lower = [token.lower() for token in text_tokens]
            
            #additional words to remove
            non_words_to_add = ["a", "the"]
            non_words_nltk = stopwords.words()
            non_words_nltk.extend(non_words_to_add)
            tokens_without_sw = [word for word in text_tokens_lower if not word in non_words_nltk]
            
            # this keeps empty spaces punctuations marks
            #I put extra filtering for just words. this removes also numbers which I think is valid
            words = list(filter(lambda x: x.isalpha(), tokens_without_sw))
            
    
if __name__ == "__main__":
    main()
