"""
Scrape dog breed images

E.g. for command line
!python scrapeImages.py --search "cat" --num_images 10 --directory "/Users/gene/Downloads"
"""
import os
os.chdir('/Users/brettharder/Documents/projects/dog_breed_prediction/src/')

import sys
sys.path.insert(0, "/Users/brettharder/Documents/projects/dog_breed_prediction/src/")

from scrapeImages import main as scrape_runner

# Params
search_term = 'french bulldog'
num_images = 50
download_dir = '/Volumes/toshiba_ext 1/dog_breed_prediction/data'

def main():
    command = (
        '--search {} '
        '--num_images {} '
        '--directory {}'
    ).format(search_term,num_images,download_dir)
    scrape_runner(command.split(' '))

if __name__ == '__main__':
    main()
