from bs4 import BeautifulSoup

with open("website.html", "r", encoding="utf-8") as html_file:                                                          #open and print the html file
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml")


    #returns the first occurence of the tag
    get_first_tag = soup.find("li")

    #returns list of all the tags
    get_all_tags = soup.find_all("li")

    #get the given tags by class or all tags by class
    get_all_tags_by_class = soup.find_all("h3", class_="heading")

    #get the given tags by id or all tags by id
    get_all_tags_by_id = soup.find_all(id="name")

    #get the text from the tag
    for i in get_all_tags_by_class:
        get_text_from_tag = i.text

