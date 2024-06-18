# .csv comma seperated value
# .txt text file


# with open('message.text','w') as file:
#     file.write(' I love You Python mama')

# with open('message.text','a') as file:
#     file.write(' I love You Python mama')


with open('message.text','r') as file:
    text=file.read()
    print(text)
