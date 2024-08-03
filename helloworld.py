import pdfkit
import os
# pdfkit.from_url('http://google.com', 'out.pdf')
# Create a class to store the input.json data
#  it should store array of json objects
#  example:
#  {
#         "title": "Introduction",
#         "pages": [
#             {
#                 "title": "Introduction to Modern System Design",
#                 "slug": "introduction-to-modern-system-design"
#             },
#             {
#                 "title": "Course Structure for Modern System Design",
#                 "slug": "course-structure-for-modern-system-design"
#             }
#         ]
#     },

class input_data:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
class pages:
    def __init__(self, title, slug):
        self.title = title
        self.slug = slug

#read the input.json file
import json
with open('../input.json') as f:
    data = json.load(f)
    # print(data)
    # traverse through the json object and store the data in the class
    for i in data:
        folderTitle = i['title']
        pages = i['pages']
        print(folderTitle)
        # Create a folder with the title name
        if not os.path.exists(folderTitle):
            os.makedirs(folderTitle)

        for j in pages:
            title = j['title']
            slug = j['slug']
            print(title, slug)
            # Download the page and store it in the folder folderTitle with the name title
            pdfkit.from_url('http://google.com', folderTitle + '/' + title + '.pdf')            
                       