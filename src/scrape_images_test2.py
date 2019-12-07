import os
os.chdir('/Users/brettharder/Documents/projects/dog_breed_prediction/src/')

from scrapeImages import main as scrape_runner

# Params
search_term = 'french bulldog'
num_images = 50
download_dir = '/Volumes/toshiba_ext 1/dog_breed_prediction/data'

scrape_runner('search {} --num_images {} --directory {}'.format(search_term,num_images,download_dir))