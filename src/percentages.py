import os


def arrays_of_stereotypes():
    directory = '/Users/oroikon/PycharmProjects/Social-Computing-Research-Project/filtered_synonyms'
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filename = str.split()
            print(filename)




if __name__ == '__main__':
    arrays_of_stereotypes()

    """
    bartender = open("/Users/oroikon/PycharmProjects/Social-Computing-Research-Project/data/raw_job_data/bartender/2ca52b7d17ff81a4.txt", 'r').read()
    print(bartender)
    """