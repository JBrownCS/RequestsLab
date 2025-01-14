'''
Problem Statement:
You're working at a company that sells second-hand cars. Your company constantly collects feedback in the form of customer reviews. 
Your manager asks you to take those reviews (saved as .txt files) and display them on your company's website. 
To do this, you'll need to write a script to convert those .txt files and process them into Python dictionaries, 
then upload the data onto your company's website (currently using Django)

In this case, the example files are stored in the same directory as this program

'''

import requests
import sys
import os


#get the directory of the files, setup list for all posts, 
# and setup the dictionary for the data
fileDir = os.path.dirname(os.path.abspath(sys.argv[0])) + "/data/feedback"
post_list = []
feedback_dict = dict()

#Cycle through the feedback files in the directory to 
# create them as a dictionary
os.chdir(fileDir)
for file in os.listdir(fileDir):
    
    feedback_file = open(file, 'r')
    feedback_info = feedback_file.readlines()
    '''
    Line 1 is the title
    Line 2 is the name of the user
    Line 3 is the date
    Line 4 is the feedback text. Each will be gathered as its own entry
    in the dictionary
    '''
    
    post_list.append({
        'title' :feedback_info[0].strip(),
        'name':feedback_info[1].strip(),
        'date':feedback_info[2].strip(),
        'feedback':feedback_info[3].strip()})
    
    feedback_file.close()

#Now POST the contents to the feedback page on the website
for post in post_list:
    response = requests.post("http://35.184.22.0/feedback/", json=post)
    response.raise_for_status()
