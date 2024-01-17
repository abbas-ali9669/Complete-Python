# In this Exercise we will scraps the link from an html form and store in file


# Solution 1
# with open("links.html", "r") as rf:
#     with open("file.txt", "a") as wf:
#         for line in rf.readlines():
#             if '<a href=' in line:
#                 pos = line.find('<a href=')
#                 first_quote = line.find('\"', pos)
#                 sec_quote = line.find('\"', first_quote+1)
#                 url = line[first_quote+1:sec_quote]
#                 wf.write(url + '\n')


# Solution 2 (Better Solution)
# Upper code will not extract. if two link exists in one line
# But this link will extract all the links though
with open("links.html", "r") as webpage:
    with open("Output.txt", "a") as wf:
        page = webpage.read()
        link_exist = True
        while link_exist:
            pos = page.find('<a href=')
            if pos == -1:
                link_exist = False
            else:
                first_quote = page.find('\"', pos)
                sec_quote = page.find('\"', first_quote+1)
                url = page[first_quote+1:sec_quote]
                wf.write(url + '\n')
                page = page[sec_quote:]