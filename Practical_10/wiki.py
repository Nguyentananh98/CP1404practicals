import wikipedia

page_name = input("Please enter page name: ")
# print(wikipedia.summary(page_name))

page_data = wikipedia.page(page_name, auto_suggest=False)
print(page_data.title)
print(page_data.summary)
print(page_data.url)
