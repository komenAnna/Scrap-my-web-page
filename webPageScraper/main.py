# Step 1: pip install beautiful soup 4
# Step 2: install parser method lxml
# Step 3: import beautiful soup library
# Step 4: open and read the HTML file in the directory using the path
# Step 5: Create an instance of beautiful soup

from bs4 import BeautifulSoup
with open('F:\Web page scraper\webPageScraper\index.html', 'r') as html_file:
    content = html_file.read()
    #print(content) -- displays the raw html content
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify()) -- also displays the raw html content
    #tags = soup.find_all('h5') - #find_all() returns the specified arguemt thsu returns the h5 tags plus its contents
    #print(tags) -- displays the h5 tags + content in a list
    #for course in tags:
        #print(course) -- grabs onlt text minus tags
    course_cards = soup.find_all('div', class_ = 'card')
    #print(course_cards)
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')

# From line 17:
# we create a var called course_cards which returns the content of the div with the class card
# NB: we add the underscore after class_ coz class is a python keyword thus the _ tells bs4 that we are attributing the html tag
# iterate over each course from the course cards list and search for the course name and price