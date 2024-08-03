import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import base64  # Import base64 module for decoding
import json
import os


class input_data:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
class pages:
    def __init__(self, title, slug):
        self.title = title
        self.slug = slug

# Define a method to convert a page to PDF
def convert_page_to_pdf(driver, url, output_file):
    # Navigate to the page
    driver.get(url)

    # Add delay to allow the page to load
    time.sleep(30)
    #  ensure the page is fully loaded
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)

    # Define the PDF options
    pdf_options = {
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': True,
        # 'paperWidth': 8.27,
        # 'paperHeight': 11.69
    }

    # Convert page to PDF
    pdf = driver.execute_cdp_cmd('Page.printToPDF', pdf_options)

    # Decode the base64 PDF data
    pdf_data = pdf['data']
    pdf_file = base64.b64decode(pdf_data)



    # Save the PDF file
    with open(output_file, 'wb') as f:
        f.write(pdf_file)


# Set up Chrome options and service
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:8989")
# service = Service('path/to/chromedriver')  # Update the path to your chromedriver executable
driver = webdriver.Chrome( options=chrome_options)


with open('../input.json') as f:
    data = json.load(f)
    # print(data)
    # traverse through the json object and store the data in the class
    a = 0
    for i in data:
        a = a+1
        folderTitle = i['title']
        pages = i['pages']
        folderTitle = str(a)+'.'+folderTitle 
        print(folderTitle)
        # Create a folder with the title name
        if not os.path.exists(folderTitle):
            os.makedirs(folderTitle)

        b= 0
        for j in pages:
            b = b+1
            title = j['title']
            title = str(a)+'.'+str(b)+'.'+title
            slug = j['slug']
            print(title, slug)

            # Download the page and store it in the folder folderTitle with the name title
            convert_page_to_pdf(driver, "https://www.educative.io/courses/grokking-modern-system-design-interview-for-engineers-managers/"+slug, folderTitle + '/' + title + '.pdf')
            #  add random delay
            # time.sleep(a+b*2)

# Close the browser
driver.quit()
