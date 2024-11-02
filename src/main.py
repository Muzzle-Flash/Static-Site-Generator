from move_to_destination import move_to_destination
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive
import os

def main():
    move_to_destination('static', 'public')
    generate_pages_recursive('content', 'template.html', 'public')
    #generate_page('content/index.md', 'template.html', 'public/index.html')
    
    


if __name__=="__main__":
    main()